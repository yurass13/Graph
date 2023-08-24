"""Module contins base objects for lib core."""
from __future__ import annotations
from typing import Any, Dict, Iterable, Literal, Optional, Tuple, Union

from .types import NAME, PARAMS, NameMixin, AliasMixin, AttributesMixin

from copy import deepcopy

from pandas import DataFrame

"""
TODO Refactor plan:
    - Refactor types.py:
        - Interface Name - add :param name[get]: str
            NOTE name should be protected.
            NOTE try cast all types to str.
            NOTE name has brackets if it contains spacer literal:
                >>> named = Name('with space')
                >>> print(named.name)
                (with spase)
                ...
        - Interface Alias(Name) - add :param alias[get, set]: str
            NOTE __str__ -> f"{alias}({name})" if alias setted.
        - Interface Attributes - add descriptor attrs[get, set]: dict
            NOTE set object Iterable. Call iter - iterate attrs.

    - Refactor test_node.py
        - Test Creation and node logic
            - Node(name, **attrs)
        - Tests for Name
        - Tests for Attributes

    - Refactor class Node(Name, Attributes)
        - init?
        - str, repr magic

    - Refactor test_edge.py
        - Test Creation and edge logic
            - Edge(nodes: Tuple(Node, Node),
                   alias: Optional[str],
                   oriented:bool = False,
                   **attrs)
            - :param is_oriented[get, set].
                NOTE :param name changing on :param oriented changed.
                NOTE when Edge is oriented mean than left_node -> right_node.
                    else left_node -> right_node and right_node -> left_node,
                    NOTE exclude situation, when left_node is right_node.
                        SAMPLE Edge.name -> f'({left_node} - LOOPED)'
            - Cast str and repr logic.
                NOTE name -> (Node.name -> Node.name) when oriented. 
                NOTE name -> (Node.name == Node.name) when NOT oriented. 
                str(edge)-> alias(name): {**attrs}
                str(edge)-> (name): {**attrs}
            - left_node[get], right_node[get] property.
        - Test for Alias, Name logic
        - Test for Attributes
    - Refactor class Edge(Alias, Attributes)
        - Check init.
        - Create left, right properties[get]
        - Relation literal strategy. (cls)
        - Name builder. (cls)
        - Overrite setter for :param name.
        - str, repr magic.
    - Create tests for graph.
        TODO test plan
    - Refactor(rewrite) class Graph.
        - Controller for nodes set. (descriptor)
            [add:uniq, del->del Edges, get]
            NOTE Node.name is unique.
            NOTE Node on delete should trigger check edges.
        - Controller for edges list. (descriptor).
            - dfs (generator)
            - bfs (generator)
            - indexing, searching alogorythms?
            - searching by name and by alias.
            NOTE Edge.alias is unique.
        - Contains states:
            - Update it on call single update. 
                TODO show warning that group methods in priority
                - push: total_old or pushed.
                - pop: total_old and poped: on change - full check.
            - Update it on group update. (priority)
                -||- 
            NOTE strategy by type input with decorator before call.
"""

class Node(NameMixin, AttributesMixin):
    """Base  Node class for graph.

    Parameters(from BaseAttributed):
        name: NAME - unique name of node.
        attrs: PARAMS - attributes of node.
    """
    def __init__(self, name:NAME,  **attributes: Optional[PARAMS]) -> None:
        NameMixin.__init__(self, name)
        AttributesMixin.__init__(self, **attributes)
        

    def __str__(self) -> str:
        return f"{NameMixin.__str__(self)}: {AttributesMixin.__str__(self)}"


    def __repr__(self) -> str:
        return f"{NameMixin.__repr__(self)}: {AttributesMixin.__repr__(self)}"


