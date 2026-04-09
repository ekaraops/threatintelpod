---
title: "Who Really Controls the Internet—And Why it Matters with Emily Taylor and Roxana Radu"
date: 2025-12-11T21:28:58-08:00
draft: false
channel: "SANS Institute"
channel_slug: "sans-institute"
category: "cybersecurity"
youtube_url: "https://www.youtube.com/watch?v=z3usk3jCPBc"
video_id: "z3usk3jCPBc"
thumbnail: "https://i.ytimg.com/vi/z3usk3jCPBc/sddefault.jpg"
description: "AI-generated summary of Who Really Controls the Internet—And Why it Matters with Emily Taylor and Roxana Radu from SANS Institute"
tags: ["cybersecurity"]
hook: "The internet isn't a single global network anymore—it's fracturing into geopolitical islands of control."
stings:
  - "Ukraine tried to disconnect Russia from the web, but the technical gatekeepers said no"
  - "The 'Council of Greybeards' manages the world's core protocols through informal consensus"
  - "Decades of technical inertia mean we are still running on aging, vulnerable plumbing"
card_topic: "Internet Governance + Splinternet"
topic_count: 7
---

## TL;DR (Too Long, Didn't Read)
* The internet is a distributed system designed to resist central control, but it relies on critical "choke points" like the Domain Name System (DNS).
* Internet governance is a complex mix of "soft law" (voluntary industry standards) and "hard law" (government regulations).
* Key technical bodies like the IETF and ICANN operate through consensus and "rough consensus," often making them invisible to the general public.
* Geopolitical tensions (e.g., US vs. China, Russia vs. Ukraine) are fragmenting the internet into "islands" of different standards and controls.
* Foundational protocols (like IPv4) are aging and difficult to replace due to massive technical inertia and lack of backward compatibility.
* While the system is fragile and politically contested, voluntary cooperation and signal-sharing initiatives still provide a baseline of stability.

## New Tools, Techniques, and Tactics
* **Soft Law vs. Hard Law:** A framework for understanding governance; soft law refers to voluntary standards (IETF), while hard law refers to binding government regulations.
* **Multistakeholder Model:** A governance approach where various groups (government, industry, civil society) collaborate rather than a single entity ruling.
* **Global Signal Exchange:** An initiative mentioned to enable international threat signal sharing across different sectors to fight cybercrime.
* **Rough Consensus and Running Code:** The core philosophy of the IETF used to decide on technical standards without formal voting.
* **Digital Barricades:** A concept describing how nations are building technical and regulatory walls to control their own internet environments.

## Detection & Detection Insights
* **BGP Route Hijacking:** A critical vulnerability where internet traffic is misrouted; monitoring for unexpected routing changes is essential.
* **DNS Vulnerabilities:** Since DNS is the "underpinning of trust," monitoring for DNS hijacking or unauthorized changes to domain records is vital.
* **Protocol Aging:** Awareness that older protocols (like IPv4 or ARP) have inherent trust weaknesses that attackers exploit.
* **Signal Sharing:** The importance of participating in international threat intelligence exchanges to detect global trends.
* **Infrastructure Fragility:** Recognizing that even "invisible" services like root servers or IP registries are single points of failure.

## Real-World Examples & Stories
* **The Ukraine/Russia Incident (2022):** The Ukrainian government requested ICANN to disconnect Russia from the internet; ICANN declined, highlighting the limits of technical governance.
* **WannaCry Ransomware:** Mentioned as a catalyst for discussions around a "Digital Geneva Convention" due to its massive global impact.
* **The IPv6 Struggle:** A decades-long example of how difficult it is to upgrade the internet's "plumbing" due to costs and lack of backward compatibility.
* **The "Council of Greybeards":** A metaphor used to describe the small, highly technical, and often informal groups that manage the internet's core protocols.

## Research, References & Resources
* **"Negotiating Internet Governance" by Roxana Radu:** A key book for understanding the power dynamics of the digital world.
* **IETF (Internet Engineering Task Force):** The body that sets the technical standards for how the internet functions.
* **ICANN (Internet Corporation for Assigned Names and Numbers):** The nonprofit that coordinates the global DNS and IP address space.
* **UN Cybercrime Convention:** A recent global framework aimed at aligning national laws to fight digital crime.
* **SANS SISO Network:** A community for security leaders to collaborate on these complex issues.

## Key Industry Insights & Trends
* **Fragmentation (Splinternet):** The trend of the internet moving away from a single global system toward nationalized, controlled versions (e.g., China's model).
* **Geopolitical Tech Competition:** Technology is no longer just a tool; it is the primary arena where global power struggles are played out.
* **Technical Inertia:** The massive difficulty in upgrading foundational technology once it has reached global scale.
* **Shift from Optimism to Realism:** The 1990s vision of a "borderless internet" has been replaced by a reality of digital borders and regulation.

## Business & Risk Implications
* **Operational Risk:** Reliance on aging protocols and centralized "choke points" means technical failures or hijacks can disrupt entire business operations.
* **Regulatory Risk:** As "hard law" increases, companies must navigate a patchwork of conflicting international privacy and content laws.
* **Geopolitical Risk:** Businesses operating globally may face sudden changes in connectivity or internet access due to international conflicts.
* **Architectural Risk:** Failure to plan for shifts in internet architecture (like IPv6 or new IP standards) can lead to long-term technical debt.

## Opinions vs Facts
* **Fact:** The internet is a distributed system; ICANN is a California-based nonprofit; IETF uses "rough consensus."
* **Fact:** IPv6 adoption has been a long-standing technical challenge.
* **Opinion/Prediction:** The internet may continue to fragment into "islands" of different standards over the next 5-10 years.
* **Opinion:** The current system of internet governance is "fragile" and "chaotic."

## Contradictions & Debates (if any)
* **Control vs. Coordination:** ICANN claims to be a "coordinator" rather than a "controller," but governments often view them as having immense power.
* **Openness vs. Security:** The debate over whether the internet should remain completely open/unregulated or move toward more controlled, "secure" national versions.
* **Consensus vs. Power:** While the IETF claims to be open to everyone, speakers noted that certain nationalities and technical experts hold much more influence.

## Actionable Takeaways
* **For CISOs:** Assign team members to specifically monitor long-term technology trends and internet architecture changes to avoid being blindsided.
* **For SOC Teams:** Prioritize monitoring for BGP hijacks and DNS anomalies, as these target the internet's most vulnerable foundational layers.
* **For Security Leaders:** Engage with industry standards bodies and participate in threat signal-sharing initiatives to improve collective defense.
* **For All Leaders:** Move beyond just "defending the perimeter" and start understanding the underlying governance and protocols that make your connectivity possible.
