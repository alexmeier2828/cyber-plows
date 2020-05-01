"""
  Main Testing File for Map Parsing
"""
from map_parse import MapGraph

# Main Function
def main():

    file_name = "data/maps/map_5.png"
    mapGraph(file_name).parse_map()


if __name__ == '__main__':
    main()
