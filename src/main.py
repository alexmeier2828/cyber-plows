"""
    Setup for the gui stuff should go in here.  This should be the main entry point for the project
"""
import tkinter as tk
from views.mapView import MapView
from state import *
from game import Game
import agents.agent as agent
import experiment
import util
import json

#main function


def main():
    top = tk.Tk()


    # gameState = GameState("../data/maps/map_2.png") #TODO pass in an actual map PNG
    # print(gameState.mapGraph.map_graph)
    # startPoint = list(gameState.mapGraph.get_map())[0]
    # test_agent = agent.bfsAgent(gameState)
    # directions = test_agent.generatePath()
    # for d in directions:
    #     print(d)
    #
    # print("Expaned " + str(test_agent.getCompletionDetails()) + " nodes")
    #mapView = MapView(top, gameState)
    # #print(util.vectorListToSingleSteps(directions))
    # #demoInstrutions = [ActionEnum.EAST, ActionEnum.EAST, ActionEnum.WEST, ActionEnum.NORTH, ActionEnum.WEST, ActionEnum.SOUTH, ActionEnum.WAIT]
    # game = Game(gameState, util.vectorListToSingleSteps(directions), mapView)
    #
    #
    #
    #
    #
    # game.gameLoop()

    results = experiment.runExperiment("../data/maps/map_1.png", top, {},  showGUI=True)
    results = experiment.runExperiment("../data/maps/map_2.png", top, results,  showGUI=True)
    results = experiment.runExperiment("../data/maps/map_3.png", top, results,  showGUI=True)

    dict_results = {
        "score": {"astar": [], "dfs":[], "bfs":[], "dls":[]},
        "nodes": {"astar": [], "dfs":[], "bfs":[], "dls":[]}
    }

    #print results
    for type in results.keys():
        print("Type: " + type)
        averageExpanded = 0
        averageScore = 0
        total = 0

        for result in results[type]:
            averageScore += result.score
            averageExpanded += result.nodesExpanded
            total += 1
            print(result)

            dict_results["score"][type].append(result.score)
            dict_results["nodes"][type].append(result.nodesExpanded)

        averageExpanded = averageExpanded / total
        averageScore = averageScore / total

        print("Average Score: " + str(averageScore) + " Average Expanded: " + str(averageExpanded))

        with open('data.json', 'w', newline='\n') as jsonfile:
            jsonfile.write(json.dumps(dict_results))


if __name__ == '__main__':
    main()
