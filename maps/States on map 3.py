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


############################   Map3   ############################
homebase = 'f8' #Starting position on this map, marked by the caution lines
topLeft = 'a1'
bottomRight= 'g9'


f8Actions = ('N','W','X')
f8Next = ('f2','b8','f8')

f2Actions = ('S','W','X')
f2Next = ('f8','b2','f2')

b2Actions = ('E','S','X')
b2Next = ('f2','b8','b2')

b8Actions = ('N','E','X')
b8Next = ('b2','f8','b8')



