from typing import TypeVar

from .. import _base
from .._base.items import FormattedBase as _FormattedBase

V = TypeVar('V')


class FormattedBase(_FormattedBase):
    pass


class Bold(FormattedBase):
    start = '<b>'
    end = '</b>'


class Italic(FormattedBase):
    start = '<i>'
    end = '</i>'


class Strikethrough(FormattedBase):
    start = '<s>'
    end = '</s>'


class Code(FormattedBase):
    start = '<code>'
    end = '</code>'


class Pre(FormattedBase):
    start = '<pre>'
    end = '</pre>'


class Link(_base.Link):
    template = '<a href="{url}">{label}</a>'
