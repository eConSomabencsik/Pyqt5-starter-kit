"""Factory for creating a GUI element."""

from typing import Callable, Dict, Any
from window.element import Element

element_creator_funcs: Dict[str, Callable[..., Element]] = {}

def register(element_name: str, creator_func: Callable[..., Element]) -> None:
    """Register a new GUI element."""
    element_creator_funcs[element_name] = creator_func


def unregister(element_name: str) -> None:
    """Unregister a GUI element."""
    element_creator_funcs.pop(element_name, None)


def create(arguments: Dict[str, Any]) -> Element:
    """Create a GUI element of a specific name, given JSON data."""
    args_copy = arguments.copy()
    element_name = args_copy.pop("name")
    try:
        creator_func = element_creator_funcs[element_name]
    except KeyError:
        raise ValueError(f"unknown element name {element_name!r}") from None
    return creator_func(**args_copy)