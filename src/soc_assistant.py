with open("alerts/auth-log-sample.txt", "r") as file:
    log_data = file.read()

log_lower = log_data.lower()

failed_password_count = log_lower.count("failed password")
authentication_failure_count = log_lower.count("authentication failure")
invalid_user_count = log_lower.count("invalid user")
sudo_count = log_lower.count("sudo")

risk_score = 0
findings = []

if failed_password_count > 0:
    findings.append(f"Failed password attempts detected: {failed_password_count}")
    risk_score += failed_password_count * 2

if authentication_failure_count > 0:
    findings.append(f"Authentication failures detected: {authentication_failure_count}")
    risk_score += authentication_failure_count * 2

if invalid_user_count > 0:
    findings.append(f"Invalid username attempts detected: {invalid_user_count}")
    risk_score += invalid_user_count * 3

if sudo_count > 0:
    findings.append(f"Sudo/admin activity detected: {sudo_count}")
    risk_score += sudo_count

if risk_score >= 15:
    risk_level = "High"
elif risk_score >= 5:
    risk_level = "Medium"
else:
    risk_level = "Low"

print("===== AI SOC ASSISTANT REPORT =====")
print("")
print(f"Risk Score: {risk_score}")
print(f"Risk Level: {risk_level}")
print("")

print("Findings:")
if findings:
    for finding in findings:
        print(f"- {finding}")
else:
    print("- No suspicious authentication activity detected.")

print("")
print("Recommended Investigation Steps:")
print("- Review failed login usernames")
print("- Check whether invalid usernames were attempted")
print("- Review sudo/admin activity for legitimacy")
print("- Look for repeated failures in a short time window")
print("- If external SSH attempts are found, consider firewall blocking")
