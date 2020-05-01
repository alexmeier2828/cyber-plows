"""
this file is a base class for all agent classes and should not be instantiated

"""
from collections import deque
from copy import deepcopy
from agents.generalSearch import *
from agents.agentState import AgentState
from util import toVector

class  Agent:
    def __init__(self, gameState):
        #stuff that is common to all agents goes here
        self.startState = AgentState(gameState)
        self.mapGraph = gameState.mapGraph.map_graph


    """ tion, so dont try to
        stick an implementation here.  Instead, implement a
        child class like "class newAgent(agent):". You can
        overload whichever functions you need, though this
        class provides the basics.
    """
    def generatePath(self):
        #this is where the algorithm should be called
        raise NotImplementedError

    def isGoalState(self, state):
        #checks if goal state is reached
        for col in state.snow:
            for row in col:
                if row:
                    return False
        return True

    #takes an AgentState
    def getSuccessors(self, state):
        #returns a list of successor states
        #print("expanding node: " + str(state.location))
        startPoint = state.location
        successorNodes = self.mapGraph.neighbors(startPoint)
        successors = []
        for node in successorNodes:
            copy = deepcopy(state)
            direction, length = toVector(startPoint, node)

            if length <= state.fuel:
                #state updates itself
                copy.driveTo(node)

                #add successor to list
                successors.append((copy, (direction, length)))
            #should return (state, direction) pair
        return successors


class dfsAgent(Agent):
    def __init__(self, startState):
        super().__init__(startState)

    def generatePath(self):

        def queue_function(nodes, newNodes, problem):
            for n in newNodes:
                nodes.append(n)

        stack = deque()
        stack.append(Node(None, self.startState, None))

        result = generalSearch(self, queue_function, stack)
        return result


class bfsAgent(Agent):
    def __init__(self, startState):
        super().__init__(startState)

    def generatePath(self):

        def queue_function(nodes, newNodes, problem):
            for n in newNodes:
                nodes.appendleft(n)

        queue = deque()
        queue.appendleft(Node(None, self.startState, None))

        result = generalSearch(self, queue_function, queue)
        return result
