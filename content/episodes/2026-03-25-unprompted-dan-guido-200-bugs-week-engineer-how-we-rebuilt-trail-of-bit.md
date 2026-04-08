---
title: "Dan Guido - 200 Bugs/Week/Engineer: How We Rebuilt Trail of Bits Around AI | [un]prompted 2026"
date: 2026-03-25T06:21:42-07:00
draft: false
channel: "unprompted"
channel_slug: "unprompted"
category: "cybersecurity"
youtube_url: "https://www.youtube.com/watch?v=kgwvAyF7qsA"
video_id: "kgwvAyF7qsA"
thumbnail: "https://i.ytimg.com/vi/kgwvAyF7qsA/sddefault.jpg"
description: "AI-generated summary of Dan Guido - 200 Bugs/Week/Engineer: How We Rebuilt Trail of Bits Around AI | [un]prompted 2026 from unprompted"
tags: ["cybersecurity"]
hook: "When engineers went from 15 to 200 bugs per week, the traditional consulting business model died."
stings:
  - "The psychological war against AI-native workflows"
  - "Encoding senior expertise into autonomous agents"
  - "Scaling security without the human bottleneck"
card_topic: "AI+Security+Evolution"
topic_count: 6
threats: ["Supply Chain Attacks", "Prompt Injection", "Malicious Code"]
industries: ["Cybersecurity", "Software Development"]
speakers: "Dan Guido"
---

# Podcast Summary: How Trail of Bits Rebuilt Around AI

## TL;DR (Too Long, Didn't Read)
*   **AI-Native vs. AI-Assisted:** Most companies are merely "AI-assisted" (using tools like ChatGPT to do the same tasks faster), while "AI-native" companies redesign their entire workflow around AI as a teammate.
*   **The Human Barrier:** The biggest obstacle to AI adoption is not the technology, but human psychology (identity threats, bias, and intolerance for error).
*   **Compounding Expertise:** Trail of Bits encodes senior engineer expertise into "skills" (reusable AI workflows), allowing expertise to scale and compound across the company.
*   **Massive Productivity Gains:** By using specialized AI agents, the firm has seen bug discovery rates jump from 15 bugs/week to 200 bugs/week per engineer.
*   **Security-First AI:** To prevent "AI slop" or malicious code, the company uses curated marketplaces, sandboxing, and strict package cooldown policies.
*   **Business Model Shift:** As AI increases output by 200x, the traditional "billing by the hour" model for consulting will likely fail, shifting toward "billing by expertise/results."

## New Tools, Techniques, and Tactics
*   **Claude Code:** The primary AI coding agent used as the standard enterprise tool for the firm.
*   **Skills:** Reusable, structured workflows (including examples and constraints) that encode domain expertise for AI agents to execute.
*   **MCP (Model Context Protocol) Servers:** Used to turn internal security tools (like Slither) into interfaces that AI agents can use reliably.
*   **AI Maturity Matrix:** A framework used to grade employees on their AI integration, moving from "Level 0" (no use) to "Level 3" (inventing new AI tools).
*   **Package Cooldown Policy:** A security tactic where no software package can be installed unless it is at least 7 days old, reducing the risk of malicious "day-zero" updates.
*   **Sandboxing Options:** Multiple environments (Dev Containers, Digital Ocean VMs, macOS sandboxing) to allow agents to run code safely.

## Detection & Defense Insights
*   **Safe Supply Chain:** Use a "curated marketplace" for AI plugins and skills to prevent employees from downloading unverified or malicious "AI slop."
*   **Agent Guardrails:** Implementing "bypass permissions mode" in hackathons to force engineers to build better sandboxing and guardrails.
*   **Prompt Injection Defense:** Currently managed by denying web access to agents for sensitive client work or using "agent-native shells" (like Agent.sh) for kernel-level protection.
*   **MDM Enforcement:** Using Mobile Device Management (MDM) to enforce security policies, such as the mandatory package cooldown.
*   **Verification Workflows:** Using AI to check for false positives in other AI-discovered bugs to increase trust in the output.

