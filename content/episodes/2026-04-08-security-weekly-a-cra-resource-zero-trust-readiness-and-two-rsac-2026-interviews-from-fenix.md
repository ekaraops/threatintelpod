---
title: "Zero Trust Readiness and Two RSAC 2026 Interviews from Fenix24 and Absolute Security - BSW #442"
date: 2026-04-08T02:00:48-07:00
draft: false
channel: "Security Weekly - A CRA Resource"
channel_slug: "security-weekly-a-cra-resource"
category: "cybersecurity"
youtube_url: "https://www.youtube.com/watch?v=d7zJ9OObOGY"
video_id: "d7zJ9OObOGY"
thumbnail: "https://i.ytimg.com/vi/d7zJ9OObOGY/sddefault.jpg"
description: "AI-generated summary of Zero Trust Readiness and Two RSAC 2026 Interviews from Fenix24 and Absolute Security - BSW #442 from Security Weekly - A CRA Resource"
tags: ["cybersecurity"]
hook: "Your AI agents are multiplying faster than your ability to secure them, creating a massive, unmanaged shadow attack surface."
stings:
  - "4,000 agents in ninety days"
  - "The Ghost VM credential heist"
  - "Downtime is the real killer"
card_topic: "AI + Resilience"
topic_count: 6
threats: ["Agentic AI Risk", "Identity Theft", "Ransomware", "Ghost VM Attack"]
industries: ["Technology", "Information Technology"]
speakers: ""
---

## TL;DR (Too Long, Didn't Read)
*   **Agentic AI Risk:** The rapid rise of AI agents (from 0 to 4,000 in three months for one client) creates a massive, unmanaged attack surface due to over-provisioned permissions.
*   **Data is the Core:** Most organizations are not ready for AI because they lack basic data inventory and classification; you cannot secure what you cannot find.
*   **The "Downtime" Threat:** The real economic impact of a breach is not the hack itself, but the long tail of business interruption and recovery time.
*   **Identity is the Weak Link:** Administrative identity and misconfigured MFA (especially on VPNs and test accounts) remain the primary drivers of mass destruction events.
*   **Resilience vs. Protection:** Security must shift from just "preventing" to "ensuring recovery" through automated, tested, and orchestrated processes.
*   **Complexity Increases Fragility:** As more AI and security tools are added to endpoints, the likelihood of system failure and "fragility" increases.

## New Tools, Techniques, and Tactics
*   **Agentic AI:** AI agents capable of performing tasks autonomously; currently a major risk due to "over-provisioning" (giving them too much authority).
*   **Breach Truth:** A concept of basing security orchestration on the actual technical realities and behaviors observed during real-world breaches.
*   **Argos 999:** A data discovery platform mentioned to help map data dependencies and ensure critical applications are fully backed up.
*   **Rehydration:** A technique to remotely rebuild a device from bare metal (bit-level wipe) to quickly recover from ransomware or corruption.
*   **Just-in-Time (JIT) Provisioning:** Granting access only when needed and for a limited time to enforce the principle of least privilege.
*   **Ghost VM Attack:** A tactic where attackers create a hidden virtual machine to mount detached disks and harvest sensitive files (like the Active Directory database).

## Detection & Defense Insights
*   **Identity Governance:** Focus on "non-human identities" (agents) which are expected to soon overwhelm human identities in volume.
*   **Data-Centric Defense:** Prioritize the five pillars of Zero Trust, specifically focusing on the **Data** and **Application** layers, where most organizations fail.
*   **MFA Enforcement:** Ensure MFA is applied universally, specifically targeting VPNs and "forgotten" test/admin accounts.
*   **Log Analysis:** Use Machine Learning (rather than LLMs) for log aggregation and anomaly detection to avoid "hallucinations" in security signals.
*   **Endpoint Resilience:** Monitor the "health" and presence of security agents on endpoints to ensure they haven't been disabled or broken by complexity.
*   **Orchestration over Tools:** Recognize that buying more tools won't help if they aren't orchestrated through policy, people, and process.

