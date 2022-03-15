########### CLASS NODE ##########
class Node:
    def __init__(self, value):
        self.value = value


    def get_value(self):
        return str(self.value)


    def __str__(self) -> str:
        return str(self.value)


    def __eq__(self, __o: object):
        return self.value == __o

############ CLASS EDGE ############
class Edge:
    def __init__(self, node1, node2, weight=0):
        self.weight = weight
        self.nodes = [node1, node2]  


    def get_nodes(self) -> list:
        return self.nodes


    def get_node1(self):
        return self.get_nodes()[0]


    def get_node2(self):
        return self.get_nodes()[1]


    def __str__(self) -> str:
        return f'{self.get_node1()} ------{self.weight}-----> {self.get_node2()}'
        

    def __eq__(self, __o: object) -> bool:
        return (__o.get_node1()==self.get_node1()) and (__o.get_node2()==self.get_node2())

############ CLASS GRAPH ############
class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []


    def get_graph_nodes(self) -> list:
        return self.nodes 


    def get_graph_edges(self) -> list:
        return self.edges


    def add_node(self, node):
        if node not in self.nodes:
            self.nodes.append(Node(node))


    def add_edge(self, node1:Node, node2:Node, weight=1):
        edge = Edge(node1, node2, weight)
        if edge not in self.edges:
            self.edges.append(edge)


    def add_edge2(self, edge:Edge):
        if edge not in self.edges:
            if self.get_graph_edges().count(edge)==0:
                self.edges.append(edge)


    def delete_node(self, node):
        #using list comprehensions
        #i create a new list with the same values except the one i want to delete
        self.nodes = [n for n in self.nodes if n.get_value() != node]
        self.edges = [e for e in self.edges if node not in e.get_nodes()]


    def delete_edge(self, edge: Edge):
        if edge in self.get_graph_edges() and edge is not None:
           for e in self.get_graph_edges():
                if e==edge:
                    self.edges.remove(e) 


    def edit_node_info(self, node, new_info):
        if (node is not None) and (new_info is not None) and (new_info not in self.nodes):
            self.nodes = [Node(new_info) if n.get_value() == node else n for n in self.nodes]
            for e in self.edges:
                if e.get_node1() == node:
                    e.get_nodes()[0] = Node(new_info)
                elif e.get_node2() == node:
                    e.get_nodes()[1] = Node(new_info)


    def edit_edge_connection(self, node1, node2, new_node2, n_weight:int):
        if (node1 is not None) and (node2 is not None):
            for e in self.edges:
                if (e.get_node1() == node1) and (e.get_node2() == node2):
                    if (new_node2 is not None) and (new_node2 in self.nodes):
                        if self.get_graph_edges().count(e)==1 and new_node2!=node2:
                            e.get_nodes()[1] = Node(new_node2)
                        e.weight = n_weight
                    

    def in_breadth_iterator(self, node) -> list:
        visited = []
        queue = []

        queue.append(node)

        while (queue):
            node = queue.pop(0)

            if node not in visited:
                visited.append(node)
                    
                for e in self.edges:
                    if e.get_node1() == node:
                        n = e.get_node2()
                        if n not in queue:
                            queue.append(n)
        return visited


    def in_depth_iterator(self, node) -> list:
        visited = []
        stack = []

        stack.append(node)

        while(stack):
            node = stack.pop()

            if node not in visited:
                visited.append(node)
                
                nodes_l = []
                
                for e in self.edges:
                    if e.get_node1() == node:
                        nodes_l.append(e.get_node2())
                nodes_l.reverse()
                stack.extend(nodes_l)                      

        return visited


    # the output will be -> 'A; B; 1' (for edges)
    # and -> 'Node: A' (for nodes)
    # nodes after edges
    def export_graph(self):
        with open('graph.txt', mode='w', encoding='utf-8') as f:
            for edge in self.get_graph_edges():
                f.write(str(edge.get_node1()) + '; ' + str(edge.get_node2()) + '; ' + str(edge.weight) + '\n')
            for node in self.get_graph_nodes():
                f.write('Node: ' + node.get_value() + '\n')
        f.close()


    def clear_graph(self):
        self.edges.clear()
        self.nodes.clear()


########## TESTING ############
def run():
    graph = Graph()

    graph.add_node('A')
    graph.add_node('B')
    graph.add_node('C')
    graph.add_node('D')
    graph.add_node('E')
    graph.add_node('F')

    graph.add_node('G')
    graph.add_node('H')

    graph.add_edge('A', 'B', 1)
    graph.add_edge('A', 'C', 2)

    graph.add_edge('B', 'D', 3)
    graph.add_edge('B', 'E', 4)

    graph.add_edge('C', 'E', 5)

    graph.add_edge('F', 'C', 6)

    graph.add_edge('A', 'G', 7)
    graph.add_edge('G', 'H')


    for x in graph.edges:
        print(x)

    
    # graph.delete_node('F')
    # graph.edit_edge_connection('F', 'C', 'A', 'E')

   # graph.delete_edge('B', 'E')

    # print("---------------------------------------")

    # for x in graph.edges:
    #     print(x)
    
    # for x in graph.nodes:
    #     print(x.get_value())

   # print(graph.in_breadth_iterator('A'))

    #print(graph.in_depth_iterator('A'))
    
    # graph.export_graph()
    # graph.import_graph()

    graph.clear_graph()

    for x in graph.edges:
        print(x)


if __name__=='__main__':
    run()
