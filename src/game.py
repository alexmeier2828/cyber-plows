"""This File contains the main game loop"""
import time
from state import *


class Game:
    def __init__(self, initial_state, instructions, mapView):
        self.gameState = initial_state
        self.plowInstructions = instructions
        self.time = 0
        self.mapView = mapView

    def gameLoop(self):
        print("Starting game loop...")

        i = 0;


        #main loop
        while not self.gameState.done:
            currentInstruction = ActionEnum.WAIT
            self.time = self.time + 1 #increase time counter

            if i < len(self.plowInstructions):
                currentInstruction = self.plowInstructions[i]
                print(currentInstruction)
            i = i + 1

            #move plow
            self.gameState.movePlow(currentInstruction)

            #display
            self.mapView.draw(self.gameState)
            time.sleep(0.5)
