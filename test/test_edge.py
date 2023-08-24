from base_objects import Edge, Node


CASES = [
    {
        'proto': {
            'nodes': (Node(1), Node('2'))
        },
        'require_str': "(1 == 2): {}"
    },
    {
        'proto': {
            'nodes': (Node(1), Node('2')),
            'alias': 'Named'
        },
        'require_str': "Named(1 == 2): {}"
    },
    {
        'proto': {
            'nodes': (Node(1), Node('2')),
            'alias': 'Named',
            'oriented': True
        },
        'require_str': "Named(1 -> 2): {}"
    },
    {
        'proto': {
            'nodes': (Node(1), Node('2')),
            'alias': 'Named',
            'oriented': True,
            'variable': 'some str',
            'class': object
        },
        'require_str': "Named(1 -> 2): {'variable': 'some str', 'class': <class 'object'>}"
    },
]


def test_edge_cretion():
    message = ""
    for case in CASES:
        try:
            for case in CASES:
                edge = Edge(**case['proto'])
                if not f'{edge}' == case['require_str']:
                    raise ValueError(f"node is \n{edge}\nbut expects\n{case['require_str']}")
            passed = True
        except Exception as exception:
            passed = False
            message = exception
        finally:
            assert passed, f"Creation failed with error!\n{message}"


def test_edge_name_with_orient_changed():
    nodes = Node(1), Node(2)
    edge = Edge(nodes=nodes)

    # after
    edge.is_oriented=True
    assert f'{edge}' == '(1 -> 2): {}'


def test_edge_add_n_del_attrs():
    nodes = Node(2), Node('name_node', k = 2)
    edge = Edge(
        nodes=nodes,
        alias="KekEdge",
        oriented=True,
        val = 5
    )
    expected = "KekEdge(2 -> name_node): {'val': 5}"
    try:
        edge['kwg'] = {'i': {'j': {'k': {}}}}
        addition = True
        try:
            del edge['kwg']
            deletion = True
        except:
            deletion = False
    except:
        addition = False

    assert f'{edge}' == expected and addition and deletion, f"add: {addition}, del: {deletion}\ntake: {edge}\nexpects:\n{expected}" 


def test_edge_property_nodes():
    edge = Edge((Node('some text', power = 'F'), Node(321, power = 'A')))

    is_avaliable = False
    if isinstance(edge.left_node, Node) and  isinstance(edge.right_node, Node):
        is_avaliable = True

    is_immutable = False
    try:
        edge.left_node = ''
    except AttributeError:
        try:
            edge.right_node = ''
        except AttributeError:
            is_immutable = True

    assert is_avaliable and is_immutable, f"Edge:{edge}:\n\tis_avaliable: {is_avaliable},\n\t is_immutable: {is_immutable}."
