import sys

from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
from PySide2.QtWidgets import QApplication, QMessageBox, QGraphicsView
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QGraphicsScene
from PySide2.QtWidgets import QInputDialog, QLineEdit
from PySide2.QtCore import Slot
from PySide2.QtWidgets import QMainWindow, QFileDialog
import pickle

from graph import Graph


class ApplicationWindow:
    def __init__(self):
        loader = QUiLoader()
        # 加载之前新建的ui文件
        self.ui = loader.load("./ui/main.ui")
        self.figsize = (18, 9)
        self.dpi = 100
        self.show_ID = True
        self.show_box = False
        self.graph_canvas = FigureCanvas(Figure(figsize=self.figsize, dpi=self.dpi))
        self._graph = Graph(self.figsize, self.dpi)
        self.filename = None
        # self._graph.create_test()
        self._graph.draw(ax=self.graph_canvas.figure.add_axes([0, 0, 1, 1]),
                         show_ID=self.show_ID, show_box=self.show_box)
        self.graphicsScene = QGraphicsScene()  # 创建一个QGraphicsScene
        self.graphicsScene.addWidget(self.graph_canvas)
        self.ui.graph.setScene(self.graphicsScene)
        # self.ui.graph.setViewportUpdateMode(QGraphicsView.ViewportUpdateMode.MinimalViewportUpdate)
        # self.ui.graph.show()

        self.ui.selected_node.addItem('0')
        self.ui.add_button.clicked.connect(self._add_button_down)
        self.ui.delete_button.clicked.connect(self._delete_button_down)
        self.ui.update_button.clicked.connect(self._update_button_down)
        self.ui.actionSaveAs.triggered.connect(self._save_as)
        self.ui.actionLoad.triggered.connect(self._load)
        self.ui.actionSave.triggered.connect(self._save)
        self.ui.actionNew.triggered.connect(self._new)
        self.ui.actionExport.triggered.connect(self._export)
        self.ui.actionDisplay_Boxes.toggled.connect(self._is_display_boxes)
        self.ui.actionDisplay_Indexes.toggled.connect(self._is_display_indexes)

    @Slot()
    def _is_display_indexes(self):
        self.show_ID = self.ui.actionDisplay_Indexes.isChecked()
        self._redraw()

    @Slot()
    def _is_display_boxes(self):
        self.show_box = self.ui.actionDisplay_Boxes.isChecked()
        self._redraw()

    def _redraw(self):
        del self.graph_canvas
        self.graph_canvas = FigureCanvas(Figure(figsize=self.figsize, dpi=self.dpi))
        self._graph.draw(ax=self.graph_canvas.figure.add_axes([0, 0, 1, 1]),
                         show_ID=self.show_ID, show_box=self.show_box)
        self.graphicsScene.clear()
        self.graphicsScene.addWidget(self.graph_canvas)

    @Slot()
    def _new(self):
        del self._graph
        self._graph = Graph(self.figsize, self.dpi)
        self.filename = None
        self.ui.selected_node.clear()
        self.ui.selected_node.addItem('0')
        self._redraw()

    @Slot()
    def _load(self):
        fileDir, _ = QFileDialog.getOpenFileName(QMainWindow(), "选择文件", '', 'Siweidaotu files(*.graph)')
        if not fileDir:
            return
        self.filename = fileDir
        with open(fileDir, 'rb') as f:
            del self._graph
            self._graph = pickle.load(f)
            self.ui.selected_node.clear()
            for node in self._graph.nodes_dict:
                if node is not None:
                    self.ui.selected_node.addItem(str(node.ID))
            self._redraw()

    @Slot()
    def _save(self):
        if self.filename is not None:
            with open(self.filename, 'wb') as f:
                try:
                    pickle.dump(self._graph, f)
                except Exception:
                    QMessageBox.critical(
                        self.ui,
                        '失败',
                        '未知错误')
        else:
            self._save_as()

    @Slot()
    def _save_as(self):
        # 选择目录，返回选中的路径
        # fileDir = QFileDialog.getExistingDirectory(QMainWindow(), "选择存储路径")
        # fileDir = QFileDialog.getOpenFileName(QMainWindow(), "选择文件")
        fileDir, _ = QFileDialog.getSaveFileName(None, '保存', '', 'Siweidaotu files(*.graph);;All files(*)')
        if not fileDir:
            return
        self.filename = fileDir
        with open(fileDir, 'wb') as f:
            try:
                pickle.dump(self._graph, f)
            except IOError:
                QMessageBox.critical(
                    self.ui,
                    '失败',
                    '写入失败')
            except Exception:
                QMessageBox.critical(
                    self.ui,
                    '失败',
                    '未知错误')
            else:
                QMessageBox.information(
                    self.ui,
                    '成功',
                    '已保存')

    @Slot()
    def _export(self):
        fileDir, _ = QFileDialog.getSaveFileName(None, '保存', '', '.png(*.png);;.jpg(*.jpg)')
        if not fileDir:
            return
        self.graph_canvas.figure.savefig(fileDir)

    @Slot()
    def _add_button_down(self):
        text, ok_pressed = QInputDialog.getText(
            self.ui.add_button,
            "请输入内容",
            "",
            QLineEdit.Normal,
        )
        # print(text, ok_pressed)
        if ok_pressed:
            idx_node = int(self.ui.selected_node.currentText())
            new_idx = self._graph.create_node(idx_node, text)
            self.ui.selected_node.addItem(str(new_idx))
            self._redraw()
            # print(self.graphicsScene.items())
            # self.graphicsScene.
            # self.graphicsScene.update()
            # self.ui.graph.viewport().update()

            # self.ui.delete_button.deleteLater()
            # del self.ui.delete_button

    @Slot()
    def _delete_button_down(self):
        idx_node = int(self.ui.selected_node.currentText())
        if idx_node == 0:
            QMessageBox.critical(
                self.ui,
                '错误',
                '不能删除根节点！')
            return
        self._graph.delete_node(idx_node)
        self.ui.selected_node.removeItem(self.ui.selected_node.currentIndex())
        self._redraw()

    @Slot()
    def _update_button_down(self):
        text, ok_pressed = QInputDialog.getText(
            self.ui.add_button,
            "请输入内容",
            "",
            QLineEdit.Normal,
        )
        # print(text, ok_pressed)
        if ok_pressed:
            idx_node = int(self.ui.selected_node.currentText())
            self._graph.update_node(idx_node, text)
            self._redraw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = ApplicationWindow()
    mainwindow.ui.show()
    app.exec_()
