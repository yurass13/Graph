from node import Node


class Edge:
    def __init__(self, *nodes, **attributes):
        if isinstance(nodes, [list, tuple, set]):
            left_node, right_node = nodes
            self.nodes = (Node(left_node), Node(right_node))
        else:
            return None

        if attributes is None:
            self.attrs = {}
        else:
            self.attrs = attributes

    def __len__(self):
        """
        len()
        Returns:
            len(attrs) - lenght of attrs dict with attributes.
        """
        return len(self.attrs)

    def __getitem__(self, key):
        """get - method (self[key])"""
        return self.attrs[key]

    def __setitem__(self, key, value):
        """set - method (self[key] = value)"""
        self.attrs[key] = value

    def __delitem__(self, key):
        """del - method (del self[key])"""
        del self.attrs[key]

    def __contains__(self, key):
        """Contains (key in self)"""
        return key in self.attrs

    def __iter__(self):
        """Iter for attributes."""
        return iter(self.attrs)

    def __str__(self):
        """
        Cats to str by user

        Example:
            str(self)
        """
        return f"{str(self.nodes)} : {str(self.attrs)}"

    def __repr__(self):
        """Cast to str by programm."""
        return f"{str(self.nodes)} : {str(self.attrs)}"
