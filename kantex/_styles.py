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
    def __init__(self, text: V) -> None:
        """A bold text

        Args:
            text: Text
        """
        self.text = f'**{text}**'


class Italic(FormattedBase):
    def __init__(self, text: V) -> None:
        """A italic text

        Args:
            text: Text
        """
        self.text = f'__{text}__'


class Strikethrough(FormattedBase):
    def __init__(self, text: V) -> None:
        """A strikethrough text

        Args:
            text: Text
        """
        self.text = f'~~{text}~~'


class Code(FormattedBase):
    def __init__(self, text: V) -> None:
        """Text formatted as code (monospace)

        Args:
            text: Text
        """
        self.text = f'`{text}`'


class Pre(FormattedBase):
    def __init__(self, text: V) -> None:
        """A Multiline Monospaced text.

        Args:
            text: Text
        """
        self.text = f'```{text}```'


class Link(FormattedBase):
    def __init__(self, label: V, url: str) -> None:
        """A Hyperlink with a label.

        Args:
            label: Label of the link
            url: URL of the link
        """
        self.text = f'[{label}]({url})'
