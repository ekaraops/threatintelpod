---
title: "SANS Stormcast Thursday, April 2nd, 2026: Script Removing ADS/MotW; Google Chrome 0-Day; iOS/iP…"
date: 2026-04-02T01:02:31.000Z
draft: false
channel: "SANS Internet Storm Center"
channel_slug: "sans-isc"
category: "threat-intelligence"
youtube_url: "https://www.youtube.com/watch?v=2lxRXEoH-2k"
video_id: "2lxRXEoH-2k"
thumbnail: "https://i.ytimg.com/vi/2lxRXEoH-2k/sddefault.jpg"
description: "AI-generated summary of SANS Stormcast Thursday, April 2nd, 2026: Script Removing ADS/MotW; Google Chrome 0-Day; iOS/iP… from SANS Internet Storm Center"
tags: ["threat-intelligence"]
hook: "Your security tools are being blinded by a single PowerShell command."
stings:
  - "The invisible 'Mark of the Web' erasure"
  - "State-sponsored exploits hitting the mainstream"
  - "Silent router hijacking via a single click"
card_topic: "Stealth + Exploitation"
topic_count: 6
threats: ["Exploit Kits", "CSRF", "Use-after-free", "MotW Removal"]
industries: ["Consumer Electronics", "Telecommunications"]
speakers: "Johannes Ullrich"
---

## TL;DR (Too Long, Didn't Read)
*   Attackers are using PowerShell to strip "Mark of the Web" (MotW) from downloaded files to hide from security tools.
*   Google Chrome has a critical "use-after-free" vulnerability in its Dawn (Web GPU) component that is currently being exploited.
*   Apple released urgent updates for iOS 18.7 and iPadOS 18.7 to fix 25 vulnerabilities, including those used by the "Dark Sword" exploit kit.
*   Asus routers have a Cross-Site Request Forgery (CSRF) vulnerability that allows attackers to reconfigure them silently.
*   Older mobile devices (dating back to iPhone XR) remain high-priority targets for sophisticated exploit kits.
*   Attackers are increasingly targeting home networking hardware to gain a foothold in networks.

## New Tools, Techniques, and Tactics
*   **MotW Removal:** Using PowerShell commands to delete the "Zone.Identifier" alternate data stream from files.
*   **Dawn Component Exploitation:** Targeting the Web GPU implementation within the Chrome browser.
*   **Dark Sword Exploit Kit:** A toolkit used to deliver mobile exploits, moving from state-sponsored use to wider availability.
*   **CSRF Router Attacks:** Using web-based requests to trick a user's browser into changing router settings without their knowledge.

## Detection & Defense Insights
*   **Monitor PowerShell Activity:** Watch for commands specifically targeting the removal of `Zone.Identifier` from files.
*   **File Integrity Monitoring:** Look for files that have lost their "Mark of the Web" status unexpectedly.
*   **Browser Patching:** Prioritize immediate updates for Google Chrome to mitigate the Dawn component vulnerability.
*   **Mobile Device Management (MDM):** Ensure all iOS and iPadOS devices are updated to version 18.7 or higher.
*   **Router Security:** Audit home and branch office routers for firmware updates, specifically targeting Asus devices.

## Real-World Examples & Stories
*   **The Stealthy Script:** An attacker wrote a file to a system and then immediately ran a script to hide the fact that it came from the internet.
*   **The Router Trick:** An attacker places a malicious link on a website; if a user visits it, their router is reconfigured without them seeing any error messages.
*   **The Aging iPhone:** Discussion on how devices like the iPhone XR are still being targeted by modern exploit kits.

## Research, References & Resources
*   **Google Chrome Security Updates:** Documentation regarding the 21 fixed vulnerabilities.
*   **Apple iOS 18.7/iPadOS 18.7:** Official security release notes.
*   **Asus Router Security Advisory:** Information regarding the CSRF vulnerability.

## Key Industry Insights & Trends
*   **Democratization of Exploits:** High-end "state-sponsored" style attacks (like Dark Sword) are becoming available to more attackers.
*   **Targeting the "Edge":** Attackers are moving toward home routers and mobile devices to bypass traditional enterprise perimeter security.
*   **Component-Specific Attacks:** Vulnerabilities are increasingly found in specialized browser components like Web GPU (Dawn).

## Business & Risk Implications
*   **Endpoint Risk:** If attackers can strip MotW, standard EDR/AV tools may fail to flag suspicious downloads.
*   **Mobile Workforce Risk:** Unpatched mobile devices (iOS) create easy entry points for attackers to access corporate data.
*   **Network Perimeter Risk:** Vulnerable routers can allow attackers to intercept traffic or change network configurations, leading to data breaches.
*   **Operational Risk:** Critical browser vulnerabilities require immediate patching cycles to prevent widespread exploitation.

## Opinions vs Facts
*   **Fact:** Google Chrome has a "use-after-free" vulnerability in Dawn that is being exploited.
*   **Fact:** Apple released updates for iOS 18.7 to fix 25 vulnerabilities.
*   **Fact:** Attackers used PowerShell to remove the Zone Identifier from a file.
*   **Opinion:** The speaker suggests that older devices are particularly vulnerable because they lack modern countermeasures.

## Contradictions & Debates (if any)
*   *No significant contradictions or debates were noted in this episode.*

## Actionable Takeaways
*   **CISO:** Ensure the organization has a policy for rapid patching of browsers and mobile devices.
*   **SOC Team:** Create a detection rule for PowerShell commands that modify or delete `Zone.Identifier` streams.
*   **Security Leader:** Review the lifecycle of mobile devices; ensure older hardware is either patched or retired if it can no longer receive security updates.
*   **IT Admin:** Push the latest firmware updates to all Asus routers within the organization's footprint.
