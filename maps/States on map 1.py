#Notes:
#'N' = North, 'S' = South, 'E' = East, 'W' = West, 'X' = Wait
#Coordinates are defined as follows: 
# (char) = X-axis position, where a is far left, and g is far right. 
# (int) = y-axis position, where 1 is top, and 9 is bottom.
#Example: 
# a1 = top left of map, g9 = bottom right, d5 = middle

#available actions for each position. Where F8 is homebase
    #(Coordinate)Actions = actions available based on the coordinate
    #(Coordinate)Next = next coordinate when taking a specific action
    #Example:
    #f8Actions = ('W', 'X'), means that form position f8, we can either move west or wait.
    #f8Next = ('d8', 'f8'), If we move west, next position will be d8, and if we wait, we will be at f8         


############################   Map1   ############################
homebase = 'f8' #Starting position on this map, marked by the caution lines
topLeft = 'a1'
bottomRight= 'g9'


f8Actions = ('W','X')
f8Next = ('d8', 'f8') 

d8Actions = ('N','E','X')
d8Next = ('d6', 'f8', 'd8') 

d6Actions = ('E','S','W','X')
d6Next = ('f6','d8','b6','d6')

b6Actions = ('N','E','X')
b6Next = ('b2','d6','b6')

b2Actions = ('E','S','X')
b2Next = ('f2', 'b6', 'b2')

f2Actions = ('S','W','X')
f2Next = ('f6','b2','f2')

f6Actions = ('N','W','X')
f6Next = ('f2','d6','f6')

