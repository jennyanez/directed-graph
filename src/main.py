from graph import Graph, Node, Edge
from window import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox

import os
import sys
import networkx as nx
import matplotlib.pyplot as plt


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.graph = Graph()

        #Button connections
        self.add_node_pushButton.clicked.connect(self.add_node)
        self.add_edge_pushButton.clicked.connect(self.add_edge)
        self.edit_node_pushButton.clicked.connect(self.edit_node)
        self.edit_edge_pushButton.clicked.connect(self.edit_edge)
        self.del_node_pushButton.clicked.connect(self.delete_node)
        self.del_edgepushButton.clicked.connect(self.delete_edge)
        self.clear_pushButton.clicked.connect(self.clear)
        self.import_pushButton.clicked.connect(self.import_graph)
        self.export_pushButton.clicked.connect(self.export_graph)
        self.depth_pushButton.clicked.connect(self.in_depth) 
        self.breadth_pushButton.clicked.connect(self.in_breadth)


    #Methods for connections
    def draw(self):
        g = self.graph
        if len(g.get_graph_nodes()) == 0:
            self.label_graph.clear()
            return
        aux = nx.DiGraph()
        for node in g.get_graph_nodes():
            aux.add_node(node.get_value())

        for edge in g.get_graph_edges():
            n_weight = edge.weight
            aux.add_edge(str(edge.get_node1()), str(edge.get_node2()), weight=n_weight)

        options = {
            'node_color': '#126782',
            'node_size': 1000,
            'width': 1,
            'font_size': 12,
            'font_color': 'black',
            'font_family':"sans-serif",
            'edge_color':'black',
            'arrowstyle': "->"
        }

        pos = nx.planar_layout(aux)
        nx.draw_networkx(aux, pos, with_labels=True, font_weight='light', **options)
        labels = nx.get_edge_attributes(aux, 'weight')
        nx.draw_networkx_edge_labels(aux, pos, edge_labels=labels)

        plt.axis("off")
        plt.savefig("graph_img.png", dpi=300, format='png')
        pixmap = QPixmap("graph_img.png").scaled(500, 500)
        self.label_graph.setPixmap(pixmap)
        os.remove("graph_img.png")
        plt.close()


    def fill_all_comboBoxes(self):
        self.edit_node_comboBox_3.clear()
        self.e_dest_node_comboBox.clear() 
        self.e_initial_node_comboBox.clear()  
        self.edit_edge_old_comboBox.clear()
        self.edit_edge_newDest_comboBox.clear()
        self.del_node_comboBox_6.clear()
        self.del_edge_comboBox.clear()
        self.depth_first_node_comboBox.clear() 
        self.breadth_node_comboBox.clear() 
        self.label_graph.clear()
        self.path_label.setText('')

        if len(self.graph.get_graph_nodes()) != 0:
            for node in self.graph.get_graph_nodes():
                self.edit_node_comboBox_3.addItem(str(node.get_value()))
                self.edit_edge_newDest_comboBox.addItem(str(node.get_value()))
                self.del_node_comboBox_6.addItem(str(node.get_value()))
                self.depth_first_node_comboBox.addItem(str(node.get_value())) 
                self.breadth_node_comboBox.addItem(str(node.get_value())) 
                self.e_initial_node_comboBox.addItem(str(node.get_value())) 
                self.e_dest_node_comboBox.addItem(str(node.get_value())) 
            
            if len(self.graph.get_graph_edges()) != 0:
                for edge in self.graph.get_graph_edges():
                    self.edit_edge_old_comboBox.addItem(str(edge.get_node1()) + '->' + str(edge.get_node2()) + '; ' + str(edge.weight))
                    self.del_edge_comboBox.addItem(str(edge.get_node1()) + '->' + str(edge.get_node2()) + '; ' + str(edge.weight))

            self.draw()


    def add_node(self):
        value = self.new_node_textEdit.toPlainText()

        if len(value) != 0 and value.isspace() == False:
            if value not in self.graph.get_graph_nodes():
                node = Node(value)
                self.graph.add_node(node)
                self.new_node_textEdit.setText('')
                self.fill_all_comboBoxes()
            else:
               QMessageBox.warning(self, 'Warning', 'This node already exists.') 
        else:
            QMessageBox.warning(self, 'Warning', 'You must enter a value.')
            self.new_node_textEdit.setText('')


    def add_edge(self):
        node1 = str(self.e_initial_node_comboBox.currentText())
        node2 = str(self.e_dest_node_comboBox.currentText())
        weight = self.weight_spinBox.value()

        if node1 != '' and node2 != '':
            edge = Edge(Node(node1), Node(node2), weight)
            if edge not in self.graph.get_graph_edges():
                self.graph.add_edge2(edge)
                self.fill_all_comboBoxes()
            else:
                QMessageBox.warning(self, 'Warning', 'This edge already exists.') 
        else:
            QMessageBox.warning(self, 'Warning', 'The graph is empty. Or make sure they are at least 2 nodes')


    def edit_node(self):
        node1 = self.edit_node_comboBox_3.currentText()
        new_value = self.node_new_val_textEdit.toPlainText()

        if node1 != '':
            if len(new_value) != 0 and new_value.isspace() == False:
                if new_value not in self.graph.get_graph_nodes():
                    self.graph.edit_node_info(node1, new_value)
                    self.fill_all_comboBoxes()
                else:
                    QMessageBox.warning(self, 'Warning', 'This node already exists.')
        else:
            QMessageBox.warning(self, 'Warning', 'You must enter a value. Or make sure the graph is not empty')


    def edit_edge(self):
        index = self.edit_edge_old_comboBox.currentIndex()
        new_destiny = self.edit_edge_newDest_comboBox.currentText()

        if index != -1 and new_destiny != -1:
            node1 = self.graph.get_graph_edges()[index].get_node1()
            node2 = self.graph.get_graph_edges()[index].get_node2()
            new_weight = self.edit_edge_new_weight_spinBox.value()
            
            self.graph.edit_edge_connection(node1, node2, new_destiny, new_weight)

            self.fill_all_comboBoxes()
        else:
          QMessageBox.warning(self, 'Warning', 'The graph is empty')


    def delete_node(self):
        node = self.del_node_comboBox_6.currentText()
        if len(node) != 0 and node.isspace() == False:
            reply = QMessageBox.question(self, 'Warning', 'Are you sure you want to delete this node?', QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.graph.delete_node(node)
                self.fill_all_comboBoxes()
        else:
            QMessageBox.warning(self, 'Warning', 'The graph is empty.')


    def delete_edge(self):
        index = self.del_edge_comboBox.currentIndex()
        if index != -1:
            reply = QMessageBox.question(self, 'Warning', 'Are you sure you want to delete this edge?', QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.graph.delete_edge(self.graph.get_graph_edges()[index])
                self.fill_all_comboBoxes()
        else:
            QMessageBox.warning(self, 'Warning', 'The graph is empty.')

    def in_depth(self):
        if len(self.graph.get_graph_nodes()) != 0:
            node = self.depth_first_node_comboBox.currentText()
            if node != -1:
                path = []
                for n in self.graph.in_depth_iterator(node):
                    path.append(str(n)) 
                self.path_label.setText('In depth-first search starting by node '+ str(node) + ': ' + str(path))        
        else:
            QMessageBox.warning(self, 'Warning', 'The graph is empty.')


    def in_breadth(self):
        if len(self.graph.get_graph_nodes()) != 0:
            node = self.breadth_node_comboBox.currentText()
            if node != -1:
                path = []
                for n in self.graph.in_breadth_iterator(node):
                    path.append(str(n)) 
                self.path_label.setText('In breadth-first search starting by node '+ str(node) + ': ' + str(path))        
        else:
            QMessageBox.warning(self, 'Warning', 'The graph is empty.')


    def import_graph(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', './results')

        if os.stat(file_path).st_size == 0:
            QMessageBox.warning(self, 'Warning', 'The .txt is empty.')
        
        g = Graph()

        f = open(file_path, 'r')
        
        while f:
            line = f.readline()

            if line == '':
                break

            if line.startswith('Node: '):
                l = line.split()
                node = l[1]
                g.add_node(Node(node))
            
            else:
                l = line.split('; ')
                node1 = l[0]
                node2 = l[1]
                weight = int(l[2])
                g.add_edge(Node(node1), Node(node2), weight)

        f.close()
        self.graph = g
        self.fill_all_comboBoxes()


    def export_graph(self):
        if len(self.graph.get_graph_nodes()) == 0:
           QMessageBox.information(self, 'Information', 'The graph is empty.') 
        else:
            self.graph.export_graph()
            QMessageBox.information(self, 'Information', 'The graph has been saved as "graph.txt".')
            

    def clear(self):
        reply = QMessageBox.question(self, 'Warning', 'Are you sure you want to clear the graph?', QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.graph.clear_graph()
            self.fill_all_comboBoxes()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    window.showMaximized()

    sys.exit(app.exec_())