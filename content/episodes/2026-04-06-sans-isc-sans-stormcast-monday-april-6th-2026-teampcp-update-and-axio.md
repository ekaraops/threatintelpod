---
title: "SANS Stormcast Monday, April 6th, 2026: TeamPCP Update and Axio Post Mortem; Fortinet 0-Day (#)"
date: 2026-04-06T00:31:34.000Z
draft: false
channel: "SANS Internet Storm Center"
channel_slug: "sans-isc"
category: "threat-intelligence"
youtube_url: "https://www.youtube.com/watch?v=CwxFBw6K5w8"
video_id: "CwxFBw6K5w8"
thumbnail: "https://i.ytimg.com/vi/CwxFBw6K5w8/sddefault.jpg"
description: "AI-generated summary of SANS Stormcast Monday, April 6th, 2026: TeamPCP Update and Axio Post Mortem; Fortinet 0-Day (#) from SANS Internet Storm Center"
tags: ["threat-intelligence"]
---

## TL;DR (Too Long, Didn't Read)
*   The TeamPCP threat group has slowed down; no new compromises attributed to them in about two weeks.
*   A major breach at Axio was actually caused by North Korean social engineering, not TeamPCP.
*   Attackers used a fake video call update to trick a developer into installing malware.
*   New malicious NPM packages are targeting users of the Strapi CMS.
*   Fortinet released an urgent fix for a zero-day vulnerability in FortiClient EMS being used in the wild.
*   The Fortinet flaw allows unauthenticated attackers to run unauthorized code.

## New Tools, Techniques, and Tactics
*   **Fake Video Call Updates:** Attackers trigger a fake "software update" pop-up during a video call to trick users into installing malware.
*   **Long-Game Social Engineering:** Actors spent two weeks building rapport with a target before launching the technical attack.
*   **Malicious NPM Extensions:** Attackers are publishing fake "extension" packages for the Strapi CMS to trick developers.
*   **Unauthenticated RCE:** A vulnerability in FortiClient EMS allows remote code execution without needing login credentials.
*   **NPM Package Poisoning:** The continued use of compromised versions (like version 0.3.0 of the Axio package) to distribute malware.

## Detection & Defense Insights
*   **Monitor NPM Registries:** Watch for sudden changes or suspicious versions in widely used packages.
*   **Endpoint Protection:** Use EDR to detect unauthorized code execution resulting from "software updates" triggered by web browsers or video apps.
*   **Fortinet Patching:** Prioritize the hotfix for FortiClient EMS immediately to prevent remote exploitation.
*   **Developer Awareness:** Train developers to be skeptical of "required updates" prompted during unexpected video calls.
*   **Supply Chain Auditing:** Regularly audit third-party NPM dependencies, especially those marketed as "extensions" for CMS platforms.

## Real-World Examples & Stories
*   **The Axio Incident:** A lead developer was tricked by North Korean actors during a video call. The attackers spent weeks pretending to be a legitimate company.
*   **The "Update" Trick:** During a video call, a fake error message appeared, telling the developer their video software needed an update to join the call.
*   **TeamPCP Wave:** A large wave of compromises occurred recently, but the "new" victims being reported now are actually from the original initial wave.
*   **Rapid NPM Response:** The Axio compromised package was identified within minutes of release, though it took a few hours to remove it from the registry.

## Research, References & Resources
*   **Safeep.io Blog:** Contains details on compromised NPM packages related to the Strapi CMS.
*   **Fortinet Security Advisory:** Urgent notice regarding the FortiClient EMS zero-day vulnerability.
*   **TeamPCP Updates:** Ongoing reports regarding the status of the TeamPCP threat group and their victims.
*   **Axio Post-Mortem:** Detailed breakdown of the social engineering attack against Axio.

## Key Industry Insights & Trends
*   **Social Engineering Sophistication:** Attackers are moving away from simple phishing to long-term, multi-week relationship building.
*   **Supply Chain Targeting:** Attackers are increasingly targeting the "helper" ecosystem (NPM extensions) rather than just well-known packages.
*   **Zero-Day Exploitation:** Critical infrastructure tools like Fortinet are being actively targeted by attackers before patches are widely applied.
*   **NPM as a Primary Vector:** The NPM registry remains a high-frequency target for malware distribution.

## Business & Risk Implications
*   **Developer Risk:** High-level developers are primary targets; a single compromised workstation can lead to a massive supply chain breach.
*   **Operational Downtime:** Unpatched zero-days in security tools (like Fortinet) can lead to full network compromise and significant downtime.
*   **Reputational Damage:** Companies may be wrongly associated with threat groups (like TeamPCP) due to timing, causing confusion during incident response.
*   **Supply Chain Liability:** Using unverified CMS extensions introduces significant risk to the software products your company builds.

## Opinions vs Facts
*   **Fact:** Fortinet released a hotfix for a zero-day in FortiClient EMS that is being exploited in the wild.
*   **Fact:** The Axio breach was caused by social engineering, not TeamPCP.
*   **Fact:** There are new malicious NPM packages targeting Strapi users.
*   **Opinion:** The speaker notes that social engineering via video calls is "really hard not to fall for."
*   **Opinion:** The speaker suggests that lists of TeamPCP victims found online are likely incomplete.

## Contradictions & Debates (if any)
*   **Attribution Confusion:** There was initial confusion linking the Axio breach to TeamPCP due to timing, but the post-mortem proved it was a separate North Korean operation.

## Actionable Takeaways
*   **CISO:** Ensure the security team has a process for immediate patching of "active exploitation" advisories (e.g., Fortinet).
*   **SOC Team:** Monitor for unusual developer activity, such as unexpected software installations or unusual NPM package downloads.
*   **Security Leader:** Implement "Zero Trust" principles for software updates; users should never install software prompted by a web link or a video call.
*   **DevOps/Engineering:** Audit all Strapi CMS extensions and NPM dependencies to ensure they are from trusted, verified sources.
