from typing import Union, TypeVar, Tuple, Type

from ._styles import Link
from .. import _base

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


class KeyValueItem(_base.KeyValueItem):
    pass


class Item(_base.Item):
    pass
