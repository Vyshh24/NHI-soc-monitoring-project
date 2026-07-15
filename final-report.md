# Non-Human Identity (NHI) Monitoring in a SOC
### Final Project Report — EC-Council SOC Analyst (CSA) Certification

**Author:** Vyshh
**Project Duration:** 2 weeks (compressed timeline)
**Environment:** Fully local lab (Kali Linux)
**Repository:** https://github.com/Vyshh24/NHI-soc-monitoring-project

---

## 1. Executive Summary

Traditional Security Operations Centers were built around monitoring human logins, but modern IT environments are increasingly dominated by machine identities: service accounts, API keys, CI/CD pipeline bots, and now autonomous AI agents acting without direct human oversight. Industry trends into 2026 show security teams actively rethinking identity management to account for these non-human identities (NHIs), which often carry excessive standing privileges, lack MFA, and are rarely reviewed.

This project builds a working, end-to-end NHI monitoring capability inside a self-contained SOC lab: identity inventory, log ingestion, detection engineering, risk scoring, visualization, and governance, entirely using free, local tools, at zero cost.

## 2. Objective

Build a SOC-based detection system capable of identifying anomalous behavior across non-human identities, specifically:
- Off-schedule or unusual activity
- Unauthorized privilege escalation attempts
- Interactive access on identities meant to be non-interactive
- Stale credential reactivation

## 3. Environment & Architecture

Lab setup: Fully local, no cloud dependency, zero cost, zero billing risk.

Architecture flow: Linux Identities -> auth.log (via rsyslog) -> Splunk (index=nhi_project) -> Detection Rules + Risk Scoring -> Dashboards + Alerts

Tools used:
- Kali Linux: lab host, identity creation, log generation
- rsyslog: traditional syslog file generation (auth.log)
- Splunk Free: SIEM (log ingestion, search, dashboards)
- Python: risk scoring engine
- MITRE ATT&CK: detection-to-technique mapping
- Git/GitHub: version control and documentation

## 4. NHI Inventory

| Identity Name | Type | Access | Purpose |
|---|---|---|---|
| svc-backup | Local service account | No login | Simulated backup service |
| svc-reporting | Local service account | No login | Simulated reporting service |
| ai-agent-bot | Simulated AI agent | Bash shell | Runs scheduled API-calling script |
| ci-deploy-bot | CI/CD-style identity | Bash shell | Simulated deployment automation |

Full detail: nhi-inventory.md

## 5. Detection Engineering

Four core detection rules were designed, implemented as Splunk SPL queries, and validated against real triggered log events generated during lab testing.

| # | Rule | Status | MITRE ATT&CK |
|---|---|---|---|
| 1 | Off-schedule NHI login | Logic validated | T1078.004 |
| 2 | Service account privilege escalation attempt | Triggered with real event | T1548.003 |
| 3 | Interactive login on non-interactive service account | Triggered with real event | T1078.003 |
| 4 | Stale credential reactivation | Logic and calculation validated | T1078 |

Reference Incident: On 2026-07-15, svc-backup generated 3 failed SSH login attempts and 1 failed sudo escalation attempt within a single testing window, successfully detected by Rules 2 and 3, and confirmed by the risk scoring engine as HIGH risk.

Sample detection query (Rule 2, privilege escalation):
index=nhi_project sourcetype=linux_secure "NOT in sudoers" | table _time, _raw

## 6. Risk Scoring Engine

A Python-based scoring engine (risk_scorer.py) calculates a weighted risk score per identity based on failed logins, sudo violations, and privilege level.

Results:
| Identity | Type | Score | Risk Level |
|---|---|---|---|
| svc-backup | service_account | 55 | HIGH |
| ai-agent-bot | ai_agent | 10 | LOW |
| ci-deploy-bot | ci_cd_bot | 10 | LOW |
| svc-reporting | service_account | 0-25 | LOW/MEDIUM |

The engine correctly surfaced svc-backup as the highest-priority identity, matching the real detection evidence gathered during testing.

Full code: risk_scorer.py

## 7. Dashboards & Visualization

Three Splunk dashboards were built to operationalize this data for SOC analyst use:

1. NHI Activity Summary: per-identity table of failed logins, sudo violations, and last-seen timestamps
2. NHI vs Human Activity: pie chart comparing NHI activity volume to human baseline activity
3. Suspicious Activity Over Time: timeline chart showing a clear activity spike during the incident window

## 8. Governance & Incident Response

Two governance documents were produced to address the operational and process side of NHI security, beyond detection alone:

- nhi-lifecycle-policy.md: covers provisioning, credential rotation (90-day cadence), monitoring, and deprovisioning requirements for all NHIs
- ir-playbook-compromised-nhi.md: a 6-phase incident response playbook (Detection, Triage, Containment, Eradication, Recovery, Lessons Learned), built around the real svc-backup incident captured during this project

## 9. Lessons Learned

- Splunk's default field extraction for linux_secure does not reliably populate a consistent user field across all auth.log line formats. This required manually tagging identities via eval case(match(...)) logic.
- Failed authentication and authorization attempts proved to be valuable, realistic detection test cases. A compromise attempt does not need to succeed to generate meaningful telemetry.
- A fully local lab proved sufficient to demonstrate the full NHI monitoring lifecycle at zero cost.

## 10. Future Work

- Extend detection coverage to cloud-based NHIs (AWS IAM/CloudTrail or Azure Entra ID)
- Automate the risk scoring engine to pull live data directly from Splunk's REST API
- Integrate a lightweight SOAR-style automated response for HIGH risk classifications
- Extend the 30-day stale credential detection with real longitudinal data

## 11. Conclusion

This project delivered a complete, functioning NHI monitoring capability, from identity inventory through detection, risk scoring, visualization, and governance, entirely on free, local infrastructure. The detection rules were validated against real, self-generated attack-pattern log data, and the risk scoring engine correctly prioritized the genuinely anomalous identity.

---
Built as part of EC-Council SOC Analyst (CSA) certification coursework, July 2026.
