"""
    Setup for the gui stuff should go in here.  This should be the main entry point for the project
"""
import tkinter as tk
from views.mapView import MapView

#main function


def main():
    top = tk.Tk()
    mapView = MapView(top)
    mapView.draw()




    top.mainloop()
if __name__ == '__main__':
    main()
