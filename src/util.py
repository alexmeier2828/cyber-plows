from state import ActionEnum
"""
    Return a vector (direction, length) from two points
"""
def toVector(start, end):
    x0, y0 = start
    x1, y1 = end
    direction = ActionEnum.WAIT

    if x1 == x0:    #north south
        if y1 < y0:
            direction = ActionEnum.NORTH
        elif y1 > y0:
            direction = ActionEnum.SOUTH
    else:           #east west
        if x1 < x0:
            direction = ActionEnum.WEST
        elif y1 > y0:
            direction = ActionEnum.EAST

    distance = (x1 - x0) + (y1 - y0)

    return (direction, distance)

def printSnow(snow):
    for x in snow:
        string = ""
        for y in x:
            if y:
                string = string + "#"
            else:
                string = string + "."
        print(string)
