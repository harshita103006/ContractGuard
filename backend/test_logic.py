from agents.logic_agent import run_logic_agent

contract = """
contract Test {

    uint public count;

    function increment() public {
        count++;
    }
}
"""

print(run_logic_agent(contract))