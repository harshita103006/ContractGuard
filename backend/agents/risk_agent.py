from agents.gemini_client import ask_gemini

def run_risk_agent(security_report, logic_report):

    prompt = f"""
You are the Risk Assessment Agent.

Security Report:
{security_report}

Logic Report:
{logic_report}

Provide:

Overall Risk:
Confidence:
Summary:
"""
    
    return ask_gemini(prompt)