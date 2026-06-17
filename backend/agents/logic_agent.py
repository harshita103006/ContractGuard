from agents.gemini_client import ask_gemini

def run_logic_agent(contract):

    prompt = f"""
You are a smart contract logic auditor.

Analyze the contract for:

1. Business logic flaws
2. Incorrect conditions
3. State inconsistencies
4. Unexpected behaviors
5. Edge cases

Return:

Issue:
Severity:
Explanation:

Contract:
{contract}
"""

    return ask_gemini(prompt)