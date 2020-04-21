from enum import Enum
import numpy as np
from PIL import Image
import networkx as nx
import matplotlib.pyplot as plt
from collections import namedtuple

def general_debugging():
  print("\n-------------------------")
  print("State:", state, ("Start" if is_start else ActionEnum(state.action).name))
  print("Following Path:", ("Start" if is_start else ActionEnum(state_path_root.action).name), "of length", counter)
  print(stack)

def graph_debugging():
  action_root = ("Start" if state_path_root.action == -1 else ActionEnum(state_path_root.action).name[0])
  action_prev = ("Start" if state_prev.action == -1 else ActionEnum(state_prev.action).name[0])
  #TODO: better way to output Point tuple without name attributes showing? Makes printing & Graph id messy
  print("Path", action_root, "of", counter, (action_root, state_path_root.point.x, state_path_root.point.y), "to", (action_prev, state_prev.point.x, state_prev.point.y))
  #print("Stack:", stack, "\n")

def calc_state(state, numAction):
  return State(numAction, Point(state.x + state_modifier[numAction].x, state.y + state_modifier[numAction].y))

def is_valid_state(state):
  # TODO: python define func in func to simplify these if statements, keep short circuiting
  x, y = state
  w, h = img.size

  #if inBounds and is a road
  in_bounds = True if x >= 0 and x < w and y >= 0 and y < h else False
  return True if in_bounds and img.getpixel(state) == (0, 0, 0) else False

def is_new_path(stateAction, pathAction):
  return True if stateAction != pathAction else False

def find_map_start(map, startColor):
  # Find & set start state
  w, h = map.size
  for x in range(0, w):
    for y in range(0, h):
      if img.getpixel((x,y)) == startColor:
        return Point(x, y)
  return None

class ActionEnum(Enum):
  NORTH = 0
  SOUTH = 1
  EAST = 2
  WEST = 3

inverse_action = np.array((1, 0, 3, 2), dtype=int)

Point = namedtuple('Point', ['x', 'y'])
State = namedtuple('State', ['action', 'point'])

#PIL holds (0,0) @ top left corner so N and S modifiers are flipped
state_modifier = [Point(0, -1), Point(0, 1), Point(1, 0), Point(-1, 0)]

#####    PROGRAM START    #####
img = Image.open('data/maps/map_2.png').convert('RGB')
MapGraph = nx.Graph()

start_flag = -1
start_point = find_map_start(img, (255, 255, 0))
if start_point == None:
  print("MAP_ERROR: No start position found")
  exit(1)
else:
  start_state = State(start_flag, start_point)

# Initialize a stack with the start position
stack = [start_state]
visitedStates = set()

#TODO: make these macros
debug = False
debug_graph = True
debug_graph_gui = True

limit = 300 #TODO: removes
while(stack != [] and limit > 0):
  # Take current state off the stack
  state = stack.pop()
  is_start = True if state.action == start_flag else False

  # If first iter define needed params
  if is_start:
    total_distance = 0
    walked_nodes = 0
    state_prev = state
    state_path_root = state
    counter = 0

  # --- Determine Valid Next Actions ---
  # Check all orthogonal actions and append them to the stack
  adjacent = False
  for action in ActionEnum:
    if action.value != state.action and action.value != inverse_action[state.action]:
      nextState = calc_state(state.point, action.value)
      if is_valid_state(nextState.point) and state.point not in visitedStates:
        adjacent = True
        stack.append(nextState)

  # If previous action is still valid append it last (LIFO)
  if not is_start and is_valid_state((nextState := calc_state(state.point, state.action)).point) and state.point not in visitedStates:
    adjacent = True
    stack.append(nextState)

  print(adjacent)

  # --- Determine Path Branching ---
  # If new vector path (changed action/direction)
  if is_new_path(state.action, state_path_root.action):
    # Graph Debug Printing
    if debug_graph: graph_debugging()
    print("Adjacency:", adjacent)

    # Add to Graph
    #TODO: better way to output Point tuple without name attributes showing? Makes printing & Graph id messy
    MapGraph.add_edge((state_path_root.point.x, state_path_root.point.y), (state_prev.point.x, state_prev.point.y))
    visitedStates.add(state_path_root.point)

    # Reset path tracking
    state_path_root = State(state.action, state_prev.point)
    #state_path_root = State(state.action, state.point)

    total_distance += counter
    counter = 1
  # If same path increment counter
  else:
    counter += 1

  # --- Do Printing ---
  if debug: general_debugging()

  # Prepare state information for next iteration
  state_prev = state
  walked_nodes += 1
  limit -= 1

# --- END While Loop ---

print("Walked:", walked_nodes, "\nTraveled:", total_distance)

if debug: print("visitedStates\n", visitedStates)

# Add data to graph nodes
#for node in MapGraph.nodes:
node_positions = {node: (node[0], -node[1]) for node in MapGraph.nodes}
#print(MapGraph.nodes(data=True))

# Draw Graph
if debug_graph_gui:
  nx.draw(MapGraph, pos=node_positions, with_labels=True, font_weight='bold')
  plt.show()