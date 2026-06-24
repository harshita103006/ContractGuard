from graph.workflow import graph

contract = """
contract Test {

    uint public count;

    function increment() public {
        count++;
    }
}
"""

result = graph.invoke(
    {
        "contract": contract
    }
)

print(result)