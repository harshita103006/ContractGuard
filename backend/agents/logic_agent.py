from agents.gemini_client import ask_gemini

def run_logic_agent(contract):

    prompt = f"""
You are a smart contract logic auditor.

Analyze the contract for:

1. Business Logic Flaws
2. Incorrect Conditions
3. State Inconsistencies
4. Unexpected Behaviors
5. Edge Cases

Return ONLY valid JSON.

Format:

{{
    "issue": "",
    "severity": "",
    "explanation": ""
}}

If multiple issues exist:

{{
    "issues": [
        {{
            "issue": "",
            "severity": "",
            "explanation": ""
        }}
    ]
}}

Do not return markdown.
Do not return code blocks.
Return JSON only.

Contract:

{contract}
"""

    return ask_gemini(prompt)