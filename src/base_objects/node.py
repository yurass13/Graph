class NodeCreator(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(NodeCreator, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Node:
    def __init__(self, name= None, **kwargs):
        self.name = name
        if kwargs is None:
            self.attrs = {}
        else:
            self.attrs = kwargs

    def __len__(self):
        return len(self.attrs)

    def __getitem__(self, key):
        return self.attrs[key]

    def __setitem__(self, key, value):
        self.attrs[key] = value

    def __delitem__(self, key):
        del self.attrs[key]

    def __contains__(self, key):
        return key in self.attrs

    def __iter__(self):
        return iter(self.attrs)

    def __str__(self):
        return f"{str(self.name)} : {str(self.attrs)}"

    def __repr__(self):
        return f"{str(self.name)} : {str(self.attrs)}"