## Real-World Examples & Stories
*   **The 4,000 Agent Explosion:** A customer went from zero AI agents in January to 4,000 by March, highlighting the speed of the attack surface expansion.
*   **The "Test Account" Disaster:** A massive breach occurred where thousands of VMs were encrypted because a single test account lacked MFA on a VPN.
*   **The Scattered Spider Case:** Attackers used a "Ghost VM" to bypass PAM (Privileged Access Management) by harvesting credentials from the Active Directory database.
*   **The "Magic IT" Fallacy:** During tabletop exercises, leaders often assume IT will "magically" fix everything, ignoring the reality of weeks-long downtime.
*   **The 800MHz Radio Lesson:** An emergency response test failed because the "backup" communication tools (radios) had dead batteries and were unmaintained.

## Research, References & Resources
*   **NIST Zero Trust Framework:** The standard framework for assessing readiness across identity, device, network, workload, and data.
*   **HESK (Higher Education Information Cloud Security):** A standardized request for compliance mentioned in the context of university data sharing.
*   **CMMC 2.0:** Cybersecurity Maturity Model Certification, relevant for organizations handling controlled unclassified information (CUI).
*   **Absolute Security Resilience Report:** A study mentioned regarding the fragility and patching delays of endpoint devices.

## Key Industry Insights & Trends
*   **The AI Craze:** A period of rapid, often unmanaged, adoption of AI technology driven by "Fear Of Missing Out" (FOMO).
*   **Shift to Non-Human Identities:** The identity landscape is shifting from managing employees to managing thousands of autonomous AI agents.
*   **Complexity = Fragility:** As organizations add more "AI-ready" layers to their tech stack, the systems become more prone to breaking and failing.
*   **Downtime as an Economic Metric:** The industry is moving toward measuring "resilience" (time to recover) rather than just "security" (prevention).

## Business & Risk Implications
*   **Operational Risk:** Inadequate recovery plans can lead to months of downtime, making it impossible to pay employees or serve customers.
*   **Financial Risk:** The cost of business interruption often far exceeds the immediate cost of the cyberattack or ransom.
*   **Reputational Risk:** Slow recovery times lead to customers finding alternative providers, potentially causing permanent market share loss.
*   **Compliance Risk:** Failure to classify data before deploying AI can lead to violating customer agreements and regulatory requirements.

## Opinions vs Facts
*   **Fact:** AI agents are being provisioned with high levels of authority in many environments.
*   **Fact:** Many organizations lack a formal incident response plan or a clear data inventory.
*   **Opinion:** "The AI Craze" is a period of unmanaged hype that will see many vendors disappear.
*   **Opinion:** Traditional PAM (Privileged Access Management) is not a "silver bullet" because it can be bypassed if the underlying Active Directory is compromised.
*   **Prediction:** Non-human identities will eventually overwhelm human identities in most enterprise environments.

## Contradictions & Debates (if any)
*   **Dwell Time Statistics:** The speaker challenges the industry standard of "203 days" for dwell time, arguing that modern attackers move much faster (15 minutes to 72 hours) to avoid detection.
*   **The Value of Tools:** There is a debate between the "buy more tools" mentality and the "orchestrate existing tools" reality.

## Actionable Takeaways
*   **For CISOs:** Quantify cyber risk in terms of **business process impact** (e.g., "If this app goes down, we lose $X per day") to get executive buy-in.
*   **For SOC Teams:** Prioritize the discovery and classification of sensitive data *before* enabling Agentic AI capabilities.
*   **For Security Leaders:** Move beyond "prevention" tabletop exercises; conduct "recovery" exercises that test if you can actually rebuild systems and get people back to work.
*   **For IT/Security Ops:** Audit all "test" and "service" accounts to ensure they are covered by MFA and follow the principle of least privilege.
*   **For All:** Implement "Just-in-Time" access and automated "rehydration" capabilities to reduce the window of opportunity for attackers.
