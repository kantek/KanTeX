from typing import TypeVar

from .. import _base
from .._base.items import FormattedBase as _FormattedBase

V = TypeVar('V')


class FormattedBase(_FormattedBase):
    pass


class Bold(FormattedBase):
    start = '**'
    end = '**'


class Italic(FormattedBase):
    start = '__'
    end = '__'


class Strikethrough(FormattedBase):
    start = '~~'
    end = '~~'


class Code(FormattedBase):
    start = '`'
    end = '`'


class Pre(FormattedBase):
    start = '```'
    end = '```'


class Link(_base.Link):
    template = '[{label}]({url})'
