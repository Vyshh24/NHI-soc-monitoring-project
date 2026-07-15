import datetime

# Manually input data collected from Splunk
identities = [
    {"name": "svc-backup", "type": "service_account", "failed_logins": 3, "sudo_violations": 1, "privilege": "low"},
    {"name": "svc-reporting", "type": "service_account", "failed_logins": 0, "sudo_violations": 0, "privilege": "low"},
    {"name": "ai-agent-bot", "type": "ai_agent", "failed_logins": 0, "sudo_violations": 0, "privilege": "medium"},
    {"name": "ci-deploy-bot", "type": "ci_cd_bot", "failed_logins": 0, "sudo_violations": 0, "privilege": "medium"},
]

def calculate_risk(identity):
    score = 0
    score += identity["failed_logins"] * 10
    score += identity["sudo_violations"] * 25
    if identity["privilege"] == "high":
        score += 20
    elif identity["privilege"] == "medium":
        score += 10
    return score

def risk_level(score):
    if score >= 50:
        return "HIGH"
    elif score >= 20:
        return "MEDIUM"
    else:
        return "LOW"

print(f"{'Identity':<15} {'Type':<15} {'Score':<8} {'Risk Level'}")
print("-" * 50)

results = []
for identity in identities:
    score = calculate_risk(identity)
    level = risk_level(score)
    results.append((identity["name"], identity["type"], score, level))

results.sort(key=lambda x: x[2], reverse=True)

for name, itype, score, level in results:
    print(f"{name:<15} {itype:<15} {score:<8} {level}")
