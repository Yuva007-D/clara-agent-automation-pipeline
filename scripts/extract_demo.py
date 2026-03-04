import os
import json

# Folder paths
demo_folder = "../dataset/demo_calls"
output_folder = "../outputs/accounts"

# Get all demo files
files = sorted(os.listdir(demo_folder))

for i, file in enumerate(files, start=1):

    # Read transcript
    with open(os.path.join(demo_folder, file), "r", encoding="utf-8") as f:
        text = f.read().lower()

    account_id = f"account_{i}"

    # Account Memo structure
    memo = {
        "account_id": account_id,
        "company_name": "",
        "business_hours": "",
        "office_address": "",
        "services_supported": [],
        "emergency_definition": [],
        "emergency_routing_rules": "",
        "non_emergency_routing_rules": "",
        "call_transfer_rules": "",
        "integration_constraints": "",
        "after_hours_flow_summary": "",
        "office_hours_flow_summary": "",
        "questions_or_unknowns": [],
        "notes": ""
    }

    # Simple extraction rules
    if "electric" in text:
        memo["services_supported"].append("electrical services")

    if "sprinkler" in text:
        memo["services_supported"].append("sprinkler services")

    if "fire alarm" in text:
        memo["services_supported"].append("fire alarm services")

    if "9" in text and "5" in text:
        memo["business_hours"] = "9-5"

    if memo["business_hours"] == "":
        memo["questions_or_unknowns"].append("business_hours")

    # Create account folder
    account_folder = os.path.join(output_folder, account_id, "v1")
    os.makedirs(account_folder, exist_ok=True)

    # Save memo JSON
    output_file = os.path.join(account_folder, "memo.json")

    with open(output_file, "w") as f:
        json.dump(memo, f, indent=4)

    print(f"Created memo for {account_id}")