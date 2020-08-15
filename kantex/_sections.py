from typing import Union, Iterable, TypeVar

from ._document import KanTeXDocument
from ._styles import FormattedBase, Bold

K = TypeVar('K')
V = TypeVar('V')


class Section:
    def __init__(self, *args: Union[V, 'SubSection'], indent: int = 4) -> None:
        """A section which automatically indents its contents

        The header is made bold automatically

        Args:
            *args: Initial items
            indent: Ident to use
        """
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
        """Append a subsection or item to the section

        Args:
            item: The item to append
        """
        self.items.append(item)

    def extend(self, items: Iterable) -> None:
        """Extend the section with a list of items

        Args:
            items: List of items to extend the document with
        """
        self.items.extend(items)


class SubSection(Section):
    def __init__(self, *args: Union[V, 'SubSubSection'], indent: int = 8) -> None:
        """A sub-section which automatically indents its contents

        The header is made bold automatically

        Args:
            *args: Initial items
            indent: Ident to use
        """
        super().__init__(*args, indent=indent)


class SubSubSection(SubSection):
    def __init__(self, *args: V, indent: int = 12) -> None:
        """A sub-sub-section which automatically indents its contents

        The header is made bold automatically

        Args:
            *args: Initial items
            indent: Ident to use
        """
        super().__init__(*args, indent=indent)
