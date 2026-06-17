from agents.security_agent import run_security_agent

contract = """
contract Test {
    uint public count;

    function increment() public {
        count++;
    }
}
"""

print(
    run_security_agent(contract)
)