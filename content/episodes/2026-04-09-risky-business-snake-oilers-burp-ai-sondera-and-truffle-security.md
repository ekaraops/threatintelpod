---
title: "Snake Oilers: Burp AI, Sondera and Truffle Security"
date: 2026-04-09T21:41:01.000Z
draft: false
channel: "Risky Business"
channel_slug: "risky-business"
category: "news"
youtube_url: "https://www.youtube.com/watch?v=uGrru0FP85I"
video_id: "uGrru0FP85I"
thumbnail: thumbnail: "https://i.ytimg.com/vi/uGrru0FP85I/sddefault.jpg"
description: "AI-generated summary of Snake Oilers: Burp AI, Sondera and Truffle Security from Risky Business"
tags: ["news"]
hook: "The era of the autonomous attacker has arrived, and your AI agents are already leaking your keys."
stings:
  - "The chainsaw of automated exploitation"
  - "AI agents running wild in your home directory"
  - "When 'policy as code' becomes the only leash"
card_topic: "AI + Security"
topic_count: 6
threats: ["Secret Leakage","AI Agent Hijacking","Automated Vulnerability Discovery"]
industries: ["Software Development","Cybersecurity"]
speakers: "Patrick Gray"
---

## TL;DR (Too Long, Didn't Read)
* **PortSwigger (Burp Suite)** is integrating AI to act as a "co-pilot" for security testers, helping them find complex vulnerabilities faster without replacing human expertise.
* **Sondera** provides a "harness" for AI agents, using deterministic "policy as code" to control agent behavior in real-time and prevent them from taking unauthorized actions.
* **Truffle Security (TruffleHog)** focuses on secrets discovery (API keys, credentials) and, crucially, validates if those secrets are actually "live" and usable.
* **AI is increasing risk:** AI coding agents (like Cursor) are accelerating development but also inadvertently increasing the volume of leaked secrets in code repositories.
* **The "Human in the Loop" remains vital:** AI can hallucinate or cause damage; human oversight is required to manage the "chainsaw" of offensive security tools safely.
* **Shift in Security Ownership:** While secrets management is often handled by AppSec teams, it is increasingly becoming an Identity and Access Management (IAM) concern.

## New Tools, Techniques, and Tactics
* **Burp AI:** An AI-driven enhancement for Burp Suite designed to automate repetitive testing tasks and orchestrate complex vulnerability searches.
* **Sondera Agent Harness:** A control plane that "man-in-the-middles" an AI agent's trajectory to inspect and intercept tool calls before they execute.
* **Deterministic Controls (Policy as Code):** Using languages like **Cedar** to enforce hard rules on AI agents, rather than relying on non-deterministic LLM prompts.
* **Auto-Formalization:** A technique used by Sondera to turn natural language (like employee handbooks) into mathematical, enforceable security policies.
* **Secrets Validation:** A tactic where security tools don't just find a string that *looks* like a key, but actively test it (via API calls) to see if it is live and what permissions it holds.

## Detection & Defense Insights
* **Stateful Trajectory Monitoring:** For AI agents, security must look at the entire "path" of actions (stateful) rather than just individual turns to catch "context splitting" attacks.
* **Tainting the Trajectory:** A defensive method to track sensitive data (like PII) through an agent's entire session to ensure it isn't leaked to external tools later.
* **DAST vs. SAST:** Dynamic Analysis (DAST) is essential because many vulnerabilities (like cache poisoning or request smuggling) only appear when the application is running.
* **Secrets Scanning Locations:** High-signal areas for scanning include Code Repos (60-70%), Atlassian suites (Jira/Confluence), and Chat platforms (Slack/Teams).
* **Push Protection:** A defensive mechanism (offered by GitHub) that prevents secrets from being uploaded to a platform in the first place.

## Real-World Examples & Stories
* **The "James Kettle in a Box" Joke:** A discussion on whether AI will eventually automate the high-level research capabilities of elite security researchers.
* **Orange Cyberdefense Case Study:** A major pen-testing firm used Burp AI and saw testers work 2x to 5x faster, paying for the tool within a few engagements.
* **The "AI Assistant" Leak:** A mention of an incident where an AI-generated installer accidentally included a wildcard private key.
* **The "Cursor" Risk:** An example of how AI coding agents, acting with the user's local privileges, might "pillage" a home directory to find credentials to complete a task.

## Research, References & Resources
* **Burp Suite Pro & DAST:** Industry-standard tools for manual and automated web application security testing.
* **Cedar Policy Language:** A language used for writing fine-grained, verifiable access control policies.
* **TruffleHog:** A specialized tool for discovering and managing the lifecycle of leaked secrets.
* **Agent Scaffolds:** The frameworks (like LangGraph) that wrap LLMs to give them the ability to use tools and take actions.

## Key Industry Insights & Trends
* **AI as a Productivity Multiplier:** AI is currently viewed as an "accelerator" for humans rather than a replacement for skilled security professionals.
* **Increased Attack Surface:** Continuous deployment and AI-generated code are creating more code to test at a much faster rate than humans can keep up with.
* **The "Non-Deterministic" Problem:** Using an LLM to secure another LLM is seen as flawed; true security requires deterministic, code-based guardrails.
* **The Rise of Agentic Workflows:** Organizations are moving toward autonomous agents, which introduces "insider threat" risks on steroids.

## Business & Risk Implications
* **Operational Speed vs. Security:** CEOs may prioritize the 100x speed gains of AI agents while sidelining the security reviews necessary to manage them.
* **Financial & Reputational Risk:** Leaked "live" credentials can lead to massive data breaches, especially if the keys have high-level access to production databases.
* **Compliance Risk:** AI agents may inadvertently violate regulations like GDPR or the EU AI Act if they are not governed by strict, stateful policies.
* **Resource Allocation:** AppSec teams face increasing "cognitive load" trying to manage both manual testing and massive amounts of automated DAST findings.

## Opinions vs Facts
* **Fact:** Burp Suite is used by 80,000 professionals; AI features were launched in early 2025.
* **Fact:** GitHub provides "push protection" to prevent secrets from being uploaded.
* **Opinion:** AI will not be as devastating to skilled jobs as people fear; it will be a productivity booster.
* **Opinion/Prediction:** The "human tester" will not go away because of the need for accuracy and the danger of giving AI "chainsaw" tools.
* **Opinion:** Some CEOs are "hell-bent" on AI adoption and are actively sidelining security.

## Contradictions & Debates (if any)
* **The Role of AI in Security:** There is a debate over whether AI should be used to *perform* security testing (offensive) or to *govern* AI agents (defensive).
* **Security Ownership:** There is a tension between whether secrets management belongs to the AppSec team (legacy) or the Identity/IAM team (modern reality).
* **GitHub vs. Third-Party Scanners:** A debate exists regarding GitHub's "anti-competitive" practice of keeping push protection for itself while third-party tools handle the rest of the lifecycle.

## Actionable Takeaways
* **For CISOs:** Do not assume AI agents are safe just because they have "system prompts." Implement deterministic, policy-as-code controls to govern their actions.
* **For SOC/AppSec Teams:** Move beyond simple secret scanning. Ensure your tools validate if secrets are "live" and track their permissions to prioritize remediation.
* **For Security Leaders:** Integrate DAST into CI/CD pipelines to catch runtime vulnerabilities that static analysis (SAST) will miss.
* **For Engineering Leaders:** Be aware that AI coding tools (like Cursor) operate with user privileges; monitor for unexpected file system or credential access.
