---
title: "Heather Adkins &  Four Flynn - Evaluating Threats & Automating Defense at Google | [un]prompted 2026"
date: 2026-03-25T06:23:50-07:00
draft: false
channel: "unprompted"
channel_slug: "unprompted"
category: "cybersecurity"
youtube_url: "https://www.youtube.com/watch?v=B_7RpP90rUk"
video_id: "B_7RpP90rUk"
thumbnail: "https://i.ytimg.com/vi/B_7RpP90rUk/sddefault.jpg"
description: "AI-generated summary of Heather Adkins &  Four Flynn - Evaluating Threats & Automating Defense at Google | [un]prompted 2026 from unprompted"
tags: ["cybersecurity"]
hook: "Google is training AI agents to hunt for bugs with the same relentless intuition as elite human researchers."
stings:
  - "The VAI Apocalypse looms"
  - "Autonomous patching loops"
  - "Zero-day speed at scale"
card_topic: "Agentic+Defense"
topic_count: 6
threats: ["Automated Exploit Generation", "Software Vulnerabilities", "AI-driven Hacking"]
industries: ["Software Development", "Cybersecurity", "Technology"]
---

# Podcast Summary: Evaluating Threats & Automating Defense at Google

## TL;DR (Too Long, Didn't Read)
* Google is developing AI agents to find and fix software vulnerabilities automatically to combat a "cataclysmic" increase in bugs.
* **Big Sleep** is an agentic system designed to find deep, complex memory safety bugs that traditional tools miss.
* **Code Mender** is a companion system that automatically generates, tests, and verifies patches for discovered bugs.
* The goal is to move from "finding bugs" to "eliminating every software vulnerability on Earth."
* The speakers warn of a "VAI Apocalypse," where open-source hacking frameworks make automated exploitation widespread.
* Current success includes 178 autonomous fixes in open-source libraries and hardening Google Chrome.

## New Tools, Techniques, and Tactics
* **Big Sleep:** An agentic reasoning system that mimics elite human researchers to find deep vulnerabilities.
* **Code Mender:** An automated patching engine that creates, verifies, and submits code fixes.
* **Agentic Reasoning Loops:** Instead of simple prompting, the AI uses a loop of hypothesis, testing, and revision.
* **Vibe Coding:** Mentioned as a framework for generating new "greenfield" code (which must be secure by design).
* **Automated Exploit Generation:** Big Sleep builds its own proof-of-concept exploits to ensure a bug is real (zero false positives).
* **Pluggable Verifiers:** A system using fuzzing, formal verification, and differential testing to check if a patch breaks code.

## Detection & Defense Insights
* **Beyond Fuzzing:** Big Sleep is successfully finding deep bugs that traditional fuzzers currently miss.
* **Zero False Positive Goal:** By requiring the AI to build a working exploit, the system ensures developers don't waste time on "AI slop."
* **Hardening vs. Patching:** Defense includes "hardening" (proactively fixing code structures like pointers) rather than just reacting to bugs.
* **Verification Signals:** Using debuggers, Python interpreters, and code browsers as "tools" for the AI to interact with the environment.
* **Developer Idioms:** Defense tools must write code that looks like it was written by the original human to ensure adoption.

## Real-World Examples & Stories
* **The RAND Study:** Referenced a 2017 study showing it takes experts ~22 days to exploit a deep bug; Google aims to do this in minutes.
* **NVD Backlog:** Mentioned the 30,000 unanalyzed vulnerability queue as evidence of the scale of the problem.
* **Open Source Success:** Code Mender has already autonomously generated 178 fixes for open-source libraries like `libwebp`.
* **Chrome Hardening:** Google has used these tools to proactively harden pointers within the Chrome codebase.
* **The "Researcher" Persona:** Described how AI agents now mimic the behavior of researchers "staring at a screen with coffee" to solve hard problems.

## Research, References & Resources
* **Project Zero:** Google’s elite team focused on zero-day vulnerabilities, whose expertise is being modeled by Big Sleep.
* **NVD (National Vulnerability Database):** Cited regarding the massive backlog of unanalyzed CVEs.
* **CVSS (Common Vulnerability Scoring System):** Suggested that this system may become obsolete due to the speed of AI exploitation.
* **Big Sleep Issue Tracker:** A public URL was mentioned where users can see the quality of AI-generated bug reports.

## Key Industry Insights & Trends
* **The Pivot of 2026:** The speakers predict 2026 will be remembered as the year cybersecurity became significantly more complex.
* **VAI Apocalypse:** The emerging trend of highly capable, open-source AI hacking tools available to everyone.
* **Vulnerability Explosion:** A 35% increase in logged CVEs between 2024 and 2025 indicates a growing attack surface.
* **Shift to Agentic Security:** Moving away from "chatting with LLMs" toward "autonomous agents" that use tools and reason through problems.
* **VC Investment:** Massive capital (billions) is flowing into AI-driven pentesting and vulnerability discovery startups.

## Business & Risk Implications
* **Operational Risk:** The speed of AI-driven exploitation means the window to patch is shrinking from weeks to minutes.
* **Reputational Risk:** For enterprises, the ability to "patch at the speed of AI" will become a competitive necessity.
* **Financial Impact:** The sheer volume of vulnerabilities will overwhelm traditional human-led SOC and engineering teams.
* **Scalability Challenges:** Companies must move toward automated "greenfield" security to avoid the massive cost of managing "brownfield" (legacy) debt.

## Opinions vs Facts
* **Fact:** There is a 30,000+ backlog in the NVD.
* **Fact:** Code Mender has produced 178 autonomous open-source fixes.
* **Opinion/Prediction:** 2026 will be the year "everything pivoted."
* **Opinion/Prediction:** We are not far from an "open-source full hacking tool" that can hack Google in a week.
* **Opinion/Prediction:** The CVSS scoring system will eventually become meaningless.

## Contradictions & Debates (if any)
* **Speed vs. Quality:** The speakers acknowledge a debate in the industry: Should AI tools be "quick to market" (faster) or "highly verified" (slower but more trusted)? Google has chosen the latter.
* **Business Logic vs. Infrastructure:** There is a debate/uncertainty regarding whether these tools work for "business logic" bugs versus "infrastructure" bugs (like memory safety).

## Actionable Takeaways
* **SOC Leaders:** Prepare for a massive increase in vulnerability volume; manual triage will no longer scale.
* **CISOs:** Evaluate the integration of agentic security tools into the SDLC (Software Development Life Cycle) to move from reactive to proactive defense.
* **Engineering Managers:** Focus on "secure by design" (greenfield) practices and adopting memory-safe frameworks to reduce the long-term patching burden.
* **Security Researchers:** Start exploring "agentic workflows" (using tools like debuggers and interpreters) rather than just prompt engineering.
