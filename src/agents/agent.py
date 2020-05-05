"""
this file is a base class for all agent classes and should not be instantiated
"""

from collections import deque
from copy import deepcopy
from agents.generalSearch import *
from agents.agentState import AgentState
from util import toVector, PriorityQueue

class  Agent:
    def __init__(self, gameState):
        #stuff that is common to all agents goes here
        self.startState = AgentState(gameState)
        self.mapGraph = gameState.mapGraph.map_graph
        self.nodesExpanded = 0


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


        return (state.location == state.home)

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

    #iterates the node expansion count, do not overload
    def increaseNodeCount(self):
        self.nodesExpanded = self.nodesExpanded + 1

    #should return how the agent did
    def getCompletionDetails(self):
        return self.nodesExpanded

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


class aStarAgent(Agent):
    def __init__(self, startState):
        super().__init__(startState)

    def generatePath(self):

        def queue_function(pQueue, newNodes, problem):
            for n in newNodes:
                value = betterHeuristic(n.s)
                pQueue.push(n, value)


        queue = PriorityQueue()
        queue.push(Node(None, self.startState, None), betterHeuristic(self.startState))

        result = generalSearch(self, queue_function, queue)
        return result

#for now the heuristic is hust the count of how much snow is left,
#probably not a super efficient heuristic
def heuristic(agentState):
    snow = agentState.snow
    count = 0
    for x in snow:
        for y in x:
            if y:
                count = count + 1
    return count

def betterHeuristic(agentState):
    aX, aY = agentState.location
    homeX, homeY = agentState.home
    distanceToHome = abs(aX - homeX + aY - homeY)
    if distanceToHome > 0.5 * agentState.fuel:
        return distanceToHome
    else:
        #greedy
        shortestDistance = float("inf")
        width = len(agentState.snow)
        height = len(agentState.snow[0])
        for x in range(0, width):
            for y in range(0, height):
                dist = abs(aX - x + aY - y)
                shortestDistance = min(shortestDistance, dist)
        return shortestDistance

class dlsAgent(Agent):
    def __init__(self, startState, cutoff=100):
        super().__init__(startState)
        self.cutoff = cutoff


    def generatePath(self):
        def queue_function(nodes, newNodes, problem):
            for n in newNodes:
                nodes.append(n)

        stack = deque()
        stack.append(DepthNode(None, self.startState, None, 0))

        result = limitedGeneralSearch(self, queue_function, stack, self.cutoff)
        return result
