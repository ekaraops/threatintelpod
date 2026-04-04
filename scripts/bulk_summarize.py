#!/usr/bin/env python3
"""
ThreatIntelPod - Bulk Video Summarizer
Processes a list of YouTube URLs: fetches transcript, generates AI summary, pushes to GitHub.
"""

import json
import re
import time
import urllib.request
import urllib.parse
import base64
import ssl
from datetime import datetime

# ============================================
# CONFIGURATION - Fill in your API keys
# ============================================
SUPADATA_API_KEY = "YOUR_SUPADATA_API_KEY"
OPENROUTER_API_KEY = "YOUR_OPENROUTER_API_KEY"
GITHUB_PAT = "YOUR_GITHUB_PAT"
GITHUB_REPO = "ekaraops/threatintelpod"
OPENROUTER_MODEL = "google/gemma-4-26b-a4b-it"

# Videos to process
VIDEOS = [
    "https://www.youtube.com/watch?v=3lRlZW9-eKk",
    "https://www.youtube.com/watch?v=1-tXaeUzehc",
    "https://www.youtube.com/watch?v=5oVVcPZ3B3k",
    "https://www.youtube.com/watch?v=K9l7fESVUFc",
    "https://www.youtube.com/watch?v=eCp6ixlzyh0",
    "https://www.youtube.com/watch?v=WP-ydzUq1RY",
    "https://www.youtube.com/watch?v=1sd26pWhfmg",
    "https://www.youtube.com/watch?v=l9CPmPk2R-M",
    "https://www.youtube.com/watch?v=kgwvAyF7qsA",
    "https://www.youtube.com/watch?v=B_7RpP90rUk",
    "https://www.youtube.com/watch?v=rO2yA52U_i4",
]

SYSTEM_PROMPT = """You are an expert cybersecurity analyst who creates structured podcast summaries for CISOs, SOC teams, and security leaders. Your summaries must be clear, actionable, and written in simple English (5th-6th grade reading level). Focus only on useful, high-signal insights. Do NOT include fluff or repetition. If something is unclear, state it clearly instead of guessing.

Format your output in Markdown with the following sections, each with 5-6 bullet points:

## TL;DR (Too Long, Didn't Read)
Provide 5-6 bullet points capturing the most critical insights for decision-making.

## New Tools, Techniques, and Tactics
Any new tools, frameworks, attack methods, or workflows mentioned. Include names and short explanations.

## Detection & Defense Insights
Detection ideas, signals, logs, or behaviors. Defensive recommendations. SOC-relevant insights (SIEM, EDR, identity, etc.)

## Real-World Examples & Stories
Personal experiences shared by speakers. Case studies or incidents. Practical lessons learned.

## Research, References & Resources
Research papers, blogs, tools, datasets, or frameworks mentioned. External references worth exploring.

## Key Industry Insights & Trends
Important observations about the cybersecurity landscape. Emerging trends or early signals. Changes in attacker behavior or technology.

## Business & Risk Implications
Translate technical insights into business impact. Who is affected and how (enterprise, SMB, SaaS, etc.). Financial, operational, or reputational risks.

## Opinions vs Facts
Clearly separate verified facts/observations from opinions, predictions, or assumptions.

## Contradictions & Debates (if any)
Capture disagreements or alternative viewpoints. Highlight different perspectives.

## Actionable Takeaways
What should a CISO, SOC team, or security leader do next. Practical, implementable recommendations."""

# SSL context to avoid certificate issues
ssl_ctx = ssl.create_default_context()
ssl_ctx.check_hostname = False
ssl_ctx.verify_mode = ssl.CERT_NONE


def extract_video_id(url):
    """Extract video ID from YouTube URL."""
    match = re.search(r'[?&]v=([a-zA-Z0-9_-]{11})', url)
    return match.group(1) if match else None


