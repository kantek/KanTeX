from typing import Union, Iterable, TypeVar

K = TypeVar('K')
V = TypeVar('V')


class KanTeXDocument:
    """Document containing sections."""

    def __init__(self, *args: Union[V, 'Section']) -> None:
        self.sections = [i for i in args if i]

    def __str__(self) -> str:
        return '\n\n'.join([str(section) for section in self.sections])

    def append(self, item: Union[V, 'FormattedBase', 'Section']) -> None:
        """Append an item to the document"""
        self.sections.append(item)

    def extend(self, items: Iterable) -> None:
        """Extend the document with a list of items"""
        self.sections.extend(items)


