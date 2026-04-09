---
title: "Hunting Supply Chain Attacks with Jared Myers, Director, CrowdStrike OverWatch"
date: 2026-04-09T11:00:00.000Z
draft: false
channel: "CrowdStrike"
channel_slug: "crowdstrike"
category: "threat-intelligence"
youtube_url: "https://www.youtube.com/watch?v=08dNDcZgjVI"
video_id: "08dNDcZgjVI"
thumbnail: "https://i.ytimg.com/vi/08dNDcZgjVI/sddefault.jpg"
description: "AI-generated summary of Hunting Supply Chain Attacks with Jared Myers, Director, CrowdStrike OverWatch from CrowdStrike"
tags: ["threat-intelligence"]
hook: "Your most trusted software is becoming a Trojan horse for the world's most sophisticated actors."
stings:
  - "The silent injection of malicious code"
  - "Identity theft as the ultimate backdoor"
  - "The terrifying speed of AI-driven attacks"
card_topic: "Supply + Chain"
topic_count: 6
threats: ["Supply Chain Injection","Reflective Loading","Identity Theft","AI-Assisted Attacks"]
industries: ["Software Development","Cybersecurity"]
speakers: "Jared Myers"
---

## TL;DR (Too Long, Didn't Read)
*   Supply chain attacks are increasing in frequency and sophistication, often targeting developer accounts to inject malicious code into trusted libraries.
*   While zero-day exploits are the "doorway," threat hunters focus on the "tradecraft" (post-exploitation behavior) to catch attackers.
*   Identity is now a primary attack vector; attackers target developers to steal credentials, keys, and access to build supply chain attacks.
*   AI is expected to speed up the creation of attacks and vulnerabilities, though it may not fundamentally change the nature of the threat.
*   Effective defense requires "exponential" visibility by combining network, endpoint, cloud, and identity data.
*   A "quiet" environment can be a red flag; hunters must ensure a lack of activity isn't actually a lack of visibility.

## New Tools, Techniques, and Tactics
*   **Supply Chain Injection:** Loading malicious code into legitimate libraries using methods like git tags to hide changes.
*   **Three-Way Trojan:** A multi-platform attack (Windows, Mac, Linux) that uses staged decoys and post-install scripts to reach secondary Command and Control (C2) servers.
*   **Reflective Loading:** Loading malicious code (like .NET) directly into memory to avoid writing files to the disk, making it harder to detect.
*   **Binary Renaming:** Renaming malicious binaries (e.g., renaming a tool to look like a Windows Terminal) to blend in with legitimate system processes.
*   **Vibe Coding/AI-Assisted Attacks:** Using AI to rapidly generate code or find new vulnerabilities to speed up the attack lifecycle.

## Detection & Defense Insights
*   **Focus on Post-Exploitation:** Don't just hunt for the initial exploit; hunt for the "tradecraft" (lateral movement, persistence, and data staging) that follows.
*   **Identity Threat Hunting:** Move beyond looking for failed logins. Monitor for "impossible travel," unusual account behavior, and deviations from a user's normal activity patterns.
*   **Data Correlation:** Successful hunting requires combining endpoint, network, cloud, and identity logs to see the "bigger story."
*   **Developer Security:** Implement strict MFA and identity controls specifically for developer accounts and environments.
*   **Monitor Legitimate Processes:** Watch for legitimate system processes (like PowerShell or terminal tools) performing unusual actions like memory injection or directory enumeration.

## Real-World Examples & Stories
*   **Axios Incident:** A recent supply chain attack involving a package that used post-install scripts to perform reconnaissance and load malware into memory.
*   **MOVEit Vulnerability:** An example where the initial vulnerability (writing a web shell) might look common, but the follow-on data theft is what triggers a high-priority detection.
*   **The "Kitchen Fire" Analogy:** A reminder that while a major headline (like Axios) feels like a massive fire, security teams must continue fighting the "small fires" (daily intrusions) to remain effective.
*   **Overwatch's Global Scale:** The speaker shared that their team operates 24/7 across four global regions to ensure continuous coverage.

## Research, References & Resources
*   **CrowdStrike Overwatch:** The managed threat hunting service discussed throughout the episode.
*   **Stardust/North Korea:** Mentioned as a threat actor group involved in recent supply chain activities.
*   **Trivy/Axios:** Specific recent supply chain incidents used as case studies.

## Key Industry Insights & Trends
*   **Implied Trust Exploitation:** Attackers are moving away from "breaking in" and toward "being invited in" by compromising trusted third-party software.
*   **The Speed of AI:** AI is viewed as an accelerator for attackers, allowing them to find and exploit vulnerabilities much faster than before.
*   **Identity as the Perimeter:** Identity has shifted from a secondary concern to the main vector for gaining initial access.
*   **Shift in Attack Commodity:** Supply chain attacks, once rare and difficult to execute, are becoming more common and accessible to attackers.

## Business & Risk Implications
*   **Reputational Risk:** Supply chain attacks can impact a company's customers even if the company itself wasn't the primary target.
*   **Operational Disruption:** Responding to supply chain attacks requires rapid quarantine and credential rotation, which can disrupt business workflows.
*   **Complexity of Response:** Organizations must be prepared for "cascading" questions from leadership when a widely discussed vulnerability (like Axios) is disclosed.
*   **Third-Party Risk:** Heavy reliance on open-source and third-party packages creates a massive, often invisible, attack surface for the enterprise.

## Opinions vs Facts
*   **Fact:** Attackers are targeting developer accounts to facilitate supply chain attacks.
*   **Fact:** Overwatch uses a global, multi-region team to provide 24/7 coverage.
*   **Opinion:** AI will speed up attacks but won't fundamentally change the core nature of supply chain threats.
*   **Opinion/Prediction:** The "identity piece" will continue to be the most critical part of the attack lifecycle.
*   **Opinion:** A lack of alerts can sometimes be a sign of a visibility gap rather than a secure environment.

## Contradictions & Debates (if any)
*   **Zero-Day vs. Tradecraft:** There is a subtle debate on where to focus energy. While many chase the "zero-day" (the exploit), the speakers argue that hunting the "tradecraft" (the behavior after the exploit) is a more reliable way to catch sophisticated actors.

## Actionable Takeaways
*   **For CISOs:** Ensure your security strategy includes "Identity Threat Detection and Response" (ITDR), not just traditional endpoint security.
*   **For SOC Teams:** Don't get "tunnel vision" during major news events; continue monitoring for standard daily threats to avoid being distracted.
*   **For Security Leaders:** Audit your developer workflows. Ensure MFA is mandatory for all code repositories, package managers, and deployment tools.
*   **For Threat Hunters:** Prioritize the correlation of identity data with endpoint and network data to identify "living off the land" techniques.
*   **For All:** Review your third-party software inventory and understand the "implied trust" you have placed in your current software supply chain.
