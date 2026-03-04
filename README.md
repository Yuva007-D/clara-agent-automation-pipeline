# Clara Agent Automation Pipeline

## Overview

This project builds a zero-cost automation pipeline that converts demo call transcripts and onboarding call transcripts into structured configurations for a Retell AI voice agent.

The pipeline processes demo calls to generate an initial agent configuration (v1) and updates the configuration after onboarding calls to produce version 2 (v2) with a changelog.

---

## Architecture

Pipeline A (Demo → v1)

Demo Transcript  
↓  
Extract structured data  
↓  
Generate Account Memo JSON  
↓  
Generate Retell Agent Spec  

Pipeline B (Onboarding → v2)

Onboarding Transcript  
↓  
Update Account Memo  
↓  
Generate Updated Agent Spec  
↓  
Create Changelog  

---

## Project Structure
dataset/
    demo_calls/
        demo1.txt
        demo2.txt
        demo3.txt
        demo4.txt
        demo5.txt

    onboarding_calls/
        onboard1.txt
        onboard2.txt
        onboard3.txt
        onboard4.txt
        onboard5.txt

scripts/
    extract_demo.py
    generate_agent.py
    update_onboarding.py

outputs/
    accounts/
        account_1/
            v1/
            v2/
        account_2/
        account_3/
        account_4/
        account_5/

---

## How to Run the Pipeline

1. Open the project folder in VS Code or terminal.

2. Place demo transcripts inside:

dataset/demo_calls/

3. Place onboarding transcripts inside:

dataset/onboarding_calls/

4. Run the scripts:

cd scripts
python extract_demo.py
python generate_agent.py
python update_onboarding.py


---

## Outputs

For each account the pipeline generates:

- Account Memo JSON
- Retell Agent Draft Specification
- Versioned configuration (v1 → v2)
- Changelog describing updates

Example output:

outputs/accounts/account_1/

v1/
    memo.json
    agent_spec.json

v2/
    memo.json
    agent_spec.json
    changes.md

---

## Design Decisions

- Used rule-based extraction to keep the system zero-cost
- Stored outputs in structured JSON files
- Implemented versioning with v1 and v2 folders
- Generated changelog for onboarding updates
- Designed the pipeline to be repeatable and easy to run

---

## Future Improvements

- Use local LLM for more accurate extraction
- Integrate with Retell API for automatic agent creation
- Add a simple dashboard for reviewing account configurations
- Implement better transcript parsing


