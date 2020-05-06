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


def runExperiment(map, top, results, showGUI=False):
    results = results
    runs = []
    gameState = GameState(map, (40, 40))
    startPoints = gameState.getValidStartPoints()
    for location in startPoints:

        #aStar
        gameStateAStar = GameState(map, (40, 40))
        gameStateAStar.setStartPoint(location)
        astar = agents.aStarAgent(gameStateAStar)



        #dfs
        gameStateDFS = GameState(map, (40, 40))
        gameStateDFS.setStartPoint(location)
        dfs = agents.dfsAgent(gameStateDFS)


        #bfs
        gameStateBFS = GameState(map, (40, 40))
        gameStateBFS.setStartPoint(location)
        bfs = agents.bfsAgent(gameStateBFS)

        #dls
        gameStateDLS = GameState(map, (40, 40))
        gameStateDLS.setStartPoint(location)
        dls = agents.dlsAgent(gameStateDLS, 100)






        #add to Runs
        runs.append((gameStateAStar, astar, "astar"))
        runs.append((gameStateDFS, dfs, "dfs"))
        runs.append((gameStateBFS, bfs, "bfs"))
        runs.append((gameStateDLS, dls, "dls"))


    mapView = MapView(top, gameState)
    #start Runs
    for run in runs:
        gameState, agent, type = run
        print("Running a " + type + "run...")
        path = agent.generatePath()


        game = Game(gameState, util.vectorListToSingleSteps(path), mapView)
        score = game.gameLoop(showGUI=showGUI)

        result = Result(score, type, agent.nodesExpanded)
        #add results
        if type in results:
            results[type].append(result)
        else:
            results[type] = [result]

    return results
