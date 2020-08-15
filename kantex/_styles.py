from typing import Union, TypeVar

K = TypeVar('K')
V = TypeVar('V')


class FormattedBase:
    """Base class for any message type."""
    text: str

    def __add__(self, other: Union[V, 'FormattedBase']) -> str:
        return str(self) + str(other)

    def __repr__(self) -> str:
        return f'{type(self).__name__}({self.text})'

    def __str__(self) -> str:
        return self.text


class Bold(FormattedBase):
    """A bold text."""

    def __init__(self, text: V) -> None:
        self.text = f'**{text}**'


class Italic(FormattedBase):
    """A italic text."""

    def __init__(self, text: V) -> None:
        self.text = f'__{text}__'


class Strikethrough(FormattedBase):
    def __init__(self, text: V) -> None:
        self.text = f'~~{text}~~'


class Code(FormattedBase):
    """A Monospaced text."""

    def __init__(self, text: V) -> None:
        self.text = f'`{text}`'


class Pre(FormattedBase):
    """A Multiline Monospaced text."""

    def __init__(self, text: V) -> None:
        self.text = f'```{text}```'


class Link(FormattedBase):
    """A Hyperlink with a label."""

    def __init__(self, label: V, url: str) -> None:
        self.text = f'[{label}]({url})'


