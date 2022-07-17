import matplotlib.pyplot as plt
# from matplotlib.widgets import Button

from node import Node

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


class Graph:
    def __init__(self, figsize, dpi, fontsize=16):
        self.fontsize = fontsize
        self.linewidth = 2
        self.linestyle = 'solid'
        self.linecolor = 'black'
        # create figure
        self.figsize = figsize
        self.dpi = dpi
        self.ax = None
        self.transf = None
        # print(self.fig.get_dpi(), self.fig.get_size_inches())
        # create root node
        self.root = Node(ID=0, text='根节点', fontsize=self.fontsize,
                         figsize=self.figsize, dpi=self.dpi, position=(0.05, 0.5))
        self.next_ID = 1
        self.nodes_dict = {0: self.root}
        self.root.selected = True

    def move_node(self, cur_idx: int, direction: str):
        cur_node = self.nodes_dict[cur_idx]
        parent = cur_node.parent
        i = parent.children.index(cur_node)
        if direction == 'up':
            if i > 0:
                parent.children[i - 1], parent.children[i] = parent.children[i], parent.children[i - 1]
        else:
            if i < parent.num_of_children - 1:
                parent.children[i + 1], parent.children[i] = parent.children[i], parent.children[i + 1]

    def move_node_to_parent(self, cur_idx: int):
        cur_node = self.nodes_dict[cur_idx]
        parent = cur_node.parent
        if parent.parent is None:
            return
        grandparent = parent.parent
        parent.children.remove(cur_node)
        i = grandparent.children.index(parent)
        grandparent.children.insert(i, cur_node)
        cur_node.parent = grandparent

    def move_node_to_child(self, cur_idx: int):
        cur_node = self.nodes_dict[cur_idx]
        parent = cur_node.parent
        i = parent.children.index(cur_node)
        if i < parent.num_of_children - 1:
            parent.children.pop(i)
            parent.children[i].children.insert(0, cur_node)
            cur_node.parent = parent.children[i]

    def create_node(self, parent_idx: int, text='请输入', fontsize=14):
        parent = self.nodes_dict[parent_idx]
        node = Node(ID=self.next_ID, text=text, fontsize=self.fontsize,
                    figsize=self.figsize, dpi=self.dpi,
                    parent=parent)
        self.next_ID += 1
        # self.nodes_list.append(node)
        self.nodes_dict[node.ID] = node
        parent.children.append(node)
        return node.ID

    def delete_node(self, cur_idx: int, selected_node):

        def delete(root: Node):
            for node in root.children:
                delete(node)
            # self.nodes_list[root.ID] = None
            self.nodes_dict.pop(root.ID)
            selected_node.removeItem(selected_node.findText(str(root.ID)))
            del root

        cur_node = self.nodes_dict[cur_idx]
        # print(cur_node.ID, cur_node.text, cur_node.parent)
        for node in cur_node.parent.children:
            if id(node) == id(cur_node):
                cur_node.parent.children.remove(node)
        delete(cur_node)

    def update_node(self, idx_node, text):
        cur_node = self.nodes_dict[idx_node]
        cur_node.text = text
        cur_node.height = (cur_node.fontsize * 2.0) / cur_node.figsize[1] / cur_node.dpi
        cur_node.width = (cur_node.fontsize * len(text) * 1.5) / cur_node.figsize[0] / cur_node.dpi

    def _calculate_structure_attribute(self, root: Node):
        root.num_of_children = len(root.children)
        if root.num_of_children == 0:
            root.first_half = 0.5
            root.second_half = 0.5
            self.root.lines_all = 1
            return 1
        root.lines_all = 0
        root.lines_each_children.clear()
        for node in root.children:
            cur = self._calculate_structure_attribute(node)
            root.lines_each_children.append(cur)
            root.lines_all += cur
        root.first_half = sum(root.lines_each_children[:root.num_of_children // 2])
        root.second_half = sum(root.lines_each_children[root.num_of_children // 2:])
        if root.num_of_children % 2 == 1:
            root.first_half += root.children[root.num_of_children // 2].first_half
            root.second_half -= root.children[root.num_of_children // 2].first_half
        # print(root.ID, root.lines_all)
        # print(root.first_half, root.second_half)
        return root.lines_all

    def _draw_branch(self, point, length=0.01):
        """
        draw the link-line to the child \n
        :param point: the position on the trunk
        :param length: the length of branch
        :return:
        """
        x = (point[0], point[0] + length)
        y = (point[1], point[1])
        self.ax.plot(x, y,
                     transform=self.ax.transAxes,
                     color=self.linecolor, linestyle=self.linestyle, linewidth=self.linewidth)
        return x[1], y[1]

    def _draw(self, root: Node, position, show_ID, show_box):
        root.link_point_parent = position
        root.draw_node(self.ax, show_ID, show_box, self.fontsize)
        if root.num_of_children == 0:
            return
        cur_point = self._draw_branch((root.link_point_parent[0] + root.width, root.link_point_parent[1]))
        vertical_length_up = \
            (root.first_half - root.children[0].first_half) * root.height * 1.2
        vertical_length_down = \
            (root.second_half - root.children[-1].second_half) * root.height * 1.2
        vertical_end = [cur_point[0], cur_point[1] - vertical_length_down]
        vertical_start = [cur_point[0], cur_point[1] + vertical_length_up]
        self.ax.plot((vertical_start[0], vertical_end[0]), (vertical_start[1], vertical_end[1]),
                     transform=self.ax.transAxes,
                     color=self.linecolor, linestyle=self.linestyle, linewidth=self.linewidth)
        # calculate positions of children and draw them
        for i in range(len(root.children)):
            node_start = self._draw_branch(vertical_start)
            self._draw(root.children[i], node_start, show_ID, show_box)
            if i < root.num_of_children - 1:
                vertical_start[1] -= (
                        (root.children[i].second_half + root.children[i + 1].first_half) * root.height * 1.2)

    def draw(self, ax, show_ID=False, show_box=False):
        # self._create()
        self.ax = ax
        self.transf = ax.transAxes.inverted()
        self._calculate_structure_attribute(self.root)
        self._draw(self.root, self.root.link_point_parent, show_ID, show_box)

    def _get_wh(self, root: Node):
        # print(root.width, root.height)
        bbox = root.text_fig.get_bbox_patch().get_extents().transformed(self.transf)
        root.width = bbox.width
        root.height = bbox.height
        # print(root.text_fig.get_bbox_patch().get_extents().transformed(self.transf).width,
        #       root.text_fig.get_bbox_patch().get_extents().transformed(self.transf).height)
        # print(bbox.width, bbox.height)
        for node in root.children:
            self._get_wh(node)

    def get_wh(self):
        self._get_wh(self.root)

    def show(self):
        plt.show()

    def create_test(self):
        for i in range(2):
            self.root.children.append(Node(ID=self.next_ID, text='神经网络' + str(self.next_ID), fontsize=14,
                                           figsize=self.figsize, dpi=self.dpi))
            self.next_ID += 1
        t = [5, 0]
        for i, node in enumerate(self.root.children):
            for j in range(t[i]):
                node.children.append(Node(ID=self.next_ID, text='神经网络' + str(self.next_ID), fontsize=14,
                                          figsize=self.figsize, dpi=self.dpi))
                self.next_ID += 1
        t = [3, 0, 0, 0, 0]
        for i, node in enumerate(self.root.children[0].children):
            for j in range(t[i]):
                node.children.append(Node(ID=self.next_ID,
                                          text='神经网络' + str(self.next_ID), fontsize=14,
                                          figsize=self.figsize, dpi=self.dpi))
                self.next_ID += 1
        t = [0, 4, 1]
        for i, node in enumerate(self.root.children[0].children[0].children):
            for j in range(t[i]):
                node.children.append(Node(ID=self.next_ID, text='神经网络' + str(self.next_ID), fontsize=14,
                                          figsize=self.figsize, dpi=self.dpi))
                self.next_ID += 1
        t = [0, 0, 2, 3]
        for i, node in enumerate(self.root.children[0].children[0].children[1].children):
            for j in range(t[i]):
                node.children.append(Node(ID=self.next_ID, text='神经网络' + str(self.next_ID), fontsize=14,
                                          figsize=self.figsize, dpi=self.dpi))
                self.next_ID += 1
