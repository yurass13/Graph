from typing import Any, Dict, List

from copy import deepcopy

from base_objects import Node


_lamb =  lambda x: x/2
CASES:List[Dict[str, Any]] = [
        # Without attrs, name type - int
        {
            'proto': {
                'name' : 2
            },
            'require_str' : "2: {}"},
        # One attr with type - str, name type - str
        {
            'proto':{
                'name' : 'a',
                'f1': 'f1 str attribute'
            },
            'require_str' : "a: {'f1': 'f1 str attribute'}"},
        # many attrs with different types.
        {
            'proto':{
                'name' : "name with spaces",
                'lambda' : _lamb,
                'dict' : {'i': {'j': {'k': {}}}},
                'tuple':(1, [1,2,3]),
                'class': object
            },
            'require_str' : "(name with spaces): {'lambda': " + 
                            f"{_lamb}" + 
                            ", 'dict': {'i': {'j': {'k': {}}}}, " +
                            "'tuple': (1, [1, 2, 3]), 'class': <class 'object'>}"
        },
    ]


def test_node_creation() -> None:

    info = dict()

    for index, case in enumerate(CASES):
        try:
            # Create object
            node = Node(**deepcopy(case['proto']))

            # Save objects for other tests
            case['node_exemplar'] = node

        except Exception as exception:
            info[index] = exception

        assert len(info) == 0, f"Failed cases info:\n{info}\n"


def test_node_name_repr() -> None:

    info = dict()

    for index, case in enumerate(CASES):
        try:

            # Node.attrs repr test
            if not case['require_str'] == f"{case['node_exemplar']}":
                raise ValueError("Node.__repr__() result is wrong!\n" +
                                 f"Value: {case['node_exemplar']}\n" +
                                 f"Expected: {case['require_str']}")

        except Exception as exception:
            info[index] = exception

    assert len(info) == 0, f"Failed cases info:\n{info}\n"


#---------------------------------------NameMixin--------------------------------------
def test_node_name_init_get() -> None:

    info = dict()

    for index, case in enumerate(CASES):
        try:
            # Node.name types test
            if not isinstance(case['node_exemplar'].name, str):
                raise TypeError("Node.name type is not str!" +
                                f"Current type: {type(case['node_exemplar'].name)}\n")

            # Node.name values test
            if not case['node_exemplar'].name == str(case['proto']['name']):
                raise ValueError("Node.name value is wrong!" +
                                 f"\nValue:{case['node_exemplar'].name}" +
                                 f"\nExpected:{case['proto']['name']}\n")

        except Exception as exception:
            info[index] = exception

        assert len(info) == 0, f"Failed cases info:\n{info}\n"


def test_node_name_set() -> None:
    # INFO Name.name property didn't has set method!
    node = Node('name should be immutable')

    is_immutable = False
    try:
        node.name = 'name changed' # type: ignore
    except AttributeError:
        is_immutable = True

    assert is_immutable and node.name == 'name should be immutable', node


#------------------------------------AttributesMixin-----------------------------------
def test_node_attrs_init_get() -> None:
    info = dict()

    for index, case in enumerate(CASES):
        try:
            attrs = deepcopy(case['proto'])
            del attrs['name']

            # Node.attrs test
            _node_attrs_comparing(case['node_exemplar'], attrs)

        except Exception as exception:
            info[index] = exception

        assert len(info) == 0, f"Failed cases info:\n{info}\n"


def test_node_iterable() -> None:
    _case = CASES[-1]
    node:Node = _case['node_exemplar']

    info = []

    try:
        expected_node_len:int = len(_case['proto']) - 1

        if not len(node) == expected_node_len:
            info.append({'len': f"\nTake:\n{len(node)}\nExpected:\n{expected_node_len}"})

    except AttributeError as exception:
        info.append({'len': str(exception)})

    try:
        attrs = deepcopy(_case['proto'])
        del attrs['name']
        
        if not list(iter(node)) == list(iter(attrs)):
            info.append({'iter': f"\nTake:\n{list(iter(node))}\nExpected:\n{list(iter(attrs))}"})
    except AttributeError as exception:
        info.append({'iter': str(exception)})

    assert len(info) == 0, f"Failed cases info:\n{info}\n"


def test_node_attrs_set() -> None:
    node = Node("n")
    expected:str = "n: {'val': 2}"
    _add:bool = False
    _del:bool = False
    info:List[Dict[str, str]] = []
    try:
        node['kwg'] = {'i': {'j': {'k': {}}}}
        node['val'] = 2
        _add = True
    except Exception as exception:
        info.append({'add': str(exception)})

    try:
        del node['kwg']
        _del = True
    except Exception as exception:
        info.append({'del': str(exception)})

    assert f'{node}' == expected and _add and _del, f"Errors:\n{info},\nTake:\n{node}\nExpected:\n{expected}"


#-----------------------------------Support Functions----------------------------------
def _node_attrs_comparing(node:Node, attrs:dict) -> bool:


    class ObjectsAreNotComparable(Exception):
        pass


    def is_equal(obj1, obj2) -> bool:
        if not type(obj1) == type(obj2):
            raise TypeError('attr type are not equal!')

        objects_equal = obj1 == obj2 or obj2 is None and obj1 is None

        if isinstance(obj1, (bool, int, float, complex)) and not objects_equal:
            return False

        if obj1 is obj2:
            return True

        if isinstance(obj1, (list, tuple, set)):
            return all([is_equal(*value) for value in zip(obj1, obj2)])
        elif isinstance(obj1, dict):
            if len(obj1.keys()) == 0 and len(obj2.keys()) == 0:
                # Empty dict
                return True
            if not obj1.keys() == obj2.keys():
                raise KeyError('node.attrs contains dict from sample' +
                                    'but keys are not equal!' + 
                                    f'\nInstance:{obj1}')

            obj2_values_by_obj1_keys = [obj2[key] for key in obj1]
            to_comparing = zip(obj1.values(), obj2_values_by_obj1_keys)
            for value1, value2 in to_comparing:
                if not is_equal(value1, value2):
                    raise ValueError('Dict element of node.attr is not equal!' +
                                        f'\nValue:{value1}')
            return True
        else:
            raise ObjectsAreNotComparable(f'node.attrs has object: {obj1} ' +
                                            f'with type:{type(obj1)}!')


    try:
        if not is_equal(node.attrs, attrs):
            raise ValueError('Type of attr is ok, but not a value!')
    except ObjectsAreNotComparable as exception:
        # TODO log warning here
        raise ObjectsAreNotComparable(exception)

    return False
