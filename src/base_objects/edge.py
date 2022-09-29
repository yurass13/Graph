from base_objects.node import Node


class Edge:
    def __init__(self, left_node: Node, right_node: Node, alias = None, **attributes):
        self.nodes = (left_node, right_node)

        if attributes is None:
            self.attrs = {}
        else:
            self.attrs = attributes

        self._set_alias(alias)
        

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
        return self._get_description_str()

    def __repr__(self):
        """Cast to str by programm."""
        return self._get_description_str()

    def _get_description_str(self):
        if self.__alias is None:
            return f"{str(self.nodes)} : {str(self.attrs)}"
        else:
            temp = {
                'left_node' : self.nodes[0],
                'right_node': self.nodes[1],
            }
            return f"{str(self.__alias)} : {str(temp | self.attrs)}"

    def _set_alias(self, alias):
        self.__alias = alias

    def _get_alias(self):
        return self.__alias

    def _del_alias(self):
        self.__alias = None

    alias = property(_get_alias, _set_alias, _del_alias)