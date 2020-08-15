from typing import Union, TypeVar, Tuple, Type

from ._styles import Link, FormattedBase

K = TypeVar('K')
V = TypeVar('V')


class Mention(Link):
    """Inline Mention of a User."""

    def __init__(self, label: V, uid: int):
        super().__init__(label, f'tg://user?id={uid}')


class KeyValueItem(FormattedBase):
    """A item that has a key and a value divided by a colon."""

    def __init__(self, key: Union[K, FormattedBase], value: Union[V, FormattedBase],
                 colon_styles: Tuple[Type[FormattedBase]] = None) -> None:
        self.key = key
        self.value = value
        colon = ':'
        if colon_styles is not None:
            for style in colon_styles:
                colon = style(colon)

        self.text = f'{key}{colon} {value}'


class Item(FormattedBase):
    """A simple item without any formatting."""

    def __init__(self, text: V) -> None:
        self.text = str(text)



