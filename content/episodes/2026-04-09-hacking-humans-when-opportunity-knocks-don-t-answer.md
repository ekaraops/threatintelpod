---
title: "When “opportunity” knocks, don’t answer."
date: 2026-04-09T05:00:00.000Z
draft: false
channel: "Hacking Humans"
channel_slug: "hacking-humans"
category: "stories"
youtube_url: "https://pdst.fm/e/pdrl.fm/7d51b0/traffic.megaphone.fm/CYBW9589328900.mp3?updated=1775675871"
video_id: "pod-hacking-humans-when-opportunity-knocks-don-t-"
thumbnail: "https://megaphone.imgix.net/podcasts/8797f03a-a50b-11ea-b6c0-87ebb093948d/image/hacking-humans-cover-art-cw.png?ixlib=rails-4.3.1&max-w=3000&max-h=3000&fit=crop&auto=format,compress"
description: "AI-generated summary of When “opportunity” knocks, don’t answer. from Hacking Humans"
tags: ["stories"]
hook: "Your most trusted platforms are being weaponized to bleed you dry."
stings:
  - "A Scrabble game turns into a predator's playground"
  - "The $20 million mountain rescue hoax"
  - "Legitimate tools used for illegitimate takeover"
card_topic: "Social + Engineering"
topic_count: 6
threats: ["Phishing","RMM Abuse","Social Engineering","Lookalike Domains"]
industries: ["Finance","Travel","Technology"]
speakers: "Dave Bittner, Joe Carrigan, Maria Varmazis"
---

## TL;DR (Too Long, Didn't Read)
*   **LinkedIn Phishing:** Attackers are using fake LinkedIn notifications and lookalike domains (e.g., "Inked in") to steal credentials via urgent "business opportunity" lures.
*   **Tax Season Scams:** Fraudsters are impersonating the IRS via phone and email, often using Remote Monitoring and Management (RMM) tools to take over computers.
*   **Everest Fraud:** A massive $20 million scam involves guides inducing altitude sickness in climbers to trigger expensive, fraudulent helicopter rescues.
*   **Social Engineering via Games:** Scammers are using the chat functions in casual games like Scrabble to build rapport and move victims to unmonitored platforms like Telegram.
*   **RMM Abuse:** Nearly 40% of recent tax fraud involves the misuse of legitimate remote management tools to bypass security filters.
*   **The "Trust" Gap:** A recurring theme is that attackers exploit environments and individuals that trust established platforms (LinkedIn, IRS, or even casual game players) too much.

## New Tools, Techniques, and Tactics
*   **Lookalike Domains:** Using visually similar names (e.g., "Inked in" instead of "LinkedIn") to deceive users on login pages.
*   **RMM Tool Exploitation:** Using legitimate Remote Monitoring and Management tools (often whitelisted by IT) to gain full control of a victim's machine during phishing attacks.
*   **Induced Medical Emergencies:** A physical tactic where scammers (in the Everest case) use substances like baking soda or specific medications to mimic altitude sickness.
*   **Platform Shifting:** Moving a conversation from a monitored or public environment (Scrabble chat) to a private, unmonitored one (Telegram or WhatsApp) to facilitate a scam.
*   **Urgency & Authority Lures:** Using "urgent business opportunities" or "IRS tax issues" to bypass a victim's critical thinking.

## Detection & Defense Insights
*   **Monitor RMM Usage:** Be highly suspicious of any unexpected requests to install or use remote desktop/management tools, especially following an email.
*   **Domain Verification:** Train users to inspect the actual URL of a login page, not just the visual branding or logos.
*   **Inbound Communication Policy:** Adopt a "don't trust inbound" rule for sensitive matters; if the IRS or a bank calls, hang up and call them back using an official, verified number.
*   **Zero Trust Execution:** Implement "default deny" policies for software execution to prevent unknown or unauthorized tools from running.
*   **Email Header Analysis:** Watch for sender addresses that do not match the official domain of the service they claim to represent.

## Real-World Examples & Stories
*   **The Scrabble Seducer:** A case study from Reddit where a scammer used a Scrabble game to build a fake persona (a lumberjack traveling to Canada) to target a victim.
*   **Everest Rescue Scam:** A widespread fraud where guides, helicopter companies, and hospitals conspired to bill $20 million in fake emergency evacuations.
*   **The "Ghost" Tax Preparer:** Temporary, "pop-up" tax shops that appear near tax deadlines to collect fees and disappear without filing correctly.
*   **The IRS Phone Scam:** A classic example where scammers demand immediate payment or personal info, often using threats of legal action to create panic.

## Research, References & Resources
*   **Cofense Phishing Defense Center:** Provided research on the LinkedIn credential harvesting campaign.
*   **Proofpoint:** Reported that 40% of 2026 tax fraud involves the use of RMM tools.
*   **Better Business Bureau (BBB):** Provided warnings regarding tax-related scams and "ghost" preparers.
*   **Kathmandu Post:** Reported on the investigative findings regarding the Everest climbing scams.
*   **r/scambait:** A community resource for observing and documenting real-world social engineering attempts.

## Key Industry Insights & Trends
*   **Weaponizing Legitimacy:** Attackers are moving away from "obvious" malware and toward using legitimate tools (RMM, LinkedIn, official-looking emails) to stay under the radar.
*   **Industry-Specific Targeting:** Scammers are finding niche ways to exploit specific high-value activities, such as professional networking or extreme tourism.
*   **The Decline of Platform Trust:** As platforms like LinkedIn become "cesspools" of spam, users may become desensitized, making them more vulnerable to sophisticated spoofs.
*   **Automation in Scams:** The use of chatbots and automated scripts to engage in long-form social engineering (as seen in the Scrabble example).

## Business & Risk Implications
*   **Financial Loss:** Direct theft through fraudulent billing (Everest) or tax fraud can cost individuals and organizations millions.
*   **Operational Risk:** If an attacker uses RMM tools to take over a corporate machine, they gain a foothold for ransomware or data exfiltration.
*   **Reputational Risk:** For service providers (like travel guides or tax preparers), being associated with fraud can lead to total business collapse.
*   **Insurance Volatility:** Widespread fraud (like the Everest case) can lead insurance companies to stop covering certain high-risk activities entirely.

## Opinions vs Facts
*   **Fact:** Attackers are using lookalike domains for LinkedIn phishing.
*   **Fact:** 40% of tracked tax fraud involves RMM tools (per Proofpoint).
*   **Opinion:** One speaker stated that LinkedIn has become a "cesspool" and a "scam platform."
*   **Opinion/Prediction:** The discussion regarding whether insurance companies will stop covering Everest climbs is a potential outcome, not a confirmed fact.

## Contradictions & Debates (if any)
*   **The Value of LinkedIn:** There is a debate between the necessity of LinkedIn for professional networking (especially in sectors like Space/InfoSec) versus its high volume of spam and scams.
*   **The Speed of Government:** A discussion occurred regarding whether the "slow" nature of official government communication (letters vs. email) is a flaw or a necessary security feature.

## Actionable Takeaways
*   **For CISOs:** Implement "Default Deny" at the execution level and strictly control/monitor the use of RMM tools within the enterprise.
*   **For SOC Teams:** Create alerts for "lookalike" domain patterns and monitor for unusual outbound connections to known RMM provider IP ranges.
*   **For Security Leaders:** Conduct training specifically on "Platform Shifting"—teaching employees that a legitimate conversation on one app should never move to an unmanaged app (like Telegram) for business.
*   **For All Employees:** If you receive an "urgent" notification regarding taxes or professional accounts, do not click the link. Navigate to the official website manually through your browser.
