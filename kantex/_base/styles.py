from typing import Union, TypeVar

K = TypeVar('K')
V = TypeVar('V')


class FormattedBase:
    """Base class for any message type."""
    start: str
    end: str
    text: str

    def __init__(self, text: V) -> None:
        """A italic text

        Args:
            text: Text
        """
        self.text = f'{self.start}{text}{self.end}'

    def __add__(self, other: Union[V, 'FormattedBase']) -> str:
        return str(self) + str(other)

    def __repr__(self) -> str:
        return f'{type(self).__name__}({self.text})'

    def __str__(self) -> str:
        return self.text


class Bold(FormattedBase):
    pass


class Italic(FormattedBase):
    pass


class Strikethrough(FormattedBase):
    pass


class Code(FormattedBase):
    pass


class Pre(FormattedBase):
    pass


class Link(FormattedBase):
    template = None

    def __init__(self, label: V, url: str) -> None:
        """A Hyperlink with a label.

        Args:
            label: Label of the link
            url: URL of the link
        """

        self.text = self.template.format(label=label, url=url)
