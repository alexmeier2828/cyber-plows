"""
this file is a base class for all agent classes and should not be instantiated

"""

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
        raise NotImplementedError

    def getNextState(self, instruction):
        #returns the next state
        raise NotImplementedError

    def getSuccessors(self, state):
        #returns a list of successor states
        raise NotImplementedError
