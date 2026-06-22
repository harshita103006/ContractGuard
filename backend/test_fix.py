from agents.fix_agent import run_fix_agent

findings = """
Issue: Missing Access Control
Severity: High

Explanation:
Any user can call the admin function.
"""

print(run_fix_agent(findings))