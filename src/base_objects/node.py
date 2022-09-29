"""Base class of node."""
class Node:
    """
    Base class of node object.

    Class Parameters:
        name - unique name of node.
        attrs - dict with attributes of node.
    """
    def __init__(self, name= None, **kwargs):
        """
        Init function

        Parameters:
            name - unique name of node.
            kwargs - attributes of node
        """
        self.name = name
        if kwargs is None:
            self.attrs = {}
        else:
            self.attrs = kwargs

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
        Cast to str by user

        Example:
            str(self)
        """
        return f"{str(self.name)} : {str(self.attrs)}"

    def __repr__(self):
        """Cast to str by programm."""
        return f"{str(self.name)} : {str(self.attrs)}"
