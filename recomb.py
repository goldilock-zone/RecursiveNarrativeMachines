import random
import networkx as nx
import matplotlib.pyplot as plt

class TopologicalLens:
    def __init__(self, n, lensID):
        self.lensID = lensID
        self.n = n  # Number of portals
        self.k = self.generate_random_k()
        self.connections = self.generate_connections()
        self.graph = self.create_graph()

    def generate_random_k(self):
        return random.randint(self.n, 2 * self.n)
    
    def set_lens_num(self, lens_num):
        self.k = lens_num

    def generate_connections(self):
        connections = []
        while len(connections) < self.k:
            portal1 = random.randint(1, self.n)
            portal2 = random.randint(1, self.n)
            if portal1 != portal2:
                connections.append((portal1, portal2))

        # Create a set of all nodes
        all_nodes = set(range(1, self.n + 1))

        # Create a set of nodes that are connected
        connected_nodes = set()
        for connection in connections:
            connected_nodes.add(connection[0])
            connected_nodes.add(connection[1])

        # Find isolated nodes (nodes not connected to others)
        isolated_nodes = all_nodes - connected_nodes

        # Connect isolated nodes to the rest of the graph
        for isolated_node in isolated_nodes:
            portal2 = random.choice(list(connected_nodes))
            connections.append((isolated_node, portal2))
        
        # If there are more connections than k, remove random connections
        while len(connections) > self.k:
            connections.pop(random.randint(0, len(connections) - 1))
        
        # If there are fewer connections than k, add random new connections
        while len(connections) < self.k:
            portal1 = random.randint(1, self.n)
            portal2 = random.randint(1, self.n)
            if portal1 != portal2 and (portal1, portal2) not in connections:
                connections.append((portal1, portal2))
        
        return connections

    def create_graph(self):
        G = nx.Graph()
        G.add_nodes_from(range(1, self.n + 1))
        G.add_edges_from(self.connections)
        return G

    def visualize(self):
        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos, with_labels=True, node_size=300, node_color='skyblue', font_size=10, font_color='black')
        plt.title('Topological Lens')
        plt.show()
    
    def get_edge_ids(self):
        edge_ids = {}
        for idx, (node1, node2) in enumerate(self.connections, start=1):
            edge_id = f"lensID{self.lensID}start{node1}end{node2}"
            edge_ids[edge_id] = ""
        return edge_ids

if __name__ == "__main__":
    # n = 5
    # topological_lens = TopologicalLens(n, "TestLens")
    # topological_lens.set_lens_num(8)
    # topological_lens.visualize()

    # edge_ids = topological_lens.get_edge_ids()
    # print("Edge IDs:")
    # print(edge_ids)
    pass