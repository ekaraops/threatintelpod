---
title: "#279 - AI Readiness (with JP Bourget)"
date: 2026-04-12T12:31:05.000Z
draft: false
channel: "CISO Tradecraft"
channel_slug: "ciso-tradecraft"
category: "leadership"
youtube_url: "https://www.youtube.com/watch?v=nstCSJYWl_I"
video_id: "nstCSJYWl_I"
thumbnail: "https://i.ytimg.com/vi/nstCSJYWl_I/sddefault.jpg"
description: "AI-generated summary of #279 - AI Readiness (with JP Bourget) from CISO Tradecraft"
tags: ["leadership"]
hook: "Your company's data is a ticking time bomb waiting for an AI agent to trigger it."
stings:
  - "The nightmare of commingled data"
  - "Identity theft by autonomous agents"
  - "The high cost of 'free' intelligence"
card_topic: "AI + Governance"
topic_count: 6
threats: ["Data Leakage","Agentic Identity Hijacking","Insider Risk"]
industries: ["Enterprise IT","Data Management"]
speakers: "JP Bourget"
---

## TL;DR (Too Long, Didn't Read)
* **AI Readiness is Data Governance:** True readiness isn't just about having AI; it is about having clean, structured, and properly labeled data.
* **The Three Pillars:** Effective AI readiness requires excellence in threat protection, data security, and device management.
* **Data Architecture is Key:** Organizations must move away from "commingled" data (mixing different sensitivity levels in one folder) toward role-based, structured repositories.
* **Identity is the New Perimeter:** As "agentic" AI (AI that can act on its own) grows, managing the identities of these digital agents will be a major security challenge.
* **Change Management > Technical Setup:** Simply buying licenses won't work; organizations must focus on training and finding specific business use cases to see ROI.
* **Paid vs. Free AI:** Always use paid enterprise versions of AI tools to ensure data isn't used to train public models.

## New Tools, Techniques, and Tactics
* **Agentic Systems/Identity:** AI "agents" that can perform tasks and spawn sub-agents, requiring a new way to manage their digital identities.
* **DSPM (Data Security Posture Management):** Tools used to audit prompts and identify if sensitive information is being shared with LLMs.
* **RBAC (Role-Based Access Control) for Data:** Re-architecting file structures (like SharePoint) so that permissions are tied to specific business roles.
* **Personal AI Infrastructure (PAI):** A concept (from Daniel Miessler) of building a personalized AI system that understands an individual's context, goals, and memory.
* **Telos Framework:** A method for documenting personal purpose, goals, and challenges so an AI agent can better assist a specific user.

## Detection & Defense Insights
* **Data Labeling & Sensitivity:** Using tools like Microsoft Purview to apply labels to data so AI respects privacy boundaries.
* **Insider Risk Monitoring:** Watching for unusual behavior, such as a user accessing a high volume of files they have permission for but don't normally use.
* **Prompt Auditing:** Monitoring what users are typing into LLMs to prevent the leakage of sensitive corporate data.
* **Zero-Based Access Review:** Periodically cleaning up permissions (e.g., removing temporary access) to ensure AI doesn't accidentally grant "over-privileged" access.
* **Agentic Identity Management:** Developing ways to issue short-lived, secure identities (similar to Kubernetes certificates) for AI agents.

## Real-World Examples & Stories
* **The "Commingled Data" Nightmare:** A common scenario where a single SharePoint site contains everything from HR payroll to public party invites, making AI security impossible.
* **The "Bobby the Intern" Test:** A way to test AI security—if an intern asks an AI for quarterly financials, the AI should refuse because the intern lacks the underlying permissions.
* **The "Drug Dealer" Analogy:** A warning that AI services may start very cheap to get users "hooked," only to raise prices significantly once they become essential.
* **The "Chiropractor" Example:** A story about a professional using a free Gmail account, highlighting how personal accounts lack the protections of paid workspace accounts.

## Research, References & Resources
* **Daniel Miessler:** A researcher/writer mentioned for his work on personal AI and the "Telos" framework.
* **Microsoft Purview:** A tool discussed for data labeling, governance, and compliance.
* **Claude (Anthropic) & GPT (OpenAI):** Mentioned as the primary LLMs being integrated into enterprise workflows.
* **SaltCon:** A cybersecurity event mentioned as a place for practitioners to connect.

## Key Industry Insights & Trends
* **Shift from UI to API:** In the future, security products may be designed for AI agents to "consume" via API rather than for humans to click through a User Interface (UI).
* **The End of "Cheap" AI:** The era of nearly free AI development may be ending due to high energy costs, GPU shortages, and the need for companies to become profitable.
* **Agentic Economy:** A prediction that AI agents may eventually transact with each other using digital currencies (like crypto or stablecoins) rather than fiat money.
* **Tectonic Human Shift:** The transition from information workers to AI-augmented workers is viewed as a shift as large as the Industrial Revolution.

## Business & Risk Implications
* **Operational Risk:** Poor data architecture leads to "hallucinations" and the accidental exposure of sensitive data through AI.
* **Financial Risk:** Uncontrolled AI usage (especially via APIs) can lead to massive, unexpected "token bills" if throttles are not in place.
* **Reputational Risk:** Using free AI models can lead to corporate secrets being absorbed into public training sets.
* **Adoption Risk:** Organizations risk wasting money on expensive AI licenses if they fail to provide training and clear business use cases.

## Opinions vs Facts
* **Fact:** Microsoft Copilot honors existing SharePoint permissions and sensitivity labels.
* **Fact:** Using free versions of LLMs generally means your data can be used for training.
* **Opinion:** AI agents may eventually prefer transacting in cryptocurrency rather than fiat.
* **Opinion/Prediction:** The future of security products will be driven by API speed and quality rather than human-friendly interfaces.
* **Opinion:** We are approaching a "tectonic shift" in humanity comparable to the Industrial Revolution.

## Contradictions & Debates (if any)
* **The Value of UI:** While most current software focuses on User Interface (UI), there is a debate about whether the future of software is actually "UI-less" and built for agents.
* **AI Training Data:** There is a discussion regarding whether providing "feedback" (thumbs up/down) to an AI model constitutes submitting your reasoning/data for training.

## Actionable Takeaways
* **CISO:** Prioritize data governance and "cleaning the house" (data labeling and architecture) before a wide-scale AI rollout.
* **SOC Team:** Implement monitoring for "insider risk" specifically related to AI prompt patterns and unusual data access.
* **Security Leaders:** Move away from "dumping" AI tools on employees; instead, create "Lunch and Learns" and document high-value use cases.
* **IT/DevOps:** Set strict API usage limits and "throttles" on all AI tools to prevent runaway costs.
* **All Leaders:** Ensure the organization is using **paid enterprise versions** of all AI tools to protect corporate intellectual property.
