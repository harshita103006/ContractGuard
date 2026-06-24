from agents.gemini_client import ask_gemini

def run_security_agent(contract):

    prompt = f"""
You are a senior blockchain security auditor.

Analyze the Solidity smart contract.

Check for:

1. Reentrancy
2. Access Control Issues
3. Integer Overflow / Underflow
4. Unsafe External Calls
5. Denial of Service Risks

Return ONLY valid JSON.

Format:

{{
    "issue": "",
    "severity": "",
    "explanation": ""
}}

If multiple issues exist, return:

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