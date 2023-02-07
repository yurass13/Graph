from base_objects import Node

# TODO Refactor
lamb =  lambda x: x/2
CASES = [
        {
            'name' : '2',
            'kwgs' : {},
            'cretion_repr' : "2 : {}"},
        {
            'name' : 'a',
            'kwgs' : {'f1': 'f1 str attribute'},
            'cretion_repr' : "a : {'f1': 'f1 str attribute'}"},
        {
            'name' : 7,
            'kwgs' : {
                'lambda' : lamb,
                'dict' : {'i': {'j': {'k': {}}}},
                'tuple':(1, [1,2,3]),
                'object': object
            },
            'cretion_repr' : "7 : {'lambda': " + str(lamb) + ", 'dict': {'i': {'j': {'k': {}}}}, 'tuple': (1, [1, 2, 3]), 'object': <class 'object'>}"
        },
    ]

def test_node_cretion():
    message = ""
    for case in CASES:
        try:
            node = Node(case['name'], **case['kwgs'])
            if not isinstance(node.name, str):
                raise TypeError(f"node.name type is {type(node.name)}")
            if not node.__repr__() == case['cretion_repr']:
                raise ValueError(f"node.repr is \n{node.__repr__()}\nbut expects\n{case['cretion_repr']}")
            passed = True
        except Exception as exception:
            passed = False
            message = exception
        finally:
            assert passed, f"Some shit!{message}"


def test_node_add_del_args():
    node = Node("n")
    expected = "n : {'val': 2}"
    try:
        node['kwg'] = {'i': {'j': {'k': {}}}}
        node['val'] = 2
        addition = True
        try:
            del node['kwg']
            deletion = True
        except:
            deletion = False
    except:
        addition = False

    assert node.__repr__() == expected and addition and deletion, f"add: {addition}, del: {deletion}, \ntake:\n{node}\nexpects\n{expected}" 