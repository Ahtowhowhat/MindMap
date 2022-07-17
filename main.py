import pickle
import sys

from PySide2.QtCore import Qt
from PySide2.QtCore import Slot
# from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtWidgets import QGraphicsScene
from PySide2.QtWidgets import QInputDialog, QLineEdit
from PySide2.QtWidgets import QMainWindow, QFileDialog
from PySide2.QtWidgets import QWidget
# import matplotlib
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas)
from matplotlib.figure import Figure
from matplotlib.transforms import Bbox

from graph import Graph
from ui_main import Ui_MainWindow
from ui_editWindow import Ui_editWindow


# matplotlib.use('Agg')

class ApplicationWindow(QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        # loader = QUiLoader()
        # 加载之前新建的ui文件
        # self.ui = loader.load("./ui/main.ui")
        self.ui = Ui_MainWindow()
        self.editWindow = QWidget()
        self.editWight = Ui_editWindow()
        self.editWight.setupUi(self.editWindow)
        self.ui.setupUi(self)
        self.figsize = (12.8, 7.2)
        self.dpi = 100
        self.fontsize = 16
        self.show_ID = False
        self.show_box = False
        self.modified = False
        self.graph_canvas = FigureCanvas(Figure(figsize=self.figsize, dpi=self.dpi))
        self._graph = Graph(self.figsize, self.dpi, self.fontsize)
        self.filename = None
        self.ax = self.graph_canvas.figure.add_axes([0, 0, 1, 1])
        # self._graph.create_test()
        self._redraw()
        self.graphicsScene = QGraphicsScene()  # 创建一个QGraphicsScene
        self.graphicsScene.addWidget(self.graph_canvas)
        self.ui.graph.setScene(self.graphicsScene)
        # self.ui.graph.setViewportUpdateMode(QGraphicsView.ViewportUpdateMode.MinimalViewportUpdate)
        # self.ui.graph.show()
        self.ui.selected_node.addItem('0')
        self.ui.statusbar.showMessage(f'{self.filename if self.filename is not None else "Untitled"}', 0)
        # self.ui.selected_node.currentIndexChanged.connect(
        #     lambda: self.ui.statusbar.showMessage(f'Current node\'s ID : {self.ui.selected_node.currentText()}'))
        self.ui.add_button.clicked.connect(self._add_button_clicked)
        self.ui.delete_button.clicked.connect(self._delete_button_clicked)
        self.ui.update_button.clicked.connect(self._update_button_clicked)
        self.ui.actionSaveAs.triggered.connect(self._save_as)
        self.ui.actionLoad.triggered.connect(self._load)
        self.ui.actionSave.triggered.connect(self._save)
        self.ui.actionNew.triggered.connect(self._new)
        self.ui.actionExport.triggered.connect(self._export)
        self.ui.actionDisplay_Boxes.toggled.connect(self._is_display_boxes)
        self.ui.actionDisplay_Indexes.toggled.connect(self._is_display_indexes)
        self.ui.actionFigure_size.triggered.connect(self._set_fig_size)
        self.ui.actionFont_size.triggered.connect(self._set_font_size)
        self.ui.actionOptimize_position.triggered.connect(self._optimize_location)
        self.ui.up_button.clicked.connect(lambda: self._updown_button_clicked('up'))
        self.ui.down_button.clicked.connect(lambda: self._updown_button_clicked('down'))
        self.ui.comment_button.clicked.connect(self._comment_button_clicked)
        self.editWight.edit_ok_button.clicked.connect(self._edit_ok_button_clicked)
        self.graph_canvas.mpl_connect('button_press_event', self._click_node)
        # self.graph_canvas.mpl_connect('scroll_event', self._scroll)
        self.ui.graph.keyPressEvent = self.keyPressEvent

    # def _scroll(self, event):
    #     axtemp = event.inaxes
    #     x_min, x_max = axtemp.get_xlim()
    #     fanwei = (x_max - x_min) / 10
    #     if event.button == 'up':
    #         axtemp.set(xlim=(x_min + fanwei, x_max - fanwei))
    #         print('up')
    #     elif event.button == 'down':
    #         axtemp.set(xlim=(x_min - fanwei, x_max + fanwei))
    #         print('down')
    #     self.graph_canvas.draw()  # 绘图动作实时反映在图像上
    #     self._redraw(False)


    @Slot()
    def _comment_button_clicked(self):
        idx_node = int(self.ui.selected_node.currentText())
        self.editWight.commentEdit.setPlainText(self._graph.nodes_dict[idx_node].comment)
        # self.editWight.commentEdit.selectAll()
        # self.editWight.commentEdit.moveCursor()
        self.editWindow.show()
        # self._graph.nodes_dict[idx_node].comment = self.editWight.commentEdit.toPlainText()

    @Slot()
    def _edit_ok_button_clicked(self):
        idx_node = int(self.ui.selected_node.currentText())
        self._graph.nodes_dict[idx_node].comment = self.editWight.commentEdit.toPlainText()
        self.editWindow.close()
        self.modified = True

    def keyPressEvent(self, event):
        # # 这里event.key（）显示的是按键的编码
        # print("按下：" + str(event.key()))
        if QApplication.keyboardModifiers() == Qt.ControlModifier:
            if event.key() == Qt.Key_Up:
                self._updown_button_clicked('up')
            elif event.key() == Qt.Key_Down:
                self._updown_button_clicked('down')
            elif event.key() == Qt.Key_Left:
                self._move_to_parent_button_down()
            elif event.key() == Qt.Key_Right:
                self._move_to_child_button_down()
        else:
            if event.key() == Qt.Key_Up:
                self._select_node_with_direction_key('u')
            elif event.key() == Qt.Key_Down:
                self._select_node_with_direction_key('d')
            elif event.key() == Qt.Key_Left:
                self._select_node_with_direction_key('l')
            elif event.key() == Qt.Key_Right:
                self._select_node_with_direction_key('r')

    def _select_node_with_direction_key(self, direction):
        if self.ui.selected_node.currentIndex() == -1:
            return
        idx_node = int(self.ui.selected_node.currentText())
        ID = idx_node
        cur_node = self._graph.nodes_dict[idx_node]
        if direction == 'u':
            if cur_node.parent is None:
                return
            ID = cur_node.parent.children[cur_node.parent.children.index(cur_node) - 1].ID
        elif direction == 'd':
            if cur_node.parent is None:
                return
            ID = cur_node.parent.children[(cur_node.parent.children.index(cur_node) + 1)%cur_node.parent.num_of_children].ID
        elif direction == 'l':
            if cur_node.parent is None:
                return
            ID = cur_node.parent.ID
        elif direction == 'r':
            if cur_node.num_of_children == 0:
                return
            ID = cur_node.children[0].ID

        if ID == int(self.ui.selected_node.currentText()):
            return
        self.ui.statusbar.showMessage(f'{self._graph.nodes_dict[ID].comment}', 0)
        self._graph.nodes_dict[ID].selected = True
        self._graph.nodes_dict[int(self.ui.selected_node.currentText())].selected = False
        self.ui.selected_node.setCurrentIndex(self.ui.selected_node.findText(str(ID)))
        self._redraw(False)

    def _click_node(self, event):
        # transf = self.ax.transAxes.inverted()
        bbox = Bbox([[0, 0], [event.x, event.y]]).transformed(self.ax.transAxes.inverted())
        x, y = bbox.width, bbox.height

        # print(bbox.width, bbox.height)
        def search(root):
            # left, bottom = root.link_point_parent[0], root.link_point_parent[1] - root.height / 2
            # right, top = root.link_point_parent[0] + root.width, root.link_point_parent[1] + root.height / 2
            if root.left < x < root.right and root.bottom < y < root.top:
                root.selected = True
                return root.ID
            for node in root.children:
                ID = search(node)
                if ID is not None:
                    return ID
            return None

        ID = search(self._graph.root)
        if ID is not None:
            self.ui.statusbar.showMessage(f'{self._graph.nodes_dict[ID].comment}', 0)
            if self.ui.selected_node.currentIndex() == -1:
                self.ui.selected_node.setCurrentIndex(self.ui.selected_node.findText(str(ID)))
                self._redraw()
            else:
                if ID == int(self.ui.selected_node.currentText()):
                    return
                self._graph.nodes_dict[int(self.ui.selected_node.currentText())].selected = False
                self.ui.selected_node.setCurrentIndex(self.ui.selected_node.findText(str(ID)))
                self._redraw(False)
        else:
            self.ui.statusbar.showMessage(f'{self.filename if self.filename is not None else "Untitled"}', 0)
            if self.ui.selected_node.currentIndex() != -1:
                self._graph.nodes_dict[int(self.ui.selected_node.currentText())].selected = False
                self.ui.selected_node.setCurrentIndex(-1)
                self._redraw()
            # self._graph.nodes_list[int(self.ui.selected_node.currentText())].draw_node(
            #     self.ax, self.show_ID, self.show_box, self.fontsize)
            # self._graph.nodes_list[id].draw_node(
            #     self.ax, self.show_ID, self.show_box, self.fontsize)
            # self.graph_canvas.draw()

    @Slot()
    def _set_font_size(self):
        text, ok_pressed = QInputDialog.getText(
            self.ui.add_button,
            "Setting",
            "Please enter the font size",
            QLineEdit.Normal,
            f'{self.fontsize}'
        )
        # print(text, ok_pressed)
        if ok_pressed:
            self.fontsize = int(text)
            self._graph.fontsize = self.fontsize
            self._redraw()
            self.modified = True

    @Slot()
    def _set_fig_size(self):
        text, ok_pressed = QInputDialog.getText(
            self.ui.add_button,
            "Setting",
            "Please enter the figure size",
            QLineEdit.Normal,
            f"{int(self.figsize[0] * self.dpi):#d} {int(self.figsize[1] * self.dpi):#d}"
        )
        # print(text, ok_pressed)
        if ok_pressed:
            width, height = list(map(int, text.split()))
            self.figsize = (width / self.dpi, height / self.dpi)
            self._graph.figsize = self.figsize
            del self.graph_canvas
            self.graph_canvas = FigureCanvas(Figure(figsize=self.figsize, dpi=self.dpi))
            self.graph_canvas.callbacks.connect('button_press_event', self._click_node)
            self.ax = self.graph_canvas.figure.add_axes([0, 0, 1, 1])
            # self.graphicsScene.clear()
            # self.graphicsScene.addWidget(self.graph_canvas)
            self.graphicsScene.deleteLater()
            self.graphicsScene = QGraphicsScene()  # 创建一个QGraphicsScene
            self.graphicsScene.addWidget(self.graph_canvas)
            self.ui.graph.setScene(self.graphicsScene)
            self._redraw()
            self.modified = True

    @Slot()
    def _is_display_indexes(self):
        self.show_ID = self.ui.actionDisplay_Indexes.isChecked()
        self._redraw(False)

    @Slot()
    def _is_display_boxes(self):
        self.show_box = self.ui.actionDisplay_Boxes.isChecked()
        self._redraw(False)

    def _redraw(self, is_get_wh=True):
        # del self.graph_canvas
        # self.graph_canvas = FigureCanvas(Figure(figsize=self.figsize, dpi=self.dpi))
        if is_get_wh:
            self._graph.draw(ax=self.ax,
                             show_ID=self.show_ID, show_box=self.show_box)
            # self.graphicsScene.clear()
            # self.graphicsScene.addWidget(self.graph_canvas)
            self.graph_canvas.draw()
            self._graph.get_wh()
        self.ax.cla()
        self._graph.draw(ax=self.ax,
                         show_ID=self.show_ID, show_box=self.show_box)
        self.graph_canvas.draw()

    @Slot()
    def _new(self):
        if self.modified:
            msgBox = QMessageBox()
            msgBox.setWindowTitle('New')
            msgBox.setText("The document has been modified.")
            msgBox.setInformativeText("Do you want to save your changes?")
            msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
            msgBox.setDefaultButton(QMessageBox.Save)
            ret = msgBox.exec()
            if ret == QMessageBox.Save:
                if not self._save():
                    return
            elif ret == QMessageBox.Cancel:
                return

        del self._graph
        self.figsize = (12.8, 7.2)
        self.dpi = 100
        self._graph = Graph(self.figsize, self.dpi, self.fontsize)
        self.filename = None
        self.ui.statusbar.showMessage(f'{self.filename if self.filename is not None else "Untitled"}', 0)
        self.ui.selected_node.clear()
        self.ui.selected_node.addItem('0')
        del self.graph_canvas
        self.graph_canvas = FigureCanvas(Figure(figsize=self.figsize, dpi=self.dpi))
        self.graph_canvas.callbacks.connect('button_press_event', self._click_node)
        self.ax = self.graph_canvas.figure.add_axes([0, 0, 1, 1])
        # self.graphicsScene.clear()
        # self.graphicsScene.addWidget(self.graph_canvas)
        self.graphicsScene.deleteLater()
        self.graphicsScene = QGraphicsScene()  # 创建一个QGraphicsScene
        self.graphicsScene.addWidget(self.graph_canvas)
        self.ui.graph.setScene(self.graphicsScene)

        self._redraw()
        self.modified = False

    @Slot()
    def _load(self):
        if self.modified:
            msgBox = QMessageBox()
            msgBox.setText("The document has been modified.")
            msgBox.setInformativeText("Do you want to save your changes?")
            msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
            msgBox.setDefaultButton(QMessageBox.Save)
            ret = msgBox.exec()
            if ret == QMessageBox.Save:
                if not self._save():
                    return
            elif ret == QMessageBox.Cancel:
                return

        fileDir, _ = QFileDialog.getOpenFileName(QMainWindow(), "Choice file", '', 'Siweidaotu files(*.graph)')
        if not fileDir:
            return
        self.filename = fileDir
        self.ui.statusbar.showMessage(f'{self.filename if self.filename is not None else "Untitled"}', 0)
        with open(fileDir, 'rb') as f:
            del self._graph
            self._graph = pickle.load(f)
            self.ui.selected_node.clear()
            for idx, node in enumerate(self._graph.nodes_dict.values()):
                self.ui.selected_node.addItem(str(node.ID))
                if node.selected:
                    self.ui.selected_node.setCurrentIndex(idx)
            self.figsize = self._graph.figsize
            self.fontsize = self._graph.fontsize
            del self.graph_canvas
            self.graph_canvas = FigureCanvas(Figure(figsize=self.figsize, dpi=self.dpi))
            self.graph_canvas.callbacks.connect('button_press_event', self._click_node)
            self.ax = self.graph_canvas.figure.add_axes([0, 0, 1, 1])
            # self.graphicsScene.clear()
            # self.graphicsScene.addWidget(self.graph_canvas)
            self.graphicsScene.deleteLater()
            self.graphicsScene = QGraphicsScene()  # 创建一个QGraphicsScene
            self.graphicsScene.addWidget(self.graph_canvas)
            self.ui.graph.setScene(self.graphicsScene)
            self._redraw(False)
            self.modified = False

    @Slot()
    def _save(self):
        if self.filename is not None:
            with open(self.filename, 'wb') as f:
                try:
                    pickle.dump(self._graph, f)
                    self.ui.statusbar.showMessage(f'{self.filename if self.filename is not None else "Untitled"}', 0)
                    self.modified = False
                    return True
                except Exception:
                    QMessageBox.critical(
                        self,
                        'Failed',
                        'Unknown error')
                    return False
        else:
            return self._save_as()

    @Slot()
    def _save_as(self):
        # 选择目录，返回选中的路径
        # fileDir = QFileDialog.getExistingDirectory(QMainWindow(), "选择存储路径")
        # fileDir = QFileDialog.getOpenFileName(QMainWindow(), "选择文件")
        fileDir, _ = QFileDialog.getSaveFileName(None, 'Saving', '', 'Siweidaotu files(*.graph);;All files(*)')
        if not fileDir:
            return False
        self.filename = fileDir
        with open(fileDir, 'wb') as f:
            try:
                pickle.dump(self._graph, f)
                self.ui.statusbar.showMessage(f'{self.filename if self.filename is not None else "Untitled"}', 0)
                self.modified = False
                return True
            except IOError:
                QMessageBox.critical(
                    self,
                    'Failed',
                    'Failed to input')
            except Exception:
                QMessageBox.critical(
                    self,
                    'Failed',
                    'Unknown error')
            return False

    @Slot()
    def _export(self):
        fileDir, _ = QFileDialog.getSaveFileName(None, 'Saving', '', '.png(*.png);;.jpg(*.jpg)')
        if not fileDir:
            return
        self.graph_canvas.figure.savefig(fileDir)

    @Slot()
    def _add_button_clicked(self):
        text, ok_pressed = QInputDialog.getText(
            self.ui.add_button,
            "Adding",
            "Please enter the content",
            QLineEdit.Normal,
        )
        # print(text, ok_pressed)
        if ok_pressed:
            idx_node = int(self.ui.selected_node.currentText())
            new_idx = self._graph.create_node(idx_node, text)
            self.ui.selected_node.addItem(str(new_idx))
            self._redraw()
            self.modified = True
            # print(self.graphicsScene.items())
            # self.graphicsScene.
            # self.graphicsScene.update()
            # self.ui.graph.viewport().update()

            # self.ui.delete_button.deleteLater()
            # del self.ui.delete_button

    @Slot()
    def _delete_button_clicked(self):
        idx_node = int(self.ui.selected_node.currentText())
        if idx_node == 0:
            QMessageBox.critical(
                self,
                'Failed',
                'The root node cannot be deleted!')
            return
        self._graph.delete_node(idx_node, self.ui.selected_node)
        self._graph.nodes_dict[int(self.ui.selected_node.currentText())].selected = True
        self._redraw(False)
        self.modified = True

    @Slot()
    def _update_button_clicked(self):
        idx_node = int(self.ui.selected_node.currentText())
        text, ok_pressed = QInputDialog.getText(
            self.ui.add_button,
            "Updating",
            "Please enter the content",
            QLineEdit.Normal,
            self._graph.nodes_dict[idx_node].text
        )
        # print(text, ok_pressed)
        if ok_pressed:
            self._graph.update_node(idx_node, text)
            self._redraw()
            self.modified = True

    @Slot()
    def _updown_button_clicked(self, direction: str):
        idx_node = int(self.ui.selected_node.currentText())
        if idx_node == 0:
            return
        self._graph.move_node(idx_node, direction)
        self._redraw(False)
        self.modified = True

    @Slot()
    def _move_to_parent_button_down(self):
        idx_node = int(self.ui.selected_node.currentText())
        if idx_node == 0:
            return
        self._graph.move_node_to_parent(idx_node)
        self._redraw(False)
        self.modified = True

    @Slot()
    def _move_to_child_button_down(self):
        idx_node = int(self.ui.selected_node.currentText())
        if idx_node == 0:
            return
        self._graph.move_node_to_child(idx_node)
        self._redraw(False)
        self.modified = True

    @Slot()
    def _optimize_location(self):
        # long = max(self._graph.root.first_half, self._graph.root.second_half)
        # delta = (self._graph.root.first_half-self._graph.root.lines_all/2)*self._graph.root.height
        delta = (self._graph.root.first_half - self._graph.root.second_half) * self._graph.root.height
        # delta /= (self.figsize[1]*self.dpi)
        self._graph.root.link_point_parent = (self._graph.root.link_point_parent[0],
                                              0.5 - delta / 2)
        self._redraw(False)
        self.modified = True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = ApplicationWindow()
    mainwindow.show()
    app.exec_()
