from enum import Enum
import numpy as np
from PIL import Image
import networkx as nx
import matplotlib.pyplot as plt
from collections import namedtuple

def print_stack(stack):
  print("[", sep="", end="")
  for state in stack: print("(", ACTION_ENUM(state.action).name[0], ", ", state.point.x, ", ", state.point.y, "), ", sep="", end="")
  print("]", sep="")

def graph_debugging():
  action_root = ("Start" if state_path_root.action == -1 else ACTION_ENUM(state_path_root.action).name[0])
  action_prev = ("Start" if state_prev.action == -1 else ACTION_ENUM(state_prev.action).name[0])
  #TODO: better way to output Point tuple without name attributes showing? Makes printing & Graph id messy
  print("Path", action_root, "of", counter, (action_root, state_path_root.point.x, state_path_root.point.y), "to", (action_prev, state_prev.point.x, state_prev.point.y), "Adjacent" if adjacent else "")
  print("State: (", ACTION_ENUM(state.action).name[0], ", ", state.point.x, ", ", state.point.y, ")", sep="")
  #print("Action:", ACTION_ENUM(state.action).name[0], "Inverse:", ACTION_ENUM(inverse_action[state.action]).name[0])
  print_stack(stack)
  print()

def calc_state(state, numAction):
  return State(numAction, Point(state.x + state_modifier[numAction].x, state.y + state_modifier[numAction].y))

def is_valid_state(state):
  # TODO: python define func in func to simplify these if statements, keep short circuiting
  x, y = state
  w, h = img.size

  #if is in_bounds and is a road
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

class ACTION_ENUM(Enum):
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
img = Image.open('data/maps/map_5.png').convert('RGB')
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
visited_states = set()

#TODO: make these macros
debug_stack = False
debug_graph = True
debug_graph_gui = True

max_stack_size = 0
while(stack != []):
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

  # --- Determine Path Branching ---
  # If new vector path (changed action/direction)
  if is_new_path(state.action, state_path_root.action):
    if debug_graph: # Graph Debug Printing
      graph_debugging()

    # Add to Graph
    #TODO: better way to output Point tuple without name attributes showing? Makes printing & Graph id messy
    MapGraph.add_edge((state_path_root.point.x, state_path_root.point.y), (state_prev.point.x, state_prev.point.y))
    visited_states.add(state_path_root.point)

    #if state == State(2, (5, 4)): adjacent = False

    # Reset path tracking
    if adjacent:
      state_path_root = State(state.action, state_prev.point)
    else:
      state_path_root = State(state.action, calc_state(state.point, inverse_action[state.action]).point)

    total_distance += counter
    counter = 1
  # If same path increment counter
  else:
    counter += 1

  # --- Determine Valid Next Actions ---
  if debug_stack: print("State: (", "Start" if state.action == -1 else ACTION_ENUM(state.action).name[0], ", ", state.point.x, ", ", state.point.y, ")", sep="")

  # Check all orthogonal actions and append them to the stack
  adjacent = False
  if state.point not in visited_states:
    for action in ACTION_ENUM:
      if action.value != state.action and action.value != inverse_action[state.action]:
        state_next = calc_state(state.point, action.value)
        if is_valid_state(state_next.point):
          adjacent = True
          stack.append(state_next)

    # If previous action is still valid append it last (LIFO)
    if not is_start and is_valid_state((state_next := calc_state(state.point, state.action)).point):
      adjacent = True
      stack.append(state_next)

  # --- Prepare for next Iteration
  if max_stack_size < len(stack): max_stack_size = len(stack)
  state_prev = state
  walked_nodes += 1

# --- END While Loop ---
print("Peak stack size:", max_stack_size)
print("Set size:", len(visited_states))
print("Walked:", walked_nodes, "\nTraveled:", total_distance)
if debug_stack: print("Visited States\n", visited_states)

# Add data to graph nodes
#for node in MapGraph.nodes:
node_positions = {node: (node[0], -node[1]) for node in MapGraph.nodes}
#print(MapGraph.nodes(data=True))

# Draw Graph
if debug_graph_gui:
  nx.draw(MapGraph, pos=node_positions, with_labels=True, font_weight='bold')
  plt.show()