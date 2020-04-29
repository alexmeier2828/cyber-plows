"""
this file is a base class for all agent classes and should not be instantiated

"""
from generalSearch import *
from agentState import AgentState
from util import toVector

class  Agent:
    def __init__(self, gameState):
        #stuff that is common to all agents goes here
        self.startState = agentState(gameState)
        self.mapGraph = gameState.mapGraph
        raise NotImplementedError


    """ tion, so dont try to
        stick an implementation here.  Instead, implement a
        child class like "class newAgent(agent):". You can
        overload whichever functions you need, though this
        class provides the basics.
    """
    def generatePath(self, state):
        #this is where the algorithm should be called
        raise NotImplementedError

    def isGoalState(self, state):
        #checks if goal state is reached
        for row in state.snow:
            if row.contains(True):
                return false
            else:
                return true

    #takes an AgentState
    def getSuccessors(self, state):
        #returns a list of successor states
        startPoint = state.location
        successorNodes = self.mapGraph(startPoint)
        successors = []
        for node in successorNodes:
            copy = deepcopy(state)
            direction, length = toVector(startPoint, node)

            #state updates itself
            copy.driveTo(node)

            #add successor to list
            successors.append((copy, direction))
        #should return (state, direction) pair
        return successors


class dfsAgent(Agent):
    def __init__(self, startState):
        super().__init__(startState)

    def generatePath(self, state):

        def queue_function(nodes, newNodes, problem):
            for n in newNodes:
                nodes.push(n)

        stack = []
        stack.push(Node(None, self.startState, None))

        result = generalSearch(self, queue_function, stack)
        return result


class bfsAgent(Agent):
    def __init__(self, startState):
        super().__init__(startState)

    def generatePath(self, state):

        def queue_function(nodes, newNodes, problem):
            for n in newNodes:
                nodes.append(n)

        queue = []
        queue.append(Node(None, self.startState, None))

        result = generalSearch(self, queue_function, queue)
        return result
