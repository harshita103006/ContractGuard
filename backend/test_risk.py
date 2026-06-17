from agents.risk_agent import run_risk_agent

security = "Access control issue detected."
logic = "No major logic flaws."

print(
    run_risk_agent(
        security,
        logic
    )
)