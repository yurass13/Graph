from base_objects import Edge, Node

# TODO test_edge_creation 
CASES = []

def test_edge_cretion():
    message = ""
    for case in CASES:
        try:
            # TODO Edge test
            passed = True
        except Exception as exception:
            passed = False
            message = exception
        finally:
            assert passed, f"Some shit!{message}"


def test_edge_add_del_args():
    edge = Edge(Node(2), Node('name', k = 2), "KekEdge", True, val = 2)
    expected = "KekEdge\n2 -> name : {'val': 2}"
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

    assert edge.__repr__() == expected and addition and deletion, f"add: {addition}, del: {deletion}\ntake: {edge}\nexpects:\n{expected}" 