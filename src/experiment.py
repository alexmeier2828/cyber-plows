import tkinter as tk
from views.mapView import MapView
from state import *
from game import Game
import agents.agent as agents
import util


class Result:
    def __init__(self, score, agentType, nodesExpanded):
        self.score = score
        self.nodesExpanded = nodesExpanded
        self.agentType = agentType
    def __str__(self):
        return ("AgentType: " + self.agentType
        + " Score: " + str(self.score)
        + " Nodes Expanded: " + str(self.nodesExpanded));


def runExperiment(map, top, showGUI=False):
    results = {}
    runs = []
    gameState = GameState(map)
    startPoints = gameState.getValidStartPoints()
    for location in startPoints:


        #create agents
        gameStateDFS = GameState(map)
        gameStateDFS.setStartPoint(location)
        dfs = agents.dfsAgent(gameStateDFS)
 

        #bfs
        gameStateBFS = GameState(map)
        gameStateBFS.setStartPoint(location)
        bfs = agents.bfsAgent(gameStateBFS)





        #add to Runs
        runs.append((gameStateDFS, dfs, "dfs"))
        runs.append((gameStateBFS, bfs, "bfs"))


    #start Runs
    for run in runs:
        gameState, agent, type = run
        print("Running a " + type + "run...")
        path = agent.generatePath()

        mapView = MapView(top, gameState)
        game = Game(gameState, util.vectorListToSingleSteps(path), mapView)
        score = game.gameLoop(showGUI=showGUI)

        result = Result(score, type, agent.nodesExpanded)
        #add results
        if type in results:
            results[type].append(result)
        else:
            results[type] = [result]


    #print results
    for type in results.keys():
        print("Type: " + type)
        for result in results[type]:
            print(result)
