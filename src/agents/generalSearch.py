"""this file contains the general search function from the textbook"""

class Node:
    def __init__(self, parent, state, direction):
        self.p = parent
        self.s = state
        self.d = direction
    def expand(self, agent):
        newNodes = []
        successors = agent.getSuccessors(self.s)
        for s in successors:
            newNodes.append(Node(self, s[0], s[1]))
        return newNodes


def generalSearch(agent, queue_function, queue):
    visited = {}
    nodes = queue #the type of queue will depend on the search function
    done = False
    while True:
        if nodes.isEmpty():
            break
        node = nodes.pop()
        if agent.isGoalState(node.s):
            break
        if node.s not in visited:
            visited[node.s] = True
            queue_function(nodes, node.expand(agent), agent)

    return node
