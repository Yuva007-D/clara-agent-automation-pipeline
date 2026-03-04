import os
import json

accounts_folder = "../outputs/accounts"

for account in os.listdir(accounts_folder):

    v1_path = os.path.join(accounts_folder, account, "v1")
    memo_file = os.path.join(v1_path, "memo.json")

    if not os.path.exists(memo_file):
        continue

    with open(memo_file, "r") as f:
        memo = json.load(f)

    # Build system prompt using memo data
    system_prompt = f"""
You are an AI receptionist for {memo.get('company_name','the company')}.

Business Hours: {memo.get('business_hours','unknown')}.

During business hours:
- Greet the caller politely
- Ask the reason for the call
- Collect the caller's name and phone number
- Route or transfer the call appropriately
- If transfer fails, apologize and take a message

After hours:
- Greet the caller
- Ask if this is an emergency
- If emergency, collect name, phone number, and address immediately
- Attempt transfer to the emergency contact
- If transfer fails, apologize and promise a quick follow-up
- If non-emergency, collect details and inform them the office will respond during business hours
"""

    agent_spec = {
        "agent_name": f"{account}_agent",
        "voice_style": "professional",
        "timezone": "unknown",
        "business_hours": memo.get("business_hours", ""),
        "services_supported": memo.get("services_supported", []),
        "system_prompt": system_prompt.strip(),
        "call_transfer_protocol": "Transfer call to technician or dispatch based on emergency status",
        "fallback_protocol": "If transfer fails, collect caller details and promise follow-up",
        "version": "v1"
    }

    agent_file = os.path.join(v1_path, "agent_spec.json")

    with open(agent_file, "w") as f:
        json.dump(agent_spec, f, indent=4)

    print(f"Created agent_spec for {account}")