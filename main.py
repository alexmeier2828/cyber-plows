"""
    Setup for the gui stuff should go in here.  This should be the main entry point for the project
"""
import tkinter as tk


def main():
    #main function
    top = tk.Tk()


    canvas = tk.Canvas(top, bg = "blue", height=500, width=500)
    square = canvas.create_rectangle(300,300, 100, 100, fill="black", outline="red")

    canvas.pack()
    top.mainloop()
if __name__ == '__main__':
    main()
