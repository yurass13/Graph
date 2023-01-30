"""Module contins base objects for lib core."""
from __future__ import annotations
from typing import Any, Dict, Literal, Optional, Tuple, Iterable

from .types import BaseAttributed, NAME, PARAMS, A



class Node(BaseAttributed):
    """
    Base class of node object.

    Class Parameters:
        name: str - unique name of node.
        attrs: dict[str: [Any]] - attributes of node.
    """
    pass


class Edge(BaseAttributed):
    """Base Edge Class 
    :param is_oriented: Optional[bool] - when seted True only left node has link to right.
    """

    def __init__(
        self,
        left_node: Node,
        right_node: Node,
        name: Optional[NAME] = None,
        is_oriented:Optional[bool] = None,
        **attributes: Optional[PARAMS]
    ) -> None:
        self.__orient: bool = is_oriented if is_oriented is not None else False

        self.nodes:Tuple[(Node, Node)] = (left_node, right_node)
        self.attrs: PARAMS = attributes if attributes is not None else {}

        self.name = name if name is not None else str(self.nodes[0].name) + self.__get_relation_symbol() + str(self.nodes[1].name)


    def __get_relation_symbol(self) -> Literal[' == '] | Literal[' -> ']:
        return ' -> ' if self.__orient else ' == '


    def is_orient(self) -> bool:
        return self.__orient


class Graph:
    def __init__(self) -> None:
        self._nodes: set[Node] = set()
        self._edges: set[Edge] = set()
        return None


    def node_exist(self, node: NAME | Node) -> bool:
        if isinstance(node, Node):
            return node in self._nodes
        elif isinstance(node, NAME):
            return node in [node.name for node in self._nodes]
        else:
            raise ValueError(f'Using Incompartable type {type(node)} in node_exist(self, **node**)!')


    def add_node(
        self,
        node: Node | NAME,
        **kwargs: Optional[PARAMS]
    ) -> None:
        # TODO loosing objects attributes on use.
        self._nodes.add(
            node if isinstance(node, Node) else Node(node, **kwargs)
        )


    def add_nodes(
        self,
        nodes: Iterable[A | int] | str | int | Dict[NAME, PARAMS],
        attributes: Optional[Iterable[Any]]=None
    ) -> None:
        """Note: 
                1. Using **str** type for adding nodes means list of char.
                2. Using **int** type for adding nodes equlas using Generator: **range(int)**.
                3. Using Dict[NAME, PARAMS] for adding nodes means that attributes'll be ignored.
        """
        # TODO delegate creation; rewrite type-checkers; optimise order of operations.
        if isinstance(nodes, (list, tuple, set, str, int)):
            if isinstance(nodes, int):
                nodes = list(range(nodes))
            try:
                if attributes is None:
                    pass
                elif len(attributes) > len(nodes):
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


    def __repr__(self) -> str:
        return str(
            f'_______________Edges_______________\n{self._delegate_str_convertation(self._edges)}\n' +
            f'_______________Nodes_______________\n{self._delegate_str_convertation(self._nodes)}\n'
        )


    def __str__(self) -> str:
        return str(
            f'_______________Edges_______________\n{self._delegate_str_convertation(self._edges)}\n' +
            f'_______________Nodes_______________\n{self._delegate_str_convertation(self._nodes)}\n'
        )


    @staticmethod
    def _delegate_str_convertation(container:Iterable[A]) -> str:
        """_summary_ #TODO

        Args:
            container (_type_): _description_ 
        """
        return '\n'.join(map(str, container))