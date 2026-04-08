---
title: "Joshua Saxe - The Hard Part Isn’t Building the Agent: Measuring Effectiveness | [un]prompted 2026"
date: 2026-03-25T06:23:46-07:00
draft: false
channel: "unprompted"
channel_slug: "unprompted"
category: "cybersecurity"
youtube_url: "https://www.youtube.com/watch?v=rO2yA52U_i4"
video_id: "rO2yA52U_i4"
thumbnail: "https://i.ytimg.com/vi/rO2yA52U_i4/sddefault.jpg"
description: "AI-generated summary of Joshua Saxe - The Hard Part Isn’t Building the Agent: Measuring Effectiveness | [un]prompted 2026 from unprompted"
tags: ["cybersecurity"]
hook: "Your AI defense is likely guessing correctly, but you have no way of knowing if it's actually thinking."
stings:
  - "The death of the 'perfect truth'"
  - "Auditing the agent's soul"
  - "Beyond the binary trap"
card_topic: "AI+Defense+Metrics"
topic_count: 6
---

## TL;DR (Too Long, Didn't Read)
*   **The Problem:** Attackers are shifting from manual labor to managing AI agents, meaning defenders must also deploy autonomous AI agents to keep up.
*   **The Barrier:** We cannot trust current AI defense systems because we don't know how to measure if they are actually working or just "guessing" correctly.
*   **The Flaw in Current Metrics:** Standard metrics like Precision, Recall, and F1 scores assume a "perfect truth" (an Oracle) exists, but in cybersecurity, human experts often disagree on what is actually "true."
*   **The Solution:** Stop treating AI like a simple classifier (cat vs. dog) and start treating it like a human employee. Evaluate their *reasoning process*, not just their final answer.
*   **New Approach:** Use "Interview Protocols" (rubrics) to grade how an agent gathers evidence, understands policy, and justifies its decisions.
*   **Scaling Evaluation:** Since humans can't grade every AI action, use a second "LLM Judge" trained on a specific rubric to automate the review of agent behaviors.

## New Tools, Techniques, and Tactics
*   **Holistic Rubric-Based Evaluation:** Moving away from binary (yes/no) outcomes to grading multiple dimensions like evidence gathering and policy understanding.
*   **Agent Trajectory Grading:** Analyzing the entire "path" or sequence of steps an AI takes to reach a conclusion, rather than just the final result.
*   **LLM-as-a-Judge:** Using a highly capable LLM to act as an automated auditor, grading the performance of other AI agents based on a predefined rubric.
*   **Hill Climbing:** An iterative process where teams use evaluation data to constantly tweak prompts and architectures to improve specific rubric scores.
*   **Automated Architecture Optimization:** Using AI coding tools and genetic algorithms to automatically improve agent workflows based on evaluation feedback.

## Detection & Defense Insights
*   **Beyond Binary Signals:** SOC teams should stop looking only at whether an alert was "True" or "False" and start looking at the *quality of the investigation* performed by the agent.
*   **Monitoring for "Drift":** Once an autonomous agent is deployed, continuous monitoring is required to ensure its reasoning hasn't "gone off the rails" in production.
*   **The Noise Ceiling:** Recognize that because human labels are noisy (analysts disagree), there is a mathematical limit to how much you can improve a model using traditional supervised learning.
*   **Evidence-Based Defense:** Defensive agents must be required to output "auditable" logs that show exactly which pieces of evidence led to a sensitive action (like quarantining a server).

## Real-World Examples & Stories
*   **The Disagreeing Analyst:** The speaker noted that in SOC environments, there is often a double-digit disagreement rate between human analysts on whether an alert is worth investigating.
*   **The "Bad Lunch" Scenario:** A reminder that "ground truth" labels are often unreliable because they are created by humans who might be tired, distracted, or simply have a different opinion.
*   **The Hospital Use Case:** A practical example of why autonomy is needed: a hospital with only two IT staff cannot manually defend a massive, complex threat surface.
*   **The Simulation:** The speaker shared a simulation showing that even a tiny amount of noise (1% error) in your training data can make it impossible to tell if your AI is actually getting better.

## Research, References & Resources
*   **Mechanistic Interpretability:** Mentioned as a theoretical (but difficult) way to understand neural networks by looking at their internal weights.
*   **Classical ML Metrics:** Reference to Precision, Recall, F1, ROC curves, and the "Halting Problem" in computer science.
*   **Bayesian Modeling:** Suggested as a way to handle uncertainty and weight different human opinions based on how much they agree.

## Key Industry Insights & Trends
*   **Shift in Attacker Behavior:** We are moving from an era of manual hackers to an era of "AI Agent Managers" who scale attacks using autonomous tools.
*   **The "Vibes" Dystopia:** Many current AI security teams are operating without any formal evaluation, relying on "vibes" (engineers saying "it works on my machine"), which is dangerous for production.
*   **The Autonomy Mandate:** Organizations (especially SMBs and critical infrastructure like hospitals) will soon be forced to trust AI with sensitive actions like patching code or shutting down hosts.

## Business & Risk Implications
*   **Operational Risk:** Deploying unverified autonomous agents carries the risk of "breaking prod" (e.g., an AI accidentally shutting down a critical production server).
*   **Staffing Realities:** As cyber attacks scale via AI, the talent gap will widen, making autonomous defenders a business necessity rather than a luxury.
*   **The Cost of Rigor:** Building a proper evaluation program is expensive—it can take up 50% of a team's time—but it allows the team to move 10x faster in the long run.
*   **Reputational/Financial Risk:** Decisions made by AI regarding access management or incident response must be justifiable to leadership and regulators.

## Opinions vs Facts
*   **Fact:** Human analysts frequently disagree on security alerts (double-digit disagreement rates).
*   **Fact:** Traditional ML metrics assume a "ground truth" that does not exist in the messy reality of cybersecurity.
*   **Opinion/Prediction:** Attackers will soon transition from manual laborers to managers of AI agents.
*   **Opinion/Prediction:** We will eventually become comfortable letting AI make high-stakes decisions like quarantining a CTO's account.

## Contradictions & Debates (if any)
*   **Mechanistic Interpretability vs. Statistical Evaluation:** There is a debate on whether we should try to understand the "brain" of the AI (weights/matrices) or simply judge its behavior (statistical/behavioral). The speaker argues the latter is the only practical path.
*   **The "Oracle" Problem:** There is a tension between the mathematical need for "perfect labels" and the cybersecurity reality that "truth" is often subjective and noisy.

## Actionable Takeaways
*   **For CISOs:** Do not approve the deployment of autonomous AI agents based solely on "Accuracy" or "F1" scores. Demand to see the *reasoning rubrics* used to test them.
*   **For SOC Leaders:** Start building "Interview Protocols" for your AI tools. Define what "good investigation" looks like (e.g., did it check the logs? did it verify the user's identity?).
*   **For Security Engineers:** Invest heavily in "Evaluation Engineering." Spend the time now to build LLM-based judges and automated grading systems so you can ship with confidence.
*   **For AI Developers:** Move away from "binary" testing. Build systems that provide clear, auditable justifications for every decision they make.