def fetch_video_metadata(video_id):
    """Fetch video title, channel, and date from YouTube page."""
    url = f"https://www.youtube.com/watch?v={video_id}"
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cookie': 'CONSENT=YES+1'
    })
    try:
        resp = urllib.request.urlopen(req, context=ssl_ctx, timeout=15)
        html = resp.read().decode('utf-8', errors='ignore')

        # Extract title
        title_match = re.search(r'"title":"([^"]+)"', html)
        title = title_match.group(1) if title_match else f"Video {video_id}"

        # Extract channel name
        channel_match = re.search(r'"ownerChannelName":"([^"]+)"', html)
        channel = channel_match.group(1) if channel_match else "Unknown Channel"

        # Extract publish date
        date_match = re.search(r'"publishDate":"([^"]+)"', html)
        pub_date = date_match.group(1) if date_match else datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")

        return {
            'title': title.replace('\\u0026', '&').replace('\\u0027', "'"),
            'channel': channel,
            'published': pub_date,
        }
    except Exception as e:
        print(f"  Warning: Could not fetch metadata for {video_id}: {e}")
        return {
            'title': f"Video {video_id}",
            'channel': "Unknown Channel",
            'published': datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
        }


def fetch_transcript(video_url):
    """Fetch transcript from Supadata API."""
    params = urllib.parse.urlencode({
        'url': video_url,
        'lang': 'en',
        'text': 'true'
    })
    url = f"https://api.supadata.ai/v1/transcript?{params}"
    req = urllib.request.Request(url, headers={
        'x-api-key': SUPADATA_API_KEY,
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
    })
    try:
        resp = urllib.request.urlopen(req, context=ssl_ctx, timeout=60)
        data = json.loads(resp.read().decode('utf-8'))
        return data.get('content', '')
    except Exception as e:
        print(f"  Error fetching transcript: {e}")
        return None


def summarize_with_llm(title, channel, published, transcript):
    """Send transcript to OpenRouter for summarization."""
    # Truncate if too long
    if len(transcript) > 150000:
        transcript = transcript[:150000] + "\n\n[Transcript truncated due to length]"

    user_prompt = f"""Please create a structured summary of this cybersecurity podcast episode.

**Episode Title:** {title}
**Channel:** {channel}
**Published:** {published}

**Full Transcript:**
{transcript}"""

    body = json.dumps({
        "model": OPENROUTER_MODEL,
        "max_tokens": 8000,
        "temperature": 0.3,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt}
        ]
    }).encode('utf-8')

    req = urllib.request.Request(
        "https://openrouter.ai/api/v1/chat/completions",
        data=body,
        headers={
            'Authorization': f'Bearer {OPENROUTER_API_KEY}',
            'Content-Type': 'application/json',
            'HTTP-Referer': 'https://ekaraops.github.io/threatintelpod/',
            'X-Title': 'ThreatIntelPod'
        },
        method='POST'
    )
    try:
        resp = urllib.request.urlopen(req, context=ssl_ctx, timeout=120)
        data = json.loads(resp.read().decode('utf-8'))
        return data.get('choices', [{}])[0].get('message', {}).get('content', 'Summary generation failed.')
    except Exception as e:
        print(f"  Error from LLM: {e}")
        return None


def make_slug(text):
    """Convert text to URL-friendly slug."""
    slug = text.lower()
    slug = re.sub(r'[^a-z0-9]+', '-', slug)
    slug = slug.strip('-')
    return slug[:60]


def make_channel_slug(channel):
    """Make a channel slug."""
    return make_slug(channel)


def push_to_github(file_path, content, commit_message):
    """Push a file to GitHub via the Contents API."""
    b64_content = base64.b64encode(content.encode('utf-8')).decode('utf-8')
    url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{file_path}"

    body = json.dumps({
        "message": commit_message,
        "content": b64_content,
        "branch": "main"
    }).encode('utf-8')

    req = urllib.request.Request(
        url,
        data=body,
        headers={
            'Authorization': f'Bearer {GITHUB_PAT}',
            'Accept': 'application/vnd.github+json',
            'Content-Type': 'application/json'
        },
        method='PUT'
    )
    try:
        resp = urllib.request.urlopen(req, context=ssl_ctx, timeout=30)
        return True
    except urllib.error.HTTPError as e:
        error_body = e.read().decode('utf-8')
        if '"sha"' in error_body:
            print(f"  File already exists, skipping: {file_path}")
            return True  # Already published
        print(f"  GitHub error: {e.code} - {error_body[:200]}")
        return False
    except Exception as e:
        print(f"  GitHub error: {e}")
        return False


