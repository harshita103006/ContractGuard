from agents.gemini_client import ask_gemini

def run_security_agent(contract):

    prompt = f"""
You are a blockchain security expert.

Analyze the Solidity contract.

Check:
- Reentrancy
- Access Control
- Integer Overflow
- Unsafe Calls

Return:

Issue:
Severity:
Explanation:

Contract:
{contract}
"""

    return ask_gemini(prompt)