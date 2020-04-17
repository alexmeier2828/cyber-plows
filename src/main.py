"""
    Setup for the gui stuff should go in here.  This should be the main entry point for the project
"""
import tkinter as tk
from views.mapView import MapView
from state import *
from game import Game

#main function


def main():
    top = tk.Tk()


    gameState = GameState("../data/maps/map_1.png") #TODO pass in an actual map PNG
    mapView = MapView(top, gameState)

    #demoInstrutions = [ActionEnum.EAST, ActionEnum.EAST, ActionEnum.WEST, ActionEnum.NORTH, ActionEnum.WEST, ActionEnum.SOUTH, ActionEnum.WAIT]
    game = Game(gameState, [ActionEnum.WAIT], mapView)




    game.gameLoop()
if __name__ == '__main__':
    main()