def process_video(video_url, index, total):
    """Process a single video: metadata -> transcript -> summary -> publish."""
    video_id = extract_video_id(video_url)
    if not video_id:
        print(f"[{index}/{total}] Invalid URL: {video_url}")
        return False

    print(f"\n[{index}/{total}] Processing: {video_id}")
    print(f"  URL: {video_url}")

    # Step 1: Get metadata
    print("  Fetching metadata from YouTube...")
    meta = fetch_video_metadata(video_id)
    print(f"  Title: {meta['title']}")
    print(f"  Channel: {meta['channel']}")
    print(f"  Published: {meta['published']}")

    # Step 2: Get transcript
    print("  Fetching transcript from Supadata...")
    transcript = fetch_transcript(video_url)
    if not transcript or len(transcript) < 100:
        print("  SKIP: No transcript available")
        return False
    print(f"  Transcript length: {len(transcript)} chars")

    # Step 3: Summarize
    print("  Generating AI summary (this takes 30-90 seconds)...")
    summary = summarize_with_llm(meta['title'], meta['channel'], meta['published'], transcript)
    if not summary:
        print("  SKIP: Summary generation failed")
        return False
    print(f"  Summary length: {len(summary)} chars")

    # Step 4: Create markdown
    channel_slug = make_channel_slug(meta['channel'])
    title_slug = make_slug(meta['title'])
    pub_date = meta['published'][:10]  # YYYY-MM-DD
    filename = f"{pub_date}-{channel_slug}-{title_slug}.md"
    file_path = f"content/episodes/{filename}"

    # Escape quotes in title for YAML
    safe_title = meta['title'].replace('"', '\\"')
    category = "cybersecurity"

    markdown = f"""---
title: "{safe_title}"
date: {meta['published']}
draft: false
channel: "{meta['channel']}"
channel_slug: "{channel_slug}"
category: "{category}"
youtube_url: "{video_url}"
video_id: "{video_id}"
thumbnail: "https://i.ytimg.com/vi/{video_id}/sddefault.jpg"
description: "AI-generated summary of {safe_title} from {meta['channel']}"
tags: ["{category}"]
---

{summary}
"""

    # Step 5: Push to GitHub
    print(f"  Pushing to GitHub: {file_path}")
    success = push_to_github(file_path, markdown, f"Add summary: {filename}")
    if success:
        print(f"  Published successfully!")
    return success


def main():
    print("=" * 60)
    print("ThreatIntelPod - Bulk Video Summarizer")
    print("=" * 60)

    if SUPADATA_API_KEY == "YOUR_SUPADATA_API_KEY":
        print("\nERROR: Please set your SUPADATA_API_KEY in the script")
        return
    if GITHUB_PAT == "YOUR_GITHUB_PAT":
        print("\nERROR: Please set your GITHUB_PAT in the script")
        return

    total = len(VIDEOS)
    success_count = 0
    fail_count = 0

    for i, url in enumerate(VIDEOS, 1):
        try:
            if process_video(url, i, total):
                success_count += 1
            else:
                fail_count += 1
        except Exception as e:
            print(f"  UNEXPECTED ERROR: {e}")
            fail_count += 1

        # Rate limit pause between videos
        if i < total:
            print("  Waiting 5 seconds before next video...")
            time.sleep(5)

    print("\n" + "=" * 60)
    print(f"DONE! Published: {success_count}, Failed: {fail_count}")
    print(f"Check your site: https://ekaraops.github.io/threatintelpod/")
    print("=" * 60)


if __name__ == "__main__":
    main()
