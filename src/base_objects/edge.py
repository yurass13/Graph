from node import Node


class Edge:
    def __init__(self, *nodes, **attributes):
        if isinstance(nodes, [list, tuple, set]):
            left_node, right_node = nodes
            self.nodes = (Node(left_node), Node(right_node))
        elif nodes is None:
            return None
        else: 
            raise Exception('Wrong count of nodes')
        