class Edge(BaseAttributed):
    """Graph edge Class
        __init__ from BaseAttributed - overrited.

    Params:
        left_node: Node
            When **is_orient** setted True means that it have link to **right_node**
                else means than they has relation.
        right_node: Node
            Second node.
        :param name:str - alias of Edge; using in all casts for str.
        :param is_oriented: bool, default: False
            When True set Edge to directed (change str cast from left_node to right_node).
        attributes: - another attributes of Edge.

    Note:
        After init call nodes saving in **<Edge>.nodes** as Tuple[(**left_node**, **right_node**)];
    """

    def __init__(
        self,
        left_node: Node,
        right_node: Node,
        alias: Optional[NAME] = None,
        is_oriented:bool = False,
        **attributes: Optional[PARAMS]
    ) -> None:
        self._oriented: bool = is_oriented

        self.nodes: Tuple[(Node, Node)] = (left_node, right_node)
        self.attrs: PARAMS = attributes if attributes is not None else {}

        self.alias = alias
        self.name = self.nodes[0].name + self.__get_relation_literal() + self.nodes[1].name


    def __get_relation_literal(self) -> Literal[' == '] | Literal[' -> ']:
        return ' -> ' if self._oriented else ' == '


    def is_orient(self) -> bool:
        return self._oriented


    def __repr__(self) -> str:
        if self.alias is None:
            return super().__repr__()
        else:
            return (
                self.alias + 
                f"\n{super().__repr__()}"
            )


    def __str__(self) -> str:
        if self.alias is None:
            return super().__str__()
        else:
            return (
                self.alias +
                '\n' +
                super().__str__()
            )


class Graph:
    def __init__(self) -> None:
        # TODO id, name or ect for Graph (if it'll be needed in view or spliting on subgraphs).
        self._nodes: set[Node] = set()
        self._edges: set[Edge] = set()
        return None


    def node_exist(self, node: NAME | Node) -> bool:
        if isinstance(node, Node):
            return node in self._nodes
        else:
            return node in [node.name for node in self._nodes]


    def add_node(
        self,
        node: Node | NAME,
        **kwargs: Optional[PARAMS]
    ) -> None:
        self._nodes.add(
            node if isinstance(node, Node) else Node(node, **deepcopy(kwargs))
        )


    def add_nodes(
        self,
        nodes: Iterable[Node | int] | str | int | Dict[NAME, PARAMS],
        attributes:Optional[Iterable[Any]] = None
    ) -> None:
        """Note: 
                1. Using **str** type for adding nodes means list of char.
                2. Using **int** type for adding nodes equlas using Generator: **range(int)**.
                3. Using Dict[NAME, PARAMS] for adding nodes means that attributes'll be ignored.
        """
        # TODO type-checker as strategy creation; chain of responce for creation.
        ...


    def __repr__(self) -> str:
        return self._object_list_view()


    def __str__(self) -> str:
        return self._object_list_view()


    def sample(self, node_len:int = 5, edge_len:int = 5, view_as:str = "obj") -> None:
        """View sample of Graph using type of view from view_as.

        Args:
            node_len int: count of nodes in sample for view.
                Defaults to 5.
            edge_len int: count of edges in sample for view.
                Defaults to 5.
        """
        # TODO strategy of graph view in sample.
        ...


    def _object_list_view(self) -> str:
        """Return str(Graph) as lists of contained Edges and Nodes."""
        return (
            f"_______________Graph_______________\n{self.__class__}" + 
            "\n_______________Edges_______________\n" + 
            '\n'.join(map(str, self._edges)) +
            "\n_______________Nodes_______________\n" +
            '\n'.join(map(str, self._nodes))
        )


    def _ident_matrix(self, ffill:Any = False, edge_key:Optional[str] = None) -> DataFrame:
        """Return pandas.DataFrame with ident matrix of graph."""
        _names = [node.name for node in self._nodes]
        _names.sort()
        df =  DataFrame(columns= _names, index= _names)

        for edge in self._edges:
            if edge_key is None:
                value = True
            else:
                value = edge[edge_key]
            df.loc[edge.nodes[0].name][edge.nodes[1].name] = value
            df.loc[edge.nodes[1].name][edge.nodes[0].name] = value
        
        return df.fillna(ffill)
