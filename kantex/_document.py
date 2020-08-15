from typing import Union, Iterable, TypeVar

K = TypeVar('K')
V = TypeVar('V')


class KanTeXDocument:
    def __init__(self, *args: Union[V, 'Section']) -> None:
        """Container class for Sections and Items

        Args:
            *args: Initial items of the document
        """
        self.sections = [i for i in args if i]

    def __str__(self) -> str:
        return '\n\n'.join([str(section) for section in self.sections])

    def append(self, item: Union[V, 'FormattedBase', 'Section']) -> None:
        """Append a section or item to the document

        Args:
            item: The item to append
        """
        self.sections.append(item)

    def extend(self, items: Iterable) -> None:
        """Extend the document with a list of items

        Args:
            items: List of items to extend the document with
        """
        self.sections.extend(items)
