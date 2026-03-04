from flask import Flask, render_template
import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs", "accounts")

app = Flask(__name__, template_folder=TEMPLATE_DIR)

BASE_FOLDER = OUTPUT_DIR

def load_accounts():
    accounts = []

    for account in os.listdir(BASE_FOLDER):
        account_data = {"name": account, "v1": None, "v2": None, "changes": None}

        v1_path = os.path.join(BASE_FOLDER, account, "v1", "memo.json")
        v2_path = os.path.join(BASE_FOLDER, account, "v2", "memo.json")
        changes_path = os.path.join(BASE_FOLDER, account, "v2", "changes.md")

        if os.path.exists(v1_path):
            with open(v1_path) as f:
                account_data["v1"] = json.load(f)

        if os.path.exists(v2_path):
            with open(v2_path) as f:
                account_data["v2"] = json.load(f)

        if os.path.exists(changes_path):
            with open(changes_path) as f:
                account_data["changes"] = f.read()

        accounts.append(account_data)

    return accounts

@app.route("/")
def index():
    accounts = load_accounts()
    return render_template("index.html", accounts=accounts)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)