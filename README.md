# NHI SOC Monitoring Project

A SOC-based detection project for monitoring Non-Human Identities (NHI) — service accounts, simulated AI agents, and automation scripts — for anomalous behavior, built as part of my EC-Council SOC Analyst (CSA) certification.

## Objective
Traditional SOCs are built to monitor human logins, but modern environments are dominated by machine identities: service accounts, API keys, CI/CD bots, and now autonomous AI agents. This project builds a detection pipeline specifically for these often-overlooked identities.

## Scope
- 2 local Linux service accounts (svc-backup, svc-reporting)
- 1 simulated AI agent (ai-agent-bot)
- 1 simulated CI/CD identity (ci-deploy-bot)

## Tools & Stack
- Kali Linux — local lab environment
- Splunk Free — SIEM for log ingestion, correlation, and dashboards
- Python — risk scoring engine
- MITRE ATT&CK — detection mapping framework

## Detection Rules (4 core rules, MITRE-mapped)
| # | Rule | MITRE ATT&CK |
|---|---|---|
| 1 | Off-schedule NHI login | T1078.004 |
| 2 | Service account privilege escalation attempt | T1548.003 |
| 3 | Interactive login on non-interactive service account | T1078.003 |
| 4 | Stale credential reactivation | T1078 |

## Dashboards
- NHI Activity Summary — per-identity violation counts
- NHI vs Human Activity — activity split visualization
- Suspicious Activity Over Time — timeline of flagged events

## Risk Scoring Engine
Python script (`risk_scorer.py`) that calculates a weighted risk score per identity based on failed logins, sudo violations, and privilege level. Successfully identified `svc-backup` as HIGH risk based on real triggered detection data.

## Repo Structure
- nhi-inventory.md — inventory of all monitored identities
- project-scope.md — project objective, scope, and success criteria
- risk_scorer.py — risk scoring engine

## Project Phases & Status
1. Identity inventory & baseline — Done
2. Log ingestion pipeline (auth.log to Splunk) — Done
3. Detection engineering (4 core rules) — Done
4. Risk scoring engine — Done
5. Dashboard & visualization — Done
6. Governance policy & incident response playbook — In progress
7. Final report packaging — Not started

## Status
In progress — Day 6: Governance & Incident Response Playbook

