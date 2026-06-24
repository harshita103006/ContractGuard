from typing import TypedDict

from langgraph.graph import StateGraph, END

from agents.security_agent import run_security_agent
from agents.logic_agent import run_logic_agent
from agents.risk_agent import run_risk_agent
from agents.fix_agent import run_fix_agent


class AuditState(TypedDict):
    contract: str
    security: str
    logic: str
    risk: str
    fixes: str

def security_node(state):

    security_report = run_security_agent(
        state["contract"]
    )

    return {
        "security": security_report
    }

def logic_node(state):

    logic_report = run_logic_agent(
        state["contract"]
    )

    return {
        "logic": logic_report
    }

def risk_node(state):

    risk_report = run_risk_agent(
        state["security"],
        state["logic"]
    )

    return {
        "risk": risk_report
    }

def fix_node(state):

    findings = f"""
Security Findings:

{state['security']}

Logic Findings:

{state['logic']}
"""

    fix_report = run_fix_agent(
        findings
    )

    return {
        "fixes": fix_report
    }

builder = StateGraph(AuditState)

builder.add_node(
    "security",
    security_node
)

builder.add_node(
    "logic",
    logic_node
)

builder.add_node(
    "risk",
    risk_node
)

builder.add_node(
    "fix",
    fix_node
)

builder.set_entry_point(
    "security"
)

builder.add_edge(
    "security",
    "logic"
)

builder.add_edge(
    "logic",
    "risk"
)

builder.add_edge(
    "risk",
    "fix"
)

builder.add_edge(
    "fix",
    END
)

graph = builder.compile()

