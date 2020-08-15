from typing import Union, TypeVar, Tuple, Type

from .styles import Link, FormattedBase

K = TypeVar('K')
V = TypeVar('V')


class Mention(Link):
    def __init__(self, label: V, uid: int):
        """Inline Mention of a User.

        Args:
            label: The text of the mention
            uid: The id of the user to be mentioned
        """
        super().__init__(label, f'tg://user?id={uid}')


class KeyValueItem(FormattedBase):
    def __init__(self, key: Union[K, FormattedBase], value: Union[V, FormattedBase],
                 colon_styles: Tuple[Type[FormattedBase]] = None) -> None:
        """A item that has a key and a value divided by a colon.

        Args:
            key: The key
            value: The Value
            colon_styles: Tuple of style to be used for the colon
        """
        self.key = key
        self.value = value
        colon = ':'
        if colon_styles is not None:
            for style in colon_styles:
                colon = style(colon)

        self.text = f'{key}{colon} {value}'


class Item(FormattedBase):
    def __init__(self, text: V) -> None:
        """A simple item without any formatting.

        Args:
            text: The text
        """
        self.text = str(text)
