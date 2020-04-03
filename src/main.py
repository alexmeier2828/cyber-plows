"""
    Setup for the gui stuff should go in here.  This should be the main entry point for the project
"""
import tkinter as tk
from views.mapView import MapView
from state import *

#main function


def main():
    top = tk.Tk()


    gameState = GameState("../data/maps/map_1.png") #TODO pass in an actual map PNG
    mapView = MapView(top, gameState)
    mapView.draw(gameState)




    top.mainloop()
if __name__ == '__main__':
    main()
