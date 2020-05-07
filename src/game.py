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


        score = -self.fuelUsed - (5*self.gameState.refils)

        if self.failed:
            score = score - 10000
        #score = 1.0/(score + 1)
        return score


def isGameOver(gameState, game):
    print(gameState.plow.findStart(gameState.mapData))
    print(gameState.plow.currentPosition)
    if game.time > 1000:
        game.failed = True
        return True
    snow = gameState.mapData.getSnow()
    for col in snow:
        for row in col:
            if row:
                return False

    start = gameState.plow.findStart(gameState.mapData)
    if(gameState.plow.currentPosition[0] != start[0] and gameState.plow.currentPosition[1] != start[1]):
        return False


    return True
