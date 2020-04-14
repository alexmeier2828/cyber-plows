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


    gameState = GameState("../data/maps/map_2.png") #TODO pass in an actual map PNG
    mapView = MapView(top, gameState)

    demoInstrutions = [ActionEnum.WEST, ActionEnum.WEST, ActionEnum.NORTH, ActionEnum.EAST]
    game = Game(gameState, demoInstrutions, mapView)




    game.gameLoop()
if __name__ == '__main__':
    main()
