from enum import Enum
import numpy as np
from PIL import Image
import networkx as nx
import matplotlib.pyplot as plt

def calcAction(state, stateNum):
  return (stateNum, state[1] + state_modifier[stateNum][0], state[2] + state_modifier[stateNum][1])

def isValidState(state):
  stateXY = state[1:]

  # TODO: python define func in func to simplify these if statements, keep short circuiting
  w, h = img.size
  inBounds = True if stateXY[0] >= 0 and stateXY[0] < w and stateXY[1] >= 0 and stateXY[1] < h else False

  #if inBounds and is a road
  return True if inBounds and img.getpixel(stateXY) == (0, 0, 0) else False

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

inverse_action = np.array((1, 0, 3, 2), dtype=int)

#PIL holds (0,0) @ top left corner so N and S modifiers are flipped
state_modifier = [(0, -1), (0, 1), (1, 0), (-1, 0)]

#####    PROGRAM START    #####
img = Image.open('data/maps/map_1.png').convert('RGB')
MapGraph = nx.Graph()

start_flag = -1

start_state = findMapStart(img, (255, 255, 0), -1)
if start_state == None:
  print("MAP_ERROR: No start position found")
  exit(1)


# Initialize a stack with the start position
stack = [start_state]
visitedStates = set()

total_distance = 0
debug = False
graph_debug = True
limit = 50
while(stack != [] and limit > 0):
  # Take current state off the stack
  state = stack.pop()
  isStart = True if state[0] == start_flag else False

  # If first iter define needed params
  if(isStart):
    prevState = state
    root_path = state
    counter = 0

  # --- Determine Valid Next Actions ---
  # if the previous action is still valid append it first
  nextState = calcAction(state, state[0])
  if not isStart and isValidState(nextState) and state[1:] not in visitedStates:
    stack.append(nextState)
  # find all other valid actions and append them to the stack
  for action in ActionEnum:
    if action.value != state[0]:
      nextState = calcAction(state, action.value)
      if isValidState(nextState) and nextState[1:] != prevState[1:] and state[1:] not in visitedStates:
        stack.append(nextState)


  # --- Determine Path Branching ---
  # If new vector path (changed action/direction)
  if isNewPath(state[0], root_path[0]):
    # Add to Graph
    if graph_debug:
      rootAction = ("Start" if root_path[0] == -1 else ActionEnum(root_path[0]).name[0])
      prevAction = ("Start" if prevState[0] == -1 else ActionEnum(prevState[0]).name[0])
      print("Path", rootAction, "of", counter, (rootAction, root_path[1], root_path[2]), "to", (prevAction, prevState[1], prevState[2]))

    MapGraph.add_edge(root_path[1:], prevState[1:])
    visitedStates.add(root_path[1:])

    # Reset path tracking
    root_path = (state[0], prevState[1], prevState[2])
    counter = 1
  # If same path increment counter
  else:
    counter += 1

  # --- Do Printing ---
  if debug:
    print("\n-------------------------")
    print("State:", state, ("Start" if isStart else ActionEnum(state[0]).name))
    print("Following Path:", ("Start" if isStart else ActionEnum(root_path[0]).name), "of length", counter)
    print(stack)

  # Prepare state information for next iteration
  prevState = state
  total_distance += 1
  limit -= 1

#end while loop

print("Traveled:", total_distance)
#print(visitedStates)

# Draw Graph
#for node in MapGraph.nodes:
node_positions = {node: (node[0], -node[1]) for node in MapGraph.nodes}

#print(MapGraph.nodes(data=True))

nx.draw(MapGraph, pos=node_positions, with_labels=True, font_weight='bold')
plt.show()