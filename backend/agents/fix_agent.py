from agents.gemini_client import ask_gemini

def run_fix_agent(findings):

    prompt = f"""
You are a senior Solidity security engineer.

Generate fixes for the findings.

Findings:

{findings}

Return ONLY valid JSON.

Format:

{{
    "fixes": [
        {{
            "issue": "",
            "solution": "",
            "code_snippet": ""
        }}
    ]
}}

Do not return markdown.
Do not return code blocks.
Return JSON only.
"""

    return ask_gemini(prompt)