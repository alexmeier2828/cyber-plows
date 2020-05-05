"""
  Main Testing File for Map Parsing
"""
from map_parse import MapGraph

# Main Function
def main():

    file_name = "data/maps/map_2.png"
    #file_name = "data/maps/map_5.png"
    map_graph = MapGraph(file_name)
    map_graph.parse_map()

if __name__ == '__main__':
    main()
