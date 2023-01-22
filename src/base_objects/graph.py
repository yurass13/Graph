"""
#TODO
"""
# import pandas as pd

from .edge import Edge
from .node import Node


class Graph:
    def __init__(self):
        self._nodes = set()
        self._edges = set()


    def add_node(self, node:str|int|Node, **kwargs) -> None:
        """Add node with their attributes to the **Graph**.

        Args:
            node (str | int | Node): node for addition
        """
        try:
            self._nodes.add(
                node if isinstance(node, Node) else Node(node, kwargs=kwargs)
            )
        except Exception as ex:
            print(ex)


    def add_nodes(self, nodes:list|tuple|dict|str|int, attributes:list|tuple=None):
        """Add nodes with their attributes from container to the **Graph**.

        Args:
            nodes (list|tuple|dict):
                container with nodes or their names.

            attributes (list|tuple|dict, optional):
                container with attributes for nodes.
                Defaults to **None**.

        Examples:
            _summary_ #TODO
        """
        if isinstance(nodes, (list, tuple, str, int)):
            if isinstance(nodes, int):
                nodes = range(nodes)
            try:
                if len(attributes) > len(nodes):
                    raise ValueError("Attributes len bigger than nodes!")
            except TypeError:
                for _node in nodes:
                    self.add_node(_node)
            except Exception as ex:
                print(ex)
            else:
                for _node, _attributes in zip(nodes, attributes):
                    self.add_node(_node, kwargs=_attributes)

        else:
            for _name, _attributes in nodes.items():

                self.add_node(
                    _name, 
                    _attributes
                )
            



    def node_exist(self, node:int|str|Node):
        if isinstance(node, (int|str)):
            return node in [node.name for node in self._nodes]



    def _init_strategy(self, data) -> object:
        # TODO
        if data is None:
            pass


    def __repr__(self) -> str:
        return str(
            f'_______________Edges_______________\n{_delegate_str_convertation(self._edges)}\n' +
            f'_______________Nodes_______________\n{_delegate_str_convertation(self._nodes)}\n'
        )


def _delegate_str_convertation(container:list|tuple|set) -> str:
    """_summary_ #TODO

    Args:
        container (_type_): _description_ 
    """
    return '\n'.join(map(str, container))


# def simple_graph_generator(graph:Graph, node_count:int, edge_count:int) -> None:
#     """Init graph by randomly named $node_count$ nodes and random $edge_count$ edges."""
#     for 