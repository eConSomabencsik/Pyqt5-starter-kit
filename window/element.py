"""Represents a basic GUI element."""

from typing import Protocol

class Element(Protocol):
    """Basic representation of a gui part."""

    def setup_ui(self) -> None:
        """In this function put together the widgets."""
