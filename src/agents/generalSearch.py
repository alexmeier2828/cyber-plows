"""this file contains the general search function from the textbook"""

class Node:
    def __init__(self, parent, state, direction):
        self.p = parent
        self.s = state
        self.d = direction
    def expand(self, agent):
        agent.increaseNodeCount();
        newNodes = []
        successors = agent.getSuccessors(self.s)
        if successors is None:
            return []
        for s in successors:
            newNodes.append(Node(self, s[0], s[1]))
        return newNodes


#the graph search algorithm from the book
def generalSearch(agent, queue_function, queue):
    visited = {}
    nodes = queue #the type of queue will depend on the search function
    done = False
    while True:
        if len(queue) is 0:
            break
        node = nodes.pop()
        if agent.isGoalState(node.s):
            break
        if str(node.s) not in visited:
            visited[str(node.s)] = True
            queue_function(nodes, node.expand(agent), agent)

    return pathFromNode(node)



#converts a node tree into a sequence of directons
def pathFromNode(node):
    path = []
    head = node

    while head.d is not None:
        path.append(head.d)
        head = head.p

    path.reverse()
    return path
