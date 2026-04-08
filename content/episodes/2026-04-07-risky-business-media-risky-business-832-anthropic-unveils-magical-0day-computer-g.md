---
title: "Risky Business (832): Anthropic unveils magical 0day computer God"
date: 2026-04-07T22:14:36-07:00
draft: false
channel: "Risky Business Media"
channel_slug: "risky-business-media"
category: "cybersecurity"
youtube_url: "https://www.youtube.com/watch?v=wXMrST1GjUk"
video_id: "wXMrST1GjUk"
thumbnail: "https://i.ytimg.com/vi/wXMrST1GjUk/sddefault.jpg"
description: "AI-generated summary of Risky Business (832): Anthropic unveils magical 0day computer God from Risky Business Media"
tags: ["cybersecurity"]
hook: "Anthropic's new Mythos model is so lethal at finding zero-days that they're keeping it under lock and key."
stings:
  - "AI-driven exploit generation"
  - "North Korean social engineering"
  - "The death of manual bug hunting"
card_topic: "AI + Vulnerabilities"
topic_count: 6
---

# Podcast Summary: Risky Business (832) - Anthropic's "Mythos" Model

## TL;DR (Too Long, Didn't Read)
* Anthropic has unveiled "Mythos," an AI model specifically designed for advanced code reasoning and vulnerability discovery.
* The model is so powerful at finding "zero-day" bugs that Anthropic is limiting its preview to major security and software vendors.
* Security researchers are debating whether AI will replace human bug hunters or simply change their job description to "AI orchestrators."
* North Korean threat actors are using highly sophisticated, long-term social engineering to compromise supply chains and DeFi platforms.
* There is a growing trend of "identity-as-a-service" to combat remote work risks, such as fake employees or identity theft during onboarding.
* Significant shifts in US cybersecurity policy (CISA budget cuts) are occurring simultaneously with increased threats from China and Iran.

## New Tools, Techniques, and Tactics
* **Mythos (Anthropic):** An LLM optimized for deep reasoning about code, capable of finding bugs and writing exploits at a human-expert level.
* **Project Glass Wing:** Anthropic’s initiative to give early preview access of Mythos to major vendors (e.g., Microsoft, Apple, CrowdStrike) to help them patch before public release.
* **TestFlight Malware Deployment:** North Korean actors are using Apple’s TestFlight (a beta testing tool) to distribute malicious apps to victims.
* **VS Code Script Injection:** Attackers are placing malicious scripts in repositories that execute automatically the moment a developer opens the folder in VS Code.
* **Rowhammer on GPUs:** New research shows attackers can use Rowhammer techniques to flip bits in NVIDIA GPU memory, leading to privilege escalation.

## Detection & Defense Insights
* **Codebase Refactoring for AI:** Developers may need to refactor code into "monorepos" or standardized structures to make them "AI-friendly" for automated auditing.
* **Identity Verification (KYC) in Enterprise:** Using tools like Persona to verify that a remote worker is the same person who was interviewed, preventing "identity swapping."
* **Continuous Re-authentication:** Moving beyond "day one" identity checks to periodic "low-friction" checks (like a quick selfie) during high-risk actions.
* **DNS Monitoring:** Detecting unauthorized changes to residential router DNS settings, a tactic used by Russian intelligence to redirect users to fake login pages.
* **Hardware-Level Defense:** The need for better protections against electromagnetic sensing and GPU-based memory attacks.

## Real-World Examples & Stories
* **The Axius Compromise:** North Korean actors spent weeks building rapport via a fake Slack workspace to trick a developer into installing a "meeting update" that was actually malware.
* **Drift DeFi Hack:** North Korean actors spent months attending conferences and investing real money to build trust with DeFi developers before stealing $280 million.
* **Telegard Encryption Failure:** A "secure" chat app was found to be sending private keys to its central server, making the end-to-end encryption effectively useless.
* **Massachusetts Hospital Attack:** A case study where a hospital had to turn away ambulances during a cyberattack, highlighting the life-safety risks of healthcare breaches.

## Research, References & Resources
* **Anthropic Blog:** Documentation on the Mythos model and its findings in open-source codebases.
* **CISA Warnings:** Recent alerts regarding the exploitation of "TrueConf" (teleconferencing software) by Chinese intelligence.
* **Trail of Bits:** Security researchers who analyzed the flaws in the Telegard messaging app.
* **Lazarus Heist Podcast:** A resource mentioned for deep-diving into the ecosystem of North Korean IT worker fraud.

## Key Industry Insights & Trends
* **The "AI Arms Race" in Bug Hunting:** The era of "stable security equilibrium" is ending; the speed of vulnerability discovery is about to accelerate massively.
* **Sophisticated Social Engineering:** Threat actors (specifically North Korea) are moving away from "spray and pray" to high-effort, multi-month psychological operations.
* **The Death of the "Human Touch" in Exploit Dev:** Unlike art, where human soul matters, exploit development is purely functional, making it highly susceptible to AI replacement.
* **Identity Fragmentation:** The difficulty of managing identity across HR, IT, and payroll systems creates massive gaps that attackers exploit.

## Business & Risk Implications
* **Operational Risk:** Rapid AI-driven bug discovery could lead to a "patching treadmill" where companies struggle to fix bugs faster than they are found.
* **Reputational & Financial Risk:** Large-scale DeFi hacks (like the $280M Drift incident) demonstrate the massive capital at risk from long-term social engineering.
* **Regulatory & Political Risk:** Budget cuts to agencies like CISA may leave enterprises with less government support and intelligence during active attacks.
* **Supply Chain Vulnerability:** The use of legitimate tools (Slack, TestFlight, VS Code) for attacks means traditional "perimeter" security is no longer sufficient.

## Opinions vs Facts
* **Fact:** Anthropic has released a model (Mythos) that is highly proficient at finding code vulnerabilities.
* **Fact:** North Korean actors have successfully used social engineering to compromise high-profile targets.
* **Opinion:** The job of a vulnerability researcher will shift toward managing AI agents rather than manual hunting.
* **Opinion/Speculation:** The "Ghost Murmur" device mentioned by Trump may be real or could be a piece of CIA disinformation.
* **Opinion:** The current US political climate is causing "self-inflicted wounds" to national cybersecurity via CISA budget cuts.

## Contradictions & Debates (if any)
* **AI vs. Human Researchers:** Some researchers argue AI will only find "one-shotable" bugs, while others believe it will fundamentally change the entire landscape of software security.
* **Security vs. Usability:** There is an ongoing debate in the industry about how much "friction" (like identity checks) an employee can tolerate before it hurts productivity.
* **The "Why" of Russian Hacking:** There is confusion among analysts regarding why Russian intelligence is focusing on low-level residential router hacks during a major war.

## Actionable Takeaways
* **For CISOs:** Evaluate your "identity plumbing." Ensure you have a way to verify that the person performing high-privilege actions (like wiping devices) is actually who they claim to be.
* **For SOC Teams:** Prepare for a higher volume of vulnerabilities. Shift focus from finding simple bugs to triaging the massive influx of findings that AI-driven tools will produce.
* **For Software Engineers:** Consider "AI-readiness" in your architecture. Standardizing code structures and maintaining clean documentation will make automated security auditing more effective.
* **For Security Leaders:** Increase training on "long-con" social engineering. Employees must be taught that rapport-building on Slack or LinkedIn is a common precursor to an attack.
