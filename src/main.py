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


    gameState = GameState("../data/maps/map_2.png") #TODO pass in an actual map PNG
    print(gameState.mapGraph.map_graph)
    startPoint = list(gameState.mapGraph.get_map())[0]
    test_agent = agent.bfsAgent(gameState)
    directions = test_agent.generatePath()
    for d in directions:
        print(d)


    mapView = MapView(top, gameState)
    print(util.vectorListToSingleSteps(directions))
    #demoInstrutions = [ActionEnum.EAST, ActionEnum.EAST, ActionEnum.WEST, ActionEnum.NORTH, ActionEnum.WEST, ActionEnum.SOUTH, ActionEnum.WAIT]
    game = Game(gameState, util.vectorListToSingleSteps(directions), mapView)





    game.gameLoop()
if __name__ == '__main__':
    main()
