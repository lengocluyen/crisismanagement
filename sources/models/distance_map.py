import numpy as np
import osmnx as ox

#%matplotlib inline
np.random.seed(0)
ox.__version__

class OpenStreetMap:
    def __init__(self, city_name):
        self.map_graph = ox.graph_from_place(city_name, network_type="drive")

    def get_distance(self, origin_s, destination_s, by="length"):
        map = self.map_graph
        origin_i = origin_s[0].split(",")
        origin = (float(origin_i[0]), float(origin_i[1]))
        destination_i = destination_s[0].split(",")
        destination = (float(destination_i[0]), float(destination_i[1]))
        # impute speed on all edges missing data
        map = ox.add_edge_speeds(map)

        # calculate travel time (seconds) for all edges
        map = ox.add_edge_travel_times(map)
        origin_node = ox.distance.nearest_nodes(map, origin[1], origin[0])
        destination_node = ox.distance.nearest_nodes(map, destination[1], destination[0])

        #print(f"Distance: {origin}{destination}")
        
        route = ox.shortest_path(map, origin_node, destination_node, weight=by)
        if by == "length":
            inverse_by = "travel_time"
            route_length = int(sum(ox.utils_graph.get_route_edge_attributes(map, route,  by))) 
            route_time = int(sum(ox.utils_graph.get_route_edge_attributes(map, route, inverse_by)))
        else:
            inverse_by = "length"
            route_length = int(sum(ox.utils_graph.get_route_edge_attributes(map, route,  by))) 
            route_time = int(sum(ox.utils_graph.get_route_edge_attributes(map, route, inverse_by)))
        #print(f"is : {route_estimate} by length")
        return (route_length, route_time)


"""
G = ox.graph_from_place("Oise, France", network_type="drive")
orig = list(G)[0]
dest = list(G)[120]
print("dest", dest)
route1 = ox.shortest_path(G, orig, dest, weight="length")
route2 = ox.shortest_path(G, orig, dest, weight="travel_time")
route1_length = int(sum(ox.utils_graph.get_route_edge_attributes(G, route1, "length")))
#route2_length = int(sum(ox.utils_graph.get_route_edge_attributes(G, route2, "length")))
#route1_time = int(sum(ox.utils_graph.get_route_edge_attributes(G, route1, "travel_time")))
#route2_time = int(sum(ox.utils_graph.get_route_edge_attributes(G, route2, "travel_time")))
print("route1_length", route1_length)
#print("route2_time", route2_time)
#print("Route 1 is", route1_length, "meters and takes", route1_time, "seconds.")
#print("Route 2 is", route2_length, "meters and takes", route2_time, "seconds.")

fig, ax = ox.plot_graph_routes(
    G, routes=[route1, route2], route_colors=["r", "y"], route_linewidth=6, node_size=0
)

ox.plot_graph(G)
"""