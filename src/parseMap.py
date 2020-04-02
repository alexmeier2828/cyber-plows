from enum import Enum
from PIL import Image

def calcAction(state, stateNum):
  return (stateNum, state[1] + state_modifier[stateNum][0], state[2] + state_modifier[stateNum][1])

def isValidState(state, prevState):
  state = state[1:]
  if img.getpixel(state) == (0, 0, 0) and state != prevState[1:]:
    return True
  else:
    return False


img = Image.open('data/maps/map_1.png').convert('RGB')

# Find starting position
w, h = img.size
for x in range(w-1, -1, -1):
  for y in range(0, h):
    if img.getpixel((x,y)) == (255, 255, 0):
      start = (x, y)

class ActionEnum(Enum):
  NORTH = 0
  SOUTH = 1
  EAST = 2
  WEST = 3

state_modifier = [(0, 1), (0, -1), (1, 0), (-1, 0)]

start = (5, 7)

stack = [(-1,) + start]
counter = 1

first = True
debug = 30
while(debug > 0):
  state = stack.pop()
  if(first):
    prevState = state
    first = False
  print("Following State:", state)

  # if the previous action is still valid append that first
  # and increment counter
  nextState = calcAction(state, state[0])
  if state[0] != -1 and isValidState(nextState, prevState):
    stack.append(nextState)
    counter += 1
  else:
    counter = 1

  # find all other valid actions and append them to the stack
  for action in ActionEnum:
    if action.value != state[0]:
      nextState = calcAction(state, action.value)
      if isValidState(nextState, prevState):
        stack.append(nextState)

  prevState = state
  print(stack)
  print(counter)


  debug -= 1