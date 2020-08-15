from typing import Union, Iterable, TypeVar

from ._document import KanTeXDocument
from ._styles import FormattedBase, Bold

K = TypeVar('K')
V = TypeVar('V')


class Section:
    """A section header"""

    def __init__(self, *args: Union[V, 'SubSection'], indent: int = 4) -> None:
        self.header = Bold(args[0])
        self.items = [i for i in args[1:] if i]
        self.indent = indent

    def __add__(self, other: Union[V, 'Section']) -> 'MDTeXDocument':
        return KanTeXDocument(self, *other)

    def __str__(self) -> str:
        return '\n'.join([str(self.header)]
                         + [' ' * self.indent + str(item) for item in self.items
                            if item is not None])

    def append(self, item: Union[V, FormattedBase, 'SubSection']) -> None:
        """Append an item to the section"""
        self.items.append(item)

    def extend(self, items: Iterable) -> None:
        """Extend the section with a list of items"""
        self.items.extend(items)


class SubSection(Section):
    """A subsection Header"""

    def __init__(self, *args: Union[V, 'SubSubSection'], indent: int = 8) -> None:
        super().__init__(*args, indent=indent)


class SubSubSection(SubSection):
    """A subsubsection Header"""

    def __init__(self, *args: V, indent: int = 12) -> None:
        super().__init__(*args, indent=indent)


