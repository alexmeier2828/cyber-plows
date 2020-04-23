from enum import Enum
import numpy as np
from PIL import Image
import networkx as nx
import matplotlib.pyplot as plt
from collections import namedtuple

#---------- Globals ----------
class ACTION_ENUM(Enum):
  NORTH = 0
  SOUTH = 1
  EAST = 2
  WEST = 3

inverse_action = np.array((1, 0, 3, 2), dtype=int)

Point = namedtuple('Point', ['x', 'y'])
State = namedtuple('State', ['action', 'point'])

start_color = (255, 255, 0)

#PIL holds (0,0) @ top left corner so N and S modifiers are flipped
state_modifier = [Point(0, -1), Point(0, 1), Point(1, 0), Point(-1, 0)]

#---------- Class ----------
class MapData:

  # Constructor
  def __init__(self, imageFileName):
    #### Public Vars ####
    self.image_file_name = imageFileName
    self.width = None
    self.height = None
    self.map_graph = nx.Graph()

    ##### Private Vars ####
    self.__start_flag = -1
    #self.__start_point = None

    self.__debug_stack = False
    self.__debug_graph = True
    self.__debug_graph_gui = True

    self.__max_stack_size = -1
    self.__set_size = -1
    self.__walked_nodes = -1
    self.__traveled_distance = -1

  #---------- Public Methods ----------

  # Returns Map Graph
  def get_map(self):
    return self.map_graph

  #Runs Map Parsinf
  def parse_map(self):
    # Prepare main Data
    img = self.__load_image()

    # Get starting state
    # TODO: make this an init var instead
    start_state = self.__find_start(img)

    # Prepare data structures for graphing
    stack = [start_state]
    visited_states = set()

    # Prepare loop globals (for counting)
    max_stack_size = 0
    total_distance = 0
    walked_nodes = 0

    while(stack != []):
      # Take current state off the stack
      state = stack.pop()

      # Checking condition if it's the first iteration
      is_start = True if state.action == self.__start_flag else False

      # If first iter define needed params
      if is_start:
        state_prev = state
        state_path_root = state
        counter = 0

      ##### Determine Path Branching ####

      # If new vector path (changed action/direction)
      if self.__is_new_path(state.action, state_path_root.action):
        # Graph Debug Printing
        if self.__debug_graph: self.__graph_debugging(state_path_root, state, state_prev, counter, adjacent, stack)

        # Add to Graph
        self.map_graph.add_edge((state_path_root.point.x, state_path_root.point.y), (state_prev.point.x, state_prev.point.y))
        #TODO: better way to output Point tuple without name attributes showing? Makes printing & Graph id messy
        visited_states.add(state_path_root.point)

        # Reset path tracking
        if adjacent:
          state_path_root = State(state.action, state_prev.point)
        else:
          state_path_root = State(state.action, self.__calc_state(state.point, inverse_action[state.action]).point)

        total_distance += counter
        counter = 1

      # If same path increment counter
      else:
        counter += 1

      ##### Determine Valid Next Actions ####

      # Stack Debug Printing
      if self.__debug_stack: print("State: (", "Start" if state.action == -1 else ACTION_ENUM(state.action).name[0], ", ", state.point.x, ", ", state.point.y, ")", sep="")

      # Set an adjacent state (when at least one node is added)
      adjacent = False

      # Check only orthogonal actions and append
      if state.point not in visited_states:
        for action in ACTION_ENUM:
          if action.value != state.action and action.value != inverse_action[state.action]:
            state_next = self.__calc_state(state.point, action.value)
            if self.__is_valid_state(state_next.point, img):
              adjacent = True
              stack.append(state_next)

        # If previous action is still valid append it last (LIFO)
        state_next = self.__calc_state(state.point, state.action)
        if not is_start and self.__is_valid_state(state_next.point, img):
          adjacent = True
          stack.append(state_next)

      # --- Prepare for next Iteration
      if max_stack_size < len(stack): max_stack_size = len(stack)
      state_prev = state
      walked_nodes += 1

    # --- END While Loop ---

    # Set class properties
    self.__max_stack_size = max_stack_size
    self.__set_size = len(visited_states)
    self.__walked_nodes = walked_nodes
    self.__traveled_distance = total_distance

    # Stack Debug Printing
    if self.__debug_stack: print("Visited States\n", visited_states)

    # Draw Graph Debug
    if self.__debug_graph_gui:
      # Inject data into graph nodes
      #for node in MapGraph.nodes:
      node_positions = {node: (node[0], -node[1]) for node in self.map_graph.nodes}
      #print(MapGraph.nodes(data=True))

      nx.draw(self.map_graph, pos=node_positions, with_labels=True, font_weight='bold')
      plt.show()
  #### END parse_map ####

  #---------- Private Methods ----------

  #### Helper Functions ####

  # Load image and define some parameters
  def __load_image(self):
    # Load image
    #TODO: use load?
    img = Image.open(self.image_file_name).convert('RGB')
    if img == None:
      print("ERROR: Unable to open map")
      exit(1)

    # Define image size
    self.width, self.height = img.size
    return img

  # Find & set start state
  def __find_start(self, img):
    # Search for starting location
    start_point = None
    for x in range(0, self.width):
      for y in range(0, self.height):
        if img.getpixel((x,y)) == start_color:
          start_point = Point(x, y)

    if start_point == None:
      print("MAP_ERROR: No start position found")
      exit(1)

    return State(self.__start_flag, start_point)

  def __calc_state(self, state, numAction):
    return State(numAction, Point(state.x + state_modifier[numAction].x, state.y + state_modifier[numAction].y))

  def __is_valid_state(self, state, img):
    # TODO: python define func in func to simplify these if statements, keep short circuiting
    x, y = state
    w, h = self.width, self.height

    #if is in_bounds and is a road
    in_bounds = True if x >= 0 and x < w and y >= 0 and y < h else False
    return True if in_bounds and img.getpixel(state) == (0, 0, 0) else False

  def __is_new_path(self, stateAction, pathAction):
    return True if stateAction != pathAction else False

  #### Debugging Printers ####

  def __print_stack(self, stack):
    print("[", sep="", end="")
    for state in stack: print("(", ACTION_ENUM(state.action).name[0], ", ", state.point.x, ", ", state.point.y, "), ", sep="", end="")
    print("]", sep="")

  def __graph_debugging(self, state_path_root, state, state_prev, counter, adjacent, stack):
    action_root = ("Start" if state_path_root.action == -1 else ACTION_ENUM(state_path_root.action).name[0])
    action_prev = ("Start" if state_prev.action == -1 else ACTION_ENUM(state_prev.action).name[0])
    #TODO: better way to output Point tuple without name attributes showing? Makes printing & Graph id messy
    print("Path", action_root, "of", counter, (action_root, state_path_root.point.x, state_path_root.point.y), "to", (action_prev, state_prev.point.x, state_prev.point.y), "Adjacent" if adjacent else "")
    print("State: (", ACTION_ENUM(state.action).name[0], ", ", state.point.x, ", ", state.point.y, ")", sep="")
    #print("Action:", ACTION_ENUM(state.action).name[0], "Inverse:", ACTION_ENUM(inverse_action[state.action]).name[0])
    self.__print_stack(stack)
    print()