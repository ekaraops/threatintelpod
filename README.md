# ThreatIntelPod

AI-powered cybersecurity podcast summaries for CISOs, SOC teams, and security leaders.

## What This Does

ThreatIntelPod automatically:
1. Monitors YouTube cybersecurity channels and playlists for new episodes (weekly)
2. Sends you a Slack message for each new episode to approve or skip
3. Fetches the transcript of approved episodes
4. Uses AI to generate a structured summary with actionable takeaways
5. Publishes the summary to your website automatically

## Architecture

```
YouTube RSS Feeds --> n8n (weekly scan) --> Slack Approval
                                              |
                                     [You click Approve]
                                              |
                         Supadata API (transcript) --> OpenRouter (AI summary)
                                                          |
                                              Push to GitHub --> GitHub Pages
```

---

## Setup Guide (Step by Step)

### Prerequisites

You will need accounts (free or paid) on these services:
- **GitHub** (free) - hosts your website
- **n8n** (cloud or self-hosted) - runs the automation
- **Supadata** (paid, usage-based) - fetches YouTube transcripts
- **OpenRouter** (paid, usage-based) - AI summarization
- **Slack** (free) - approval notifications

---

### Step 1: Create the GitHub Repository

1. Go to [github.com](https://github.com) and sign in
2. Click the **+** button in the top right corner, then **New repository**
3. Name it `threatintelpod`
4. Set it to **Public** (required for free GitHub Pages)
5. Do NOT check "Add a README file" (we already have one)
6. Click **Create repository**

#### Upload the project files

**Option A: Using GitHub's web interface (easiest)**
1. On your new empty repo page, click **"uploading an existing file"**
2. Drag and drop the entire contents of the `threatintelpod/` folder
3. Click **Commit changes**

**Option B: Using the command line**
```bash
cd threatintelpod
git init
git add .
git commit -m "Initial ThreatIntelPod setup"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/threatintelpod.git
git push -u origin main
```

#### Enable GitHub Pages
1. Go to your repo's **Settings** tab
2. Click **Pages** in the left sidebar
3. Under **Source**, select **GitHub Actions**
4. The site will deploy automatically on the next push

Your site will be live at: `https://YOUR_USERNAME.github.io/threatintelpod/`

---

### Step 2: Create a GitHub Personal Access Token

The n8n workflow needs a token to push summary files to your repo.

1. Go to [github.com/settings/tokens?type=beta](https://github.com/settings/tokens?type=beta)
2. Click **Generate new token**
3. Name it `threatintelpod-n8n`
4. Set expiration to **90 days** (you'll need to renew it)
5. Under **Repository access**, select **Only select repositories** and pick `threatintelpod`
6. Under **Permissions > Repository permissions**, set **Contents** to **Read and write**
7. Click **Generate token**
8. **Copy the token immediately** - you won't see it again

Save this token somewhere safe. You'll enter it in n8n in Step 5.

---

### Step 3: Get Your API Keys

#### Supadata API Key
1. Go to [supadata.ai](https://supadata.ai) and sign up
2. Navigate to your dashboard / API keys section
3. Create a new API key
4. Copy and save it

#### OpenRouter API Key
1. Go to [openrouter.ai](https://openrouter.ai) and sign up
2. Go to **Keys** in your dashboard
3. Create a new API key
4. Copy and save it
5. Add credits to your account ($5-10 is enough to start)

---

### Step 4: Set Up Slack

You need a Slack channel for approval notifications.

1. In your Slack workspace, create a channel called `#threatintelpod-approvals`
2. In n8n (next step), you'll connect your Slack workspace when configuring the workflow

---

### Step 5: Import the n8n Workflow

1. Log into your n8n instance
2. Click **+ Add workflow** (or **New Workflow**)
3. Click the **...** menu in the top right, then **Import from file**
4. Select the file `n8n/workflow.json` from this project
5. The workflow will appear with all 14+ nodes

#### Configure Credentials

You need to set up 3 credentials in n8n:

**Slack:**
1. Click on the **"Slack: Approve Episode?"** node
2. Click on **Credential** and select **Create new**
3. Follow the OAuth flow to connect your Slack workspace
4. Set the channel to `#threatintelpod-approvals`

**Supadata API Key:**
1. Click on the **"Fetch Transcript (Supadata)"** node
2. In the Headers section, replace `YOUR_SUPADATA_API_KEY` with your actual API key

**OpenRouter API Key:**
1. Click on the **"Summarize with LLM"** node
2. In the Headers section, replace `YOUR_OPENROUTER_API_KEY` with your actual API key

**GitHub Token:**
1. Click on the **"Push to GitHub"** node
2. In the Headers section, replace `YOUR_GITHUB_PAT` with your GitHub personal access token
3. In the URL field, replace `YOUR_GITHUB_USERNAME` with your actual GitHub username

---

### Step 6: Update the Hugo Config

1. In your GitHub repo, edit `hugo.toml`
2. Replace `YOUR_GITHUB_USERNAME` in the `baseURL` with your actual GitHub username:
   ```
   baseURL = "https://YOUR_USERNAME.github.io/threatintelpod/"
   ```

---

### Step 7: Test the Workflow

1. In n8n, click the **Test workflow** button (play icon)
2. The workflow will:
   - Fetch RSS feeds from all configured channels
   - Find new videos
   - Send Slack messages for approval
3. Go to Slack and click **Summarize** on one of the messages
4. Watch n8n process the transcript and push to GitHub
5. Check your GitHub repo - a new file should appear in `content/episodes/`
6. Your website should rebuild and show the new episode within 2-3 minutes

---

### Step 8: Activate for Production

Once testing works:
1. In n8n, toggle the workflow to **Active** (the switch in the top right)
2. The workflow will now run automatically every Monday at 9:00 AM

---

## Managing Feeds

### Adding a New YouTube Channel

1. Find the channel's ID:
   - Go to the YouTube channel page
   - Open browser Developer Tools (F12)
   - In the Console, run: `document.querySelector('link[rel="canonical"]')?.href`
   - The channel ID is the `UC...` part after `/channel/`

2. In n8n, open the **"Load Feeds Config"** Code node

3. Add a new entry to the `feeds` array:
   ```javascript
   {
     name: 'Channel Name',
     slug: 'channel-name',
     type: 'channel',
     id: 'UCxxxxxxxxxxxxxxxxxxxxxxxxx',
     category: 'news',
     description: 'What this channel covers'
   }
   ```

4. Save the node and the workflow

### Adding a YouTube Playlist

Same as above, but use `type: 'playlist'` and the playlist ID (starts with `PL`):
```javascript
{
  name: 'My Playlist',
  slug: 'my-playlist',
  type: 'playlist',
  id: 'PLxxxxxxxxxxxxxxxxxxxxxxxxx',
  category: 'mixed',
  description: 'Curated playlist description'
}
```

### Removing a Feed

Delete the feed entry from the `feeds` array in the **"Load Feeds Config"** node.

---

## Customization

### Changing the Schedule

1. Click on the **"Weekly Monday 9AM"** Schedule Trigger node
2. Change `triggerAtDay` (0=Sunday, 1=Monday, ..., 6=Saturday)
3. Change `triggerAtHour` (0-23)

### Changing the AI Model

1. Click on the **"Summarize with LLM"** node
2. In the JSON body, change the `model` field
3. Available models: see [openrouter.ai/models](https://openrouter.ai/models)
4. Recommended: `anthropic/claude-sonnet-4-20250514` (good balance of quality and cost)

### Changing the Summary Prompt

1. Click on the **"Summarize with LLM"** node
2. Edit the `system` message content in the JSON body
3. Modify the sections, instructions, or format as needed

### Changing the Website Theme

Edit `assets/css/main.css` to change colors, fonts, or layout:
- `--accent-green`: Primary accent color
- `--accent-cyan`: Secondary accent color
- `--bg-primary`: Main background color
- `--bg-card`: Card background color

---

## Troubleshooting

### "Workflow execution failed" in n8n
- Check the specific node that failed (it will be highlighted in red)
- Click on the node to see the error message
- Common issues: expired API keys, rate limits, network timeouts

### Slack messages not appearing
- Verify the Slack credential is connected and authorized
- Check that the channel name matches exactly (including the `#`)
- Ensure the Slack app/bot has been invited to the channel

### Website not updating after push
- Go to your repo's **Actions** tab to check if the Hugo build succeeded
- If the build failed, click on the run to see the error log
- Common issue: YAML frontmatter syntax errors in the generated markdown

### Transcripts returning empty
- Some videos don't have captions/transcripts available
- The workflow will send a Slack notification when this happens
- Consider using Supadata's `mode=auto` parameter for AI-generated transcripts (costs more)

### "Rate limit exceeded" from Supadata
- The workflow includes a 3-second pause between transcript fetches
- If you still hit limits, increase the wait time in the **"Rate Limit Pause"** node

### Duplicate episodes appearing
- The workflow tracks seen videos using n8n's static data
- If static data is lost (rare on n8n cloud), previously seen videos may reappear for approval
- Simply click **Skip** on any duplicates

---

## Costs Estimate

| Service | Cost | Notes |
|---------|------|-------|
| GitHub Pages | Free | Public repos only |
| n8n Cloud | Free tier or ~$20/mo | Free tier has limited executions |
| Supadata | ~$0.001/transcript | Pay per use |
| OpenRouter (Claude) | ~$0.01-0.05/summary | Depends on transcript length |

**Estimated monthly cost for 10-20 episodes**: $1-5 for API calls + n8n hosting.

---

## Project Structure

```
threatintelpod/
├── .github/workflows/deploy-hugo.yml  - Auto-deploys site on push
├── assets/css/main.css                - Dark cybersecurity theme
├── content/
│   ├── about.md                       - About page
│   └── episodes/                      - Episode summaries (auto-generated)
│       ├── _index.md                  - Episodes list page config
│       └── *.md                       - Individual episode files
├── data/feeds.json                    - Reference copy of feed config
├── layouts/                           - Hugo templates
├── static/images/                     - Logo and favicon
├── n8n/workflow.json                  - Importable n8n workflow
├── hugo.toml                          - Hugo site configuration
└── README.md                          - This file
```

---

## License

MIT License. Summaries are AI-generated and may contain inaccuracies. Always refer to the original episodes for authoritative information.
