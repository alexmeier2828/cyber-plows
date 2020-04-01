import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_edge("W1", "N1", weight=3)
G.add_edge("N1", "W2", weight=2)
G.add_edge("N1", "E1", weight=2)

nx.draw(G, with_labels=True, font_weight='bold')
plt.show()