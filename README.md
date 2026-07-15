# NHI SOC Monitoring Project

A SOC-based detection project for monitoring **Non-Human Identities (NHI)** — service accounts, simulated AI agents, and automation scripts — for anomalous behavior, built as part of my EC-Council SOC Analyst (CSA) certification.

## Objective
Traditional SOCs are built to monitor human logins, but modern environments are dominated by machine identities: service accounts, API keys, CI/CD bots, and now autonomous AI agents. This project builds a detection pipeline specifically for these often-overlooked identities.

## Scope
- 2 local Linux service accounts (svc-backup, svc-reporting)
- 1 simulated AI agent (ai-agent-bot)
- 1 simulated CI/CD identity (ci-deploy-bot)

## Tools & Stack
- Kali Linux — local lab environment
- Splunk Free — SIEM for log ingestion, correlation, and dashboards
- Python — simulated AI agent scripting + risk scoring engine
- MITRE ATT&CK — detection mapping framework

## Project Phases
1. Identity inventory & baseline
2. Log ingestion pipeline (auth.log, systemd)
3. Detection engineering (4 core rules, MITRE-mapped)
4. Risk scoring engine
5. Dashboard & visualization
6. Governance policy & incident response playbook

## Repo Structure
- nhi-inventory.md — inventory of all monitored identities
- project-scope.md — project objective, scope, and success criteria
- (more files added as project progresses)

## Status
In progress — Day 2: SIEM setup

---


