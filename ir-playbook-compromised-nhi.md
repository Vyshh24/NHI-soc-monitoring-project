# Incident Response Playbook: Compromised/Misused Non-Human Identity

## Scenario
A service account (e.g., svc-backup) shows signs of misuse: repeated failed login attempts, unauthorized sudo/privilege escalation attempts, or activity outside its expected behavioral baseline.

## Reference Incident (from this project's testing)
On 2026-07-15, svc-backup generated 3 failed SSH login attempts and 1 failed sudo escalation attempt ("NOT in sudoers") within a single session window, flagged by Detection Rules 2 and 3, and confirmed via the risk scoring engine as HIGH risk (score: 55).

## Phase 1: Detection
- Trigger sources: Splunk alerts tied to Detection Rules 1-4 (off-schedule login, privilege escalation attempt, interactive login on non-interactive account, stale credential reactivation).
- Analyst confirms the alert is not a false positive by reviewing raw log entries in index=nhi_project.

## Phase 2: Triage
- Identify the NHI involved and cross-reference its entry in nhi-inventory.md (owner, intended purpose, expected behavior).
- Check the risk scoring engine output (risk_scorer.py) to confirm severity classification.
- Classify severity:
  - LOW: isolated failed login, no privilege escalation
  - MEDIUM: repeated failures or off-schedule activity
  - HIGH: privilege escalation attempt or interactive access to a non-interactive account (as seen with svc-backup)

## Phase 3: Containment
- Immediately disable the affected NHI's ability to authenticate:
  sudo usermod -L svc-backup
  sudo usermod -s /usr/sbin/nologin svc-backup
- Revoke any associated credentials/keys.
- Preserve evidence: export relevant Splunk events (index=nhi_project) covering the incident window before making further changes.

## Phase 4: Eradication
- Determine root cause: was the credential leaked, guessed, or was this a legitimate but misconfigured process?
- If credential compromise is confirmed, rotate credentials for any other NHI that may share infrastructure or trust relationships with the affected account.

## Phase 5: Recovery
- Re-provision the NHI with a new credential following the NHI Lifecycle Policy provisioning steps.
- Re-enable only after confirming least-privilege scope is correctly applied.
- Monitor closely (increased alert sensitivity) for 7 days following recovery.

## Phase 6: Lessons Learned
- Document: What baseline behavior should have prevented this sooner?
- Update detection rule thresholds if the incident revealed a gap.
- Update nhi-inventory.md with any scope/ownership changes.

---
Playbook Version: 1.0
Reference Case: svc-backup incident, 2026-07-15