## Real-World Examples & Stories
*   **The Resistance:** When Dan Guido first launched the AI initiative, 95% of the company was against it, and 25% were actively resisting.
*   **The Cooking Study:** A reference to a Stanford study showing that experts reject tools if they are framed as "replacing" them rather than "helping" them.
*   **Bug Hunting Results:** A specific case where an auditor running a fleet of specialized agents found 200 bugs per week instead of the usual 15.
*   **Sales Performance:** The sales team's revenue per representative doubled to $8 million by using AI for lead enrichment and proposal drafting.

## Research, References & Resources
*   **The Solo Paradox:** An economic concept from the 1980s (Robert Solow) describing how technology exists everywhere except in productivity statistics.
*   **Claude Code:** The specific AI tool used for the company's technical workflows.
*   **Slither:** A static analyzer for Ethereum smart contracts mentioned as an MCP integration.
*   **Stripe's "Minions" Paper:** A reference for using a central MCP server to enforce policy across all agents.
*   **Trail of Bits Open Source:** The speaker mentioned releasing their AI handbook, skills repos, and Jamf configuration stacks to the public.

## Key Industry Insights & Trends
*   **The Death of Hourly Billing:** In an AI-driven world, human output can increase 200x, making time-based billing obsolete for high-end consulting.
*   **Identity Upgrades:** Successful AI adoption requires reframing AI from a "replacement" to an "identity upgrade" (e.g., an auditor becomes a "commander of agents").
*   **The "Obelisk" Shape of Consulting:** Traditional firms have many juniors; AI-native firms will likely focus on senior talent who can leverage massive AI-driven scale.
*   **Shift to Results-Based Value:** Value in professional services is moving from "how long it took" to "the expertise and results delivered."

## Business & Risk Implications
*   **Operational Risk:** AI agents can accidentally delete work or pull in malicious dependencies; this requires heavy investment in sandboxing.
*   **Reputational Risk:** If an AI makes one embarrassing error, human trust in the system can be lost for months.
*   **Financial Risk:** Companies that fail to move from "AI-assisted" to "AI-native" risk becoming irrelevant as competitors' costs and speeds drop.
*   **Talent Risk:** Organizations must manage the "passive 50%"—employees who don't resist but don't adopt—through visible leadership and performance metrics.

## Opinions vs Facts
*   **Fact:** Trail of Bits has seen a massive increase in bug discovery and sales revenue through AI integration.
*   **Fact:** The company uses a curated marketplace and package cooldown to secure their AI workflows.
*   **Opinion:** The traditional consulting billing model (hourly) will likely change in the next 6–12 months.
*   **Opinion/Prediction:** Local AI models currently lack the "intelligence" of large cloud models (the "big model smell").
*   **Opinion:** The biggest challenge in AI adoption is psychological/human, not technical.

## Contradictions & Debates (if any)
*   **Local vs. Cloud Inference:** There is an ongoing debate/struggle between the need for privacy (local models) and the superior performance of large cloud-based models.
*   **Automation vs. Expertise:** There is a tension between giving agents autonomy to move fast and the need for strict human-led policy enforcement.

## Actionable Takeaways
*   **For CISOs:** Don't just buy ChatGPT licenses; redesign your workflows. Implement a "curated marketplace" for AI tools to prevent shadow AI.
*   **For SOC Teams:** Look for ways to turn manual investigation steps into "skills" (reusable AI workflows) to prevent knowledge loss when seniors leave.
*   **For Security Leaders:** Frame AI adoption as a way to make your experts "more dangerous" rather than a way to replace them.
*   **For Engineering Managers:** Use "Hackathons" instead of "Mandates" to encourage experimentation without triggering resistance.
*   **For All Leaders:** Ensure the "first experience" with AI is fast and successful; one bad error can destroy company-wide adoption.
