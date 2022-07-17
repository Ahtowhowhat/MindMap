from graph import Graph
import matplotlib.pyplot as plt

figsize = (18, 9)
dpi = 100
fig = plt.figure(figsize=figsize, dpi=dpi)
ax = fig.add_axes([0, 0, 1, 1])

G = Graph(figsize, dpi)
G.create_test()
# G.draw(ax)
# G.show()

G.create_node(0, 'sdfsdf')
# G.draw(ax)
# G.show()

G.create_node(0, 'rhefsdf')
G.draw(ax)
G.show()