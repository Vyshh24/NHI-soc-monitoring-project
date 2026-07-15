# Non-Human Identity (NHI) Lifecycle Policy

## Purpose
This policy defines how non-human identities (service accounts, simulated AI agents, and automation identities) are provisioned, maintained, and deprovisioned within this SOC lab environment, to minimize the attack surface presented by machine identities.

## Scope
Applies to all NHIs in this project: svc-backup, svc-reporting, ai-agent-bot, ci-deploy-bot.

## 1. Provisioning
- Every NHI must be created with the minimum privilege required for its function (least privilege principle).
- Service accounts with no interactive purpose must be created with a non-login shell (/usr/sbin/nologin).
- Every NHI must be logged in the NHI inventory (nhi-inventory.md) at creation time, including: name, type, owner/purpose, and intended access scope.
- No NHI should be created with administrative/sudo privileges by default.

## 2. Credential Management
- Credentials (passwords, keys) must not be shared across multiple NHIs.
- Interactive-capable NHIs (e.g., ai-agent-bot, ci-deploy-bot) should use key-based authentication where possible, rather than static passwords.
- Credential rotation cadence: every 90 days for all active NHIs.
- Any credential unused for 30+ days should be flagged for review (see Detection Rule 4: stale credential reactivation).

## 3. Monitoring & Review
- All NHI activity is logged via /var/log/auth.log and ingested into Splunk (index=nhi_project).
- Quarterly access reviews should confirm each NHI still requires its current permissions ("privilege creep" check).
- Any sudo/privilege escalation attempt by an NHI not explicitly authorized for elevated access must trigger an alert (see Detection Rule 2).

## 4. Deprovisioning
- NHIs must be disabled or removed immediately when:
  - The associated project/service is decommissioned
  - The NHI is no longer in active use
  - A compromise is suspected or confirmed
- Deprovisioning steps: disable login (usermod -L or set shell to nologin), revoke any associated keys/credentials, remove from active inventory, retain audit logs per retention policy.

## 5. Ownership & Accountability
- Every NHI must have a documented owner (a human or team responsible for its purpose and behavior).
- Owners are responsible for requesting rotation, reviewing alerts tied to their NHI, and approving deprovisioning.

---
Policy Version: 1.0
Last Updated: 2026-07-15
