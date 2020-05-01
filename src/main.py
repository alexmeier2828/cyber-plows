"""
    Setup for the gui stuff should go in here.  This should be the main entry point for the project
"""
import tkinter as tk
from views.mapView import MapView
from state import *
from game import Game
import agents.agent as agent
import util

#main function


def main():
    top = tk.Tk()


    gameState = GameState("../data/maps/map_1.png") #TODO pass in an actual map PNG
    print(gameState.mapGraph.map_graph)
    startPoint = list(gameState.mapGraph.get_map())[0]
    test_agent = agent.dfsAgent(gameState)
    directions = test_agent.generatePath()
    for d in directions:
        print(d)

    print("Expaned " + str(test_agent.getCompletionDetails()) + " nodes")
    mapView = MapView(top, gameState)
    #print(util.vectorListToSingleSteps(directions))
    #demoInstrutions = [ActionEnum.EAST, ActionEnum.EAST, ActionEnum.WEST, ActionEnum.NORTH, ActionEnum.WEST, ActionEnum.SOUTH, ActionEnum.WAIT]
    game = Game(gameState, util.vectorListToSingleSteps(directions), mapView)





    game.gameLoop()



if __name__ == '__main__':
    main()
