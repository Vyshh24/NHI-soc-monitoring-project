# Project: Non-Human Identity (NHI) Monitoring in a SOC

**Objective:** Build a SOC-based detection system for monitoring non-human identities
(service accounts, simulated AI agents, automation scripts) for anomalous behavior.

**Scope:** 4 local Linux identities (2 service accounts, 1 simulated AI agent, 1 CI/CD bot)

**Tools:** Kali Linux (local lab), Splunk Free or ELK Stack, Python, draw.io

**Success Criteria:**
- Working log pipeline (auth.log/systemd → SIEM)
- 4 detection rules mapped to MITRE ATT&CK
- Risk scoring engine
- Dashboard
- Governance + incident response playbook
