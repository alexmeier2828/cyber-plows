"""
this file is a base class for all agent classes and should not be instantiated

"""
from generalSearch import *
from agentState import AgentState


class  Agent:
    def __init__(self, startState):
        #stuff that is common to all agents goes here
        self.startState = startState
        raise NotImplementedError

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

    def getNextState(self, instruction):
        #returns the next state
        raise NotImplementedError

    def getSuccessors(self, state):
        #returns a list of successor states

        #should return (state, direction) pair
        raise NotImplementedError



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
