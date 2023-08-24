"""Module for constant type aliases and mixins."""

from typing import Any, Dict, Iterator, Optional

import re


NAME = str
PARAMS = Dict[str, Any]


class NameMixin:
    """ Interface Name - add :param name[get]: str
        NOTE name should be protected.
        NOTE try cast all types to str.
        NOTE name has brackets if it contains spacer literal:
            >>> named = Name('with space')
            >>> print(named.name)
            (with spase)
            ...
    """
    def __init__(self, name: NAME, *args, **kwargs) -> None:
        if isinstance(name, str):
            self._name = name
        else:
            self._name = str(name)


    @property
    def name(self) -> str:
        return self._name

    def __str__(self) -> str:
        if len(re.findall(r'\s', self.name)) > 0:
            return f"({self.name})"
        else:
            return f"{self.name}"


    def __repr__(self) -> str:
        if len(re.findall(r'\s', self.name)) > 0:
            return f"({self.name})"
        else:
            return f"{self.name}"


class AliasMixin(NameMixin):
    """Interface Alias(Name) - add :param alias[get, set]: str
        NOTE __str__ -> f"{alias if alias setted else ''}{Name.name}".
    """
    def __init__(self, name, alias, *args, **kwargs) -> None:
        NameMixin.__init__(self, name=name)
        self.alias = alias


    def __str__(self) -> str:
        return f"{'' if self.alias is None else self.alias}{super().__str__()}"


    def __repr__(self) -> str:
        return f"{'' if self.alias is None else self.alias}{super().__repr__()}"


# TODO should be sorted?
class AttributesMixin:
    """Interface Attributes - add descriptor attrs[get, set]: dict
        NOTE set object Iterable. Call iter - iterate attrs.
    """
    def __init__(self, **attrs: Optional[PARAMS]) -> None:

        if attrs is None:
            self.attrs:PARAMS = {}
        else:
            self.attrs= attrs


    def __len__(self) -> int:
        return len(self.attrs)


    def __getitem__(self, attr_name: str) -> Any:
        return self.attrs[attr_name]


    def __setitem__(self, attr_name: str, attr_value: Any) -> None:
        self.attrs[attr_name] = attr_value


    def __delitem__(self, attr_name: str) -> None:
        del self.attrs[attr_name]


    def __contains__(self, attr_name: str) -> bool:
        return attr_name in self.attrs


    def __iter__(self) -> Iterator[str]:
        return iter(self.attrs)


    def __str__(self) -> str:
        return f"{self.attrs}"


    def __repr__(self) -> str:
        return f"{self.attrs}"
