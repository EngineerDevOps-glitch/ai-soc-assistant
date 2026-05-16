with open("alerts/auth-log-sample.txt", "r") as file:
    log_data = file.read()

print("===== AUTH LOG SAMPLE =====")
print(log_data)

print("\n===== SOC ANALYSIS =====")

risk_level = "Low"
findings = []

if "authentication failure" in log_data.lower():
    findings.append("Authentication failure activity detected.")
    risk_level = "Medium"

if "failed password" in log_data.lower():
    findings.append("Failed password attempts detected.")
    risk_level = "Medium"

if "invalid user" in log_data.lower():
    findings.append("Login attempt using an invalid username detected.")
    risk_level = "Medium"

if "sudo" in log_data.lower():
    findings.append("Sudo/admin activity detected. Review for authorized use.")

if findings:
    for finding in findings:
        print(f"- {finding}")
else:
    print("- No major suspicious authentication activity detected.")

print(f"\nRisk Level: {risk_level}")

print("\nRecommended Investigation Steps:")
print("- Review usernames involved in failed logins")
print("- Check source IP addresses if SSH is involved")
print("- Confirm whether sudo activity was authorized")
print("- Look for repeated failures over a short time window")
print("- Consider account lockout or firewall rules if brute force is suspected")
