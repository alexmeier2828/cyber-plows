"""
    this file contains the mapView class which displays the graphical
    representation of the map
"""
import tkinter as tk

class MapView:
    def __init__(self, parent):
        self.height = 1028
        self.width = 1028
        self.grid_height = 32
        self.grid_width = 32
        self.mapCanvas = tk.Canvas(parent, bg="black" ,height=self.height, width=self.width)
        self.road_sprite = tk.PhotoImage(file=r'./sprites/road.gif')

    def draw(self):

        for x in range(0, self.grid_height - 1):
            for y in range(0, self.grid_width - 1):
                self.mapCanvas.create_image(x*32, y*32, image=self.road_sprite, anchor=tk.NE)

                print(x)
        self.mapCanvas.pack()
