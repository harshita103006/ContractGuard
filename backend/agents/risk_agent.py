from agents.gemini_client import ask_gemini

def run_risk_agent(security_report, logic_report):

    prompt = f"""
You are a blockchain risk assessment expert.

Security Findings:

{security_report}

Logic Findings:

{logic_report}

Return ONLY valid JSON.

Format:

{{
    "overall_risk": "",
    "confidence": "",
    "summary": ""
}}

Do not return markdown.
Do not return code blocks.
Return JSON only.
"""

    return ask_gemini(prompt)