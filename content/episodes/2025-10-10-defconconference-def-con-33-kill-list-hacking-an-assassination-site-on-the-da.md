---
title: "DEF CON 33 - Kill List: Hacking an Assassination Site on the Dark Web - Carl Miller, Chris Monteiro"
date: 2025-10-10T14:39:34-07:00
draft: false
channel: "DEFCONConference"
channel_slug: "defconconference"
category: "cybersecurity"
youtube_url: "https://www.youtube.com/watch?v=cYZmRp90hss"
video_id: "cYZmRp90hss"
thumbnail: "https://i.ytimg.com/vi/cYZmRp90hss/sddefault.jpg"
description: "AI-generated summary of DEF CON 33 - Kill List: Hacking an Assassination Site on the Dark Web - Carl Miller, Chris Monteiro from DEFCONConference"
tags: ["cybersecurity"]
hook: "The darknet's most feared assassination empire was actually a massive scam empire fueled by real-world murder plots."
stings:
  - "A 'hitman comparison site' on Google was secretly funneling killers to the darknet"
  - "Investigators used a simple URL tweak to leak thousands of real-world kill orders"
  - "32 arrests and 28 convictions from a single insecure web server"
card_topic: "Darknet + Fraud"
topic_count: 8
---

## TL;DR (Too Long, Didn't Read)
*   A darknet "assassination site" (Bisa Mafia 2) was actually a massive, sophisticated scam empire run by an individual named Yura.
*   While the "hitmen" were fake (the site always asked for more money to "complete" a hit), the people placing the orders were very real and extremely dangerous.
*   Investigators used technical exploits to gain full control of the site, exfiltrating thousands of messages and "kill orders."
*   The investigation revealed a global network of perpetrators, including family members, spouses, and professionals, plotting real-world violence.
*   By working with the FBI and local journalists, the team successfully warned targets and facilitated 32 arrests and 28 convictions.
*   The site's operator used clever "lightnet" SEO marketing to drive legitimate users toward his fraudulent darknet services.

## New Tools, Techniques, and Tactics
*   **SEO-Driven Darknet Funneling:** The attacker created a "hitman comparison site" on the clear web (lightnet) that was highly optimized for Google, funneling victims toward his darknet site.
*   **Scam-as-a-Service:** The operator franchised his codebase and brand to others, creating a sprawling empire of fraudulent services.
*   **Disinformation Campaigns:** The administrator used social media to spread rumors of successful murders to create "social proof" and legitimacy.
*   **Insecure Direct Object Reference (IDOR):** The site's messaging system allowed users to view other people's private messages simply by changing a number in the URL.
*   **Parameter Tampering:** Used to iterate through and exfiltrate the entire database of private communications.
*   **Data Exfiltration Engine:** The investigators built a custom script to scrape the site daily, sending orders to an AWS data lake for analysis.

## Detection & Defense Insights
*   **Web Server Misconfigurations:** The site had open directories (Apache misconfiguration) that exposed administrative screenshots and templates.
*   **SQL Injection (SQLi):** The site was vulnerable to SQLi, which allowed attackers to gain a web shell and Remote Code Execution (RCE).
*   **Plaintext Credentials:** A mailing component misconfiguration exposed the administrator's email and password in plaintext.
*   **Lack of Patch Management:** The site was running unpatched software, making it easy to compromise.
*   **Identity/Pattern of Life:** Attackers often used Facebook profile pictures for targets, providing a clear link between darknet personas and real-world identities.

## Real-World Examples & Stories
*   **The "Bob the Builder" Hit:** To test the site's messaging, the investigator placed a fake hit on a fictional character, which granted him access to the internal chat.
*   **The Zurich Case:** An investigator warned a woman (Elena) that her husband was trying to kill her; she was so unphased she still went to dinner with his neighbor.
*   **The Utah Kidnapping Plot:** A religious man (Christopher Pence) attempted to pay $60,000 to have his adoptive children's biological parents kidnapped and addicted to heroin.
*   **The "Mufasa" Password:** An FBI raid on a neonatologist (Ron Ilg) found a post-it note with his darknet username and the password "Mufasa."
*   **The Administrator's Irony:** The site admin was caught in a screenshot trying to find a "secure-looking" padlock icon to add to his highly insecure website.

## Research, References & Resources
*   **Pirate.london:** The website used by the speakers to coordinate investigations and warnings.
*   **Rational Wiki:** Where the investigator (Chris) originally documented his findings on darknet economics.
*   **AWS Data Lake:** Used by the investigators to store and organize the massive amount of exfiltrated data.
*   **Bitcoin Tracing:** A key method used to link darknet orders to real-world financial identities.

## Key Industry Insights & Trends
*   **The "Scam" Nature of Extreme Darknet Services:** Most "extreme" services (assassinations, red rooms) are scams designed to exploit the desperation of criminals.
*   **The Danger of the "User":** Even if the service is fake, the intent of the person paying is real, making these sites a catalyst for actual domestic and targeted violence.
*   **Convergence of Clear Web and Darknet:** Criminals are increasingly using legitimate SEO and social media to drive traffic to illegal darknet marketplaces.
*   **Law Enforcement Challenges:** The global, decentralized nature of these crimes makes it difficult for single local police forces to take jurisdiction.

## Business & Risk Implications
*   **Reputational Risk for Platforms:** Social media platforms (like Facebook) are often the source of "pattern of life" data used by criminals to identify targets.
*   **Operational Risk for Law Enforcement:** Investigating these sites requires high-level coordination between international agencies (FBI, Interpol, Europol).
*   **Financial Risk (Crypto):** While Bitcoin provides anonymity, it also provides a permanent ledger that can be used to convict criminals if traced correctly.

## Opinions vs Facts
*   **Fact:** The website was technically insecure (IDOR, SQLi, open directories).
*   **Fact:** 32 arrests and 28 convictions were made based on the disclosed data.
*   **Opinion/Observation:** The speakers noted that the "hitmen" were the most incompetent in the world because they never actually completed a hit.
*   **Prediction/Assumption:** The speaker assumes that many other kill orders remain uninvestigated due to lack of resources.

## Contradictions & Debates (if any)
*   **Police Response vs. Severity:** The speakers highlighted a contradiction where the police treated the investigator's report as a "mental health check" rather than a serious criminal threat.
*   **The "Realism" of the Site:** There was a debate between whether the site was a "real" criminal enterprise or just a scam; the conclusion was that it was a scam service, but the *threat* it facilitated was real.

## Actionable Takeaways
*   **For SOC/Security Teams:** Monitor for "pattern of life" data leaks; ensure employees' social media presence doesn't provide actionable intelligence to bad actors.
*   **For Law Enforcement:** Prioritize cross-jurisdictional intelligence sharing; a crime spanning multiple countries (like the assassination orders) requires a unified response.
*   **For Security Researchers:** Focus on the "economics" of crime; understanding how scammers use SEO and marketing can help predict where the next wave of darknet activity will emerge.
*   **For CISO/Leaders:** Recognize that "extreme" cybercrime often has a physical, real-world component that can impact employee safety.
