from enum import Enum
from PIL import Image
import networkx as nx
import matplotlib.pyplot as plt

def calcAction(state, stateNum):
  return (stateNum, state[1] + state_modifier[stateNum][0], state[2] + state_modifier[stateNum][1])

def isValidState(state, prevState):
  stateXY = state[1:]

  # TODO: python define func in func to simplify these if statements, keep short circuiting
  w, h = img.size
  inBounds = True if stateXY[0] >= 0 and stateXY[0] <= w-1 and stateXY[1] >= 0 and stateXY[1] < h-1 else False
  print(stateXY, inBounds)

  #if inBounds, is a road, and isn't the state we just came from (prevents backstepping)
  return True if inBounds and img.getpixel(stateXY) == (0, 0, 0) and stateXY != prevState[1:] else False

def isNewPath(stateAction, pathAction):
  return True if stateAction != pathAction else False

def findMapStart(map, startColor, startFlag):
  # Find & set start state
  w, h = map.size
  for x in range(0, w):
    for y in range(0, h):
      if img.getpixel((x,y)) == startColor:
        return (startFlag, x, y)

  return None


class ActionEnum(Enum):
  NORTH = 0
  SOUTH = 1
  EAST = 2
  WEST = 3

#PIL holds (0,0) @ top left corner so N and S modifiers are flipped
state_modifier = [(0, -1), (0, 1), (1, 0), (-1, 0)]

#####    PROGRAM START    #####
img = Image.open('data/maps/map_1.png').convert('RGB')
G = nx.Graph()

start_flag = -1

start_state = findMapStart(img, (255, 255, 0), -1)
if start_state == None:
  print("MAP_ERROR: No start position found")
  exit(1)


# Create stack to start with based on start position
print(img.size)
stack = [start_state]

debug = True
limit = 6
while(limit > 0):
  # Take current state off the stack
  state = stack.pop()

  # If this is the first run define certain paramters
  if(state[0] == start_flag): #if first run
    counter = 1
    prevState = state

  # --- Determine Path Branching ---
  # Determine wether the current state is a new branch and do appropriate actions
  if state[0] == start_flag or isNewPath(state[0], root_path[0]):
    counter = 1
    root_path = state
  else:
    counter += 1

  # --- Determine Valid Next Actions ---
  # if the previous action is still valid append it first & increment counter
  nextState = calcAction(state, state[0])
  if state[0] != start_flag and isValidState(nextState, prevState):
    stack.append(nextState)
  # find all other valid actions and append them to the stack
  for action in ActionEnum:
    if action.value != state[0]:
      nextState = calcAction(state, action.value)
      if isValidState(nextState, prevState):
        stack.append(nextState)

  # --- Do Printing ---
  if debug:
    print("\n-------------------------")
    print("Following State:", state, ("Start" if state[0] == -1 else ActionEnum(state[0]).name))
    print("Following Path:", ("Start" if root_path[0] == -1 else ActionEnum(root_path[0]).name), "Count:", counter)
    print(stack)

  # Prepare state information for next iteration
  prevState = state
  limit -= 1

#end while loop