"""
    this file contains the mapView class which displays the graphical
    representation of the map
"""
import tkinter as tk
from state import *

class MapView:
    def __init__(self, parent, gameState):
        self.height = gameState.mapData.height * 32
        self.width = gameState.mapData.width * 32
        self.grid_height = gameState.mapData.height
        self.grid_width = gameState.mapData.width
        print(str(self.grid_height) + "  " + str( self.grid_width))
        self.parent = parent
        self.mapCanvas = tk.Canvas(parent, bg="black" ,height=self.height, width=self.width)

        #sprites
        self.road_sprite = tk.PhotoImage(file=r'../data/sprites/road.gif')
        self.wall_sprite = tk.PhotoImage(file=r'../data/sprites/wall.gif')
        self.snow_sprite = tk.PhotoImage(file=r'../data/sprites/snow.gif')
        self.home_sprite = tk.PhotoImage(file=r'../data/sprites/home.gif')
        self.plow_sprite = tk.PhotoImage(file=r'../data/sprites/plow.gif')

    def draw(self, gameState):
        self.mapCanvas.delete("all")
        for x in range(0, self.grid_width):
            for y in range(0, self.grid_height):
                tile = gameState.mapData.mapArray[x][y]
                if tile is TileTypes.ROAD:
                    self.mapCanvas.create_image((x+1)*32, (y)*32, image=self.road_sprite, anchor=tk.NE)
                if tile is TileTypes.WALL:
                    self.mapCanvas.create_image((x+1)*32, (y)*32, image=self.wall_sprite, anchor=tk.NE)
                if tile is TileTypes.HOME:
                    self.mapCanvas.create_image((x+1)*32, (y)*32, image=self.home_sprite, anchor=tk.NE)

                if x is gameState.plow.currentPosition[0] and y is gameState.plow.currentPosition[1]:
                    self.mapCanvas.create_image((x+1)*32, (y)*32, image=self.plow_sprite, anchor=tk.NE)
        self.mapCanvas.pack()
        self.parent.update_idletasks()
        self.parent.update()
