"""This File contains the main game loop"""
import time
from state import *
import util


class Game:
    def __init__(self, initial_state, instructions, mapView):
        self.gameState = initial_state
        self.plowInstructions = instructions
        self.fuelUsed = 0
        self.time = 0;
        self.mapView = mapView
        self.failed = False

    def gameLoop(self, showGUI=True):
        print("Starting game loop...")

        i = 0;


        #main loop
        while not isGameOver(self.gameState, self):
            print(self.time)
            currentInstruction = ActionEnum.WAIT
            self.time = self.time + 1 #increase time counter

            if i < len(self.plowInstructions):
                currentInstruction = self.plowInstructions[i]
                self.fuelUsed = self.fuelUsed + 1
                print(currentInstruction)
            i = i + 1

            #move plow
            self.gameState.movePlow(currentInstruction)

            #display
            if showGUI:
                self.mapView.draw(self.gameState)
                time.sleep(0.01)


        score = self.fuelUsed #need to figure out score

        if self.failed:
            score = score + 1000
        score = 1.0/(score + 1)
        return score


def isGameOver(gameState, game):
    if game.time > 300:
        game.failed = True
        return True
    snow = gameState.mapData.getSnow()
    for col in snow:
        for row in col:
            if row:
                return False

    return True
