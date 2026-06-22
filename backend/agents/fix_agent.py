from agents.gemini_client import ask_gemini

def run_fix_agent(findings):

    prompt = f"""
You are a senior Solidity security engineer.

Generate fixes for the following findings.

For each issue provide:

Issue:
Fix:
Code Snippet:

Findings:
{findings}
"""

    return ask_gemini(prompt)