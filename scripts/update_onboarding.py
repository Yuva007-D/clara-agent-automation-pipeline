import os
import json

onboard_folder = "../dataset/onboarding_calls"
accounts_folder = "../outputs/accounts"

files = sorted(os.listdir(onboard_folder))

for i, file in enumerate(files, start=1):

    account_id = f"account_{i}"

    # read onboarding transcript
    with open(os.path.join(onboard_folder, file), "r", encoding="utf-8") as f:
        text = f.read().lower()

    v1_memo_path = os.path.join(accounts_folder, account_id, "v1", "memo.json")

    with open(v1_memo_path, "r") as f:
        memo = json.load(f)

    old_hours = memo["business_hours"]

    # update based on onboarding
    if "8" in text and "6" in text:
        memo["business_hours"] = "8-6"

    if "dispatch" in text:
        memo["emergency_routing_rules"] = "dispatch"

    if "servicetrade" in text:
        memo["integration_constraints"] = "Do not create jobs automatically in ServiceTrade"

    # create v2 folder
    v2_folder = os.path.join(accounts_folder, account_id, "v2")
    os.makedirs(v2_folder, exist_ok=True)

    # save updated memo
    with open(os.path.join(v2_folder, "memo.json"), "w") as f:
        json.dump(memo, f, indent=4)

    # create agent spec v2
    agent_spec = {
        "agent_name": f"{account_id}_agent",
        "voice_style": "professional",
        "business_hours": memo["business_hours"],
        "services_supported": memo["services_supported"],
        "emergency_routing": memo["emergency_routing_rules"],
        "version": "v2"
    }

    with open(os.path.join(v2_folder, "agent_spec.json"), "w") as f:
        json.dump(agent_spec, f, indent=4)

    # create changelog
    with open(os.path.join(v2_folder, "changes.md"), "w") as f:
        f.write(f"business_hours: {old_hours} -> {memo['business_hours']}\n")
        f.write("emergency routing updated based on onboarding call\n")

    print(f"Updated {account_id} to v2")