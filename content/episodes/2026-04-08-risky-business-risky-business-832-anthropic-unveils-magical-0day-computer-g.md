---
title: "Risky Business (832): Anthropic unveils magical 0day computer God"
date: 2026-04-08T05:14:36.000Z
draft: false
channel: "Risky Business"
channel_slug: "risky-business"
category: "news"
youtube_url: "https://www.youtube.com/watch?v=wXMrST1GjUk"
video_id: "wXMrST1GjUk"
thumbnail: "https://i.ytimg.com/vi/wXMrST1GjUk/sddefault.jpg"
description: "AI-generated summary of Risky Business (832): Anthropic unveils magical 0day computer God from Risky Business"
tags: ["news"]
hook: "The era of the human researcher is dying as AI gods begin hunting for zero-days."
stings:
  - "A machine that thinks in exploits"
  - "The long game of North Korean trust"
  - "When your code must be rewritten for the machine"
card_topic: "AI+Exploitation"
topic_count: 6
threats: ["AI-driven vulnerability discovery","Advanced social engineering","Supply chain compromise","Hardware-level bit flipping"]
industries: ["Software Development","Finance","Healthcare"]
speakers: "Patrick Gray"
---

## TL;DR (Too Long, Didn't Read)
* Anthropic's new "Mythos" model is a powerful AI specifically designed to find and exploit software vulnerabilities, potentially matching high-end human researchers.
* North Korean threat actors are using sophisticated, long-term social engineering (weeks or months of rapport building) to compromise supply chains and DeFi platforms.
* AI is shifting the software engineering paradigm; developers may soon need to refactor codebases to be "AI-friendly" for better automated security testing.
* Critical vulnerabilities are being exploited in widely used software like F5, Cisco, and Progress ShareFile, highlighting ongoing vendor risks.
* Identity verification (KYC) is moving into the enterprise to combat "identity swapping" where remote workers or contractors change mid-employment.
* The cybersecurity landscape is entering a "bonkers" era of rapid change, comparable to the transition to the internet in the early 2000s.

## New Tools, Techniques, and Tactics
* **Mythos (Anthropic):** An LLM model optimized for reasoning about code, finding bugs, and writing exploits.
* **Project Glass Wing:** Anthropic's initiative to give major vendors (Microsoft, Apple, CrowdStrike) early preview access to Mythos to find bugs before attackers do.
* **Advanced Social Engineering:** North Korean actors are building fake Slack workspaces and attending real-world conferences to build months of trust before attacking.
* **TestFlight Malware Deployment:** Using Apple's TestFlight to distribute malicious apps to victims under the guise of beta testing.
* **VS Code "Trust" Exploits:** Using malicious scripts in repositories that execute automatically the moment a developer opens the directory in VS Code.
* **Rowhammer on GPUs:** A technique to flip bits in NVIDIA GPU memory to escalate privileges or degrade AI model performance.

## Detection & Defense Insights
* **AI-Friendly Codebases:** Organizations should consider refactoring code into more structured, "monorepo-style" formats to allow AI agents to reason across the entire suite.
* **Identity Re-verification:** Implement periodic identity checks (not just at onboarding) to ensure the person performing sensitive tasks is the same person hired.
* **DNS Monitoring:** Watch for unauthorized changes to DNS settings, especially in home/small office routers, which can lead to credential theft via fake login pages.
* **Mitigating "Clickfix" Attacks:** Educate users that "emergency updates" requested during a failed meeting or software error are high-risk social engineering tactics.
* **GPU Security:** Be aware that hardware-level attacks like Rowhammer can bypass traditional software-based memory protections (like IOMMU).

## Real-World Examples & Stories
* **Axius Supply Chain Attack:** North Korean actors spent weeks building rapport via a fake Slack workspace to trick a maintainer into installing a malicious "updater."
* **Drift DeFi Hack:** North Koreans spent months attending conferences and investing real money to build trust with a DeFi platform before stealing $280 million.
* **Progress ShareFile Bug:** A "throwback" bug where an admin page redirected users but still rendered the underlying form, allowing for remote code execution.
* **Massachusetts Hospital Incident:** A hospital had to turn away ambulances during a cyberattack, highlighting the life-safety risks of healthcare breaches.
* **Telegard Encryption Failure:** A secure chat app that "defeated" its own encryption by sending private keys to a centralized server during signup.

## Research, References & Resources
* **Anthropic Blog:** Details on the Mythos model and its capabilities in vulnerability discovery.
* **CISA Warnings:** Urgent notices regarding TrueConf (teleconferencing) vulnerabilities being exploited by Chinese intelligence.
* **NCSC Reports:** Research regarding Russian military intelligence targeting residential routers (TP-Link, etc.).
* **Lazarus Heist Podcast:** A deep dive into the ecosystem of North Korean fake IT workers.
* **Trail of Bits:** Security researchers who analyzed the flaws in the Telegard messaging app.

## Key Industry Insights & Trends
* **The End of "Stable Equilibrium":** The industry is moving from a period of relative stability into a chaotic era driven by AI-driven exploit generation.
* **The "Human Touch" Irrelevance:** Unlike art, exploit development does not require "soul" or "suffering," making it a prime target for total AI replacement.
* **Shift in Vulnerability Research:** The role of human researchers may shift from finding bugs to managing AI tools that find bugs.
* **Identity as a Continuous Process:** Identity verification is moving from a "one-time event" (onboarding) to a continuous security signal.
* **Attacker Persistence:** State-sponsored actors (North Korea) are showing a massive increase in patience, willing to spend months on a single target.

## Business & Risk Implications
* **Operational Risk:** AI-driven bug discovery could lead to a "mini-catastrophe" every time a major software model is updated or a patch is released.
* **Reputational Risk:** Vendors who fail to adopt AI-driven testing (like Fortinet or Cisco) may struggle to keep up with the speed of automated discovery.
* **Financial Risk:** Large-scale DeFi and supply chain attacks demonstrate that even highly trusted entities can lose hundreds of millions in a single event.
* **Workforce Risk:** Remote work increases the risk of "identity fraud," where the person hired is not the person actually performing the work.

## Opinions vs Facts
* **Fact:** Anthropic has released a preview of the Mythos model to select vendors.
* **Fact:** North Korean actors used social engineering to compromise the Axius supply chain.
* **Opinion:** The job of a vulnerability researcher will eventually become "leveraging models to find bugs that aren't one-shotable."
* **Opinion/Speculation:** The "Ghost Murmur" device mentioned by Trump may be real or may be CIA disinformation.
* **Prediction:** The cybersecurity industry will become "utterly bonkers" due to the rapid advancement of AI.

## Contradictions & Debates (if any)
* **The "AI-Ready" Debate:** There is a debate on whether developers should move toward monorepos to help AI reasoning, which contradicts the traditional human-centric preference for smaller, separated repos.
* **Security vs. Usability:** A constant tension in the industry regarding how much "friction" (like identity checks) is acceptable before it breaks business workflows.
* **Defensive Effectiveness:** There is a debate on whether recent decreases in major outages are due to better attacker tools or better, more "playbooked" defender responses.

## Actionable Takeaways
* **CISO:** Evaluate your organization's identity verification processes; move beyond simple passwords to include periodic biometric or device-based re-verification.
* **SOC Team:** Update detection playbooks to include signals of "identity swapping" and monitor for unusual patterns in administrative actions (e.g., mass device wipes).
* **Security Leader:** Begin exploring how AI-driven testing can be integrated into your SDLC (Software Development Life Cycle) to stay ahead of automated attackers.
* **Engineering Manager:** Consider how your codebase structure affects automated security tools; aim for consistency to make your code "machine-readable."
* **All Teams:** Maintain high skepticism toward "emergency" software updates or "fixes" requested during unexpected technical glitches in meetings.
