# import matplotlib.patches as patches

# from matplotlib.widgets import Button
# from matplotlib.axes import Axes


# import matplotlib.pyplot as plt
# import matplotlib.pyplot as plt
# from matplotlib.transforms import Bbox


class Node:
    def __init__(self, ID: int, text: str, fontsize: int,
                 figsize: tuple, dpi: int,
                 lines_all: int = 1, num_of_children: int = 0, lines_each_children=None, position=None,
                 parent=None, comment: str = ''):
        # information of node
        self.button = None
        self.text_fig = None
        self.parent: Node = parent
        self.ID = ID
        self.text = text
        self.fontsize = fontsize
        self.figsize = figsize
        self.dpi = dpi
        self.height = 0
        self.width = 0
        self.children = []
        # attribute of structure
        self.lines_all = lines_all
        self.num_of_children = num_of_children
        if lines_each_children is None:
            lines_each_children = []
        self.lines_each_children = lines_each_children
        self.link_point_parent = position
        self.first_half = 0.5
        self.second_half = 0.5
        self.selected = False
        # 预留功能
        self.comment = comment

    def draw_node(self, ax, show_ID, show_box, fontsize):
        # parameters of a rectangle which represents the bounding box of the text
        self.fontsize = fontsize
        centerX, centerY = self.link_point_parent[0] + self.width / 2, self.link_point_parent[1]
        self.left, self.bottom = self.link_point_parent[0], self.link_point_parent[1] - self.height / 2
        self.right, self.top = self.link_point_parent[0] + self.width, self.link_point_parent[1] + self.height / 2

        # draw text
        self.text_fig = ax.text(centerX, centerY, self.text,
                                horizontalalignment='center',
                                verticalalignment='center',
                                fontsize=self.fontsize, color='black',
                                fontweight='heavy',
                                # fontfamily='SimHei',
                                transform=ax.transAxes,
                                bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0)
                                )

        # draw the rectangle in axes coords
        if show_box:
            # p = patches.Rectangle(
            #     (left, bottom), self.width, self.height,
            #     fill=False, transform=ax.transAxes, clip_on=False
            # )
            # ax.add_patch(p)
            props = {'boxstyle': "round,pad=0.3",
                     'facecolor': 'white',
                     'linestyle': 'solid',
                     'linewidth': 1,
                     # 'edgecolor': (30/255, 144/255, 255/255, 1),
                     'edgecolor': 'black',
                     'alpha': 1}
            self.text_fig.set_bbox(props)
        # else:
        #     self.text_fig.set_bbox(dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0, ))
        # draw ID
        elif self.selected:
            props = {'boxstyle': "round,pad=0.3",
                     'facecolor': 'white',
                     'linestyle': 'solid',
                     'linewidth': 1,
                     # 'edgecolor': (30/255, 144/255, 255/255, 1),
                     'edgecolor': 'red',
                     'alpha': 1}
            self.text_fig.set_bbox(props)

        if show_ID:
            ax.text(self.left, self.top, str(self.ID),
                    horizontalalignment='right',
                    verticalalignment='top',
                    fontsize=self.fontsize, color='black',
                    fontweight='heavy',
                    # fontfamily='SimHei',
                    transform=ax.transAxes)

        # self.button = Button(Axes(ax.figure, [0.2, 0.5, 20, 20]), '哈哈哈')
