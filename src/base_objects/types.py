"""Module for constant type-aliases."""
from __future__ import annotations

from typing import Any, Dict, Iterator, Optional, TypeVar

NAME = str
PARAMS = Dict[str, Any]


# TODO Rewrite Nodes, Edges using dataclasses as model
# TODO Create controllers for Attributed objects
# TODO Controller must have logic for work with attributes in all models.(controller.attr['some_attr'].apply() or ect)

class BaseAttributed:
    
    def __init__(self, name: NAME, **attributes: Optional[PARAMS]) -> None:
        self.name: NAME = name if isinstance(name, str) else str(name)
        self.attrs: PARAMS = attributes if attributes is not None else {}


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
        return f"{self.name} : {self.attrs}"


    def __repr__(self) -> str:
        return f"{self.name} : {self.attrs}"

A = TypeVar('A', bound=BaseAttributed)
