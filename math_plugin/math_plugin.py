# -*- coding: utf-8 -*-
#
# Copyright (C) 2013 S. Daniel Francis <francis@sugarlabs.org>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301, USA.

import math
from TurtleArt.tapalette import make_palette
from TurtleArt.taprimitive import (ArgSlot, Primitive)
from TurtleArt.tatype import TYPE_FLOAT

from plugins.plugin import Plugin
from gettext import gettext as _


class Math_plugin(Plugin):
    def __init__(self, parent):
        self._parent = parent
        self._status = False

    def setup(self):
        palette = make_palette('math',
                               colors=["#FF00FF", "#A000A0"],
                               help_string=_('Advanced mathematic functions'))
        palette.add_block('sin',
                          style='number-style-1arg',
                          label='sin',
                          string_or_number=True,
                          prim_name='sin',
                          help_string=_('Sine'))
        self._parent.lc.def_prim(
            'sin', 1, Primitive(lambda self, x: math.sin(math.radians(x)),
                                return_type=TYPE_FLOAT,
                                arg_descs=[ArgSlot(TYPE_FLOAT)]))
        palette.add_block('cos',
                          style='number-style-1arg',
                          label='cos',
                          string_or_number=True,
                          prim_name='cos',
                          help_string=_('Cosine'))
        self._parent.lc.def_prim(
            'cos', 1, Primitive(lambda self, x: math.cos(math.radians(x)),
                                return_type=TYPE_FLOAT,
                                arg_descs=[ArgSlot(TYPE_FLOAT)]))
        palette.add_block('tan',
                          style='number-style-1arg',
                          label='tan',
                          string_or_number=True,
                          prim_name='tan',
                          help_string=_('Tangent'))
        self._parent.lc.def_prim(
            'tan', 1, Primitive(lambda self, x: math.tan(math.radians(x)),
                                return_type=TYPE_FLOAT,
                                arg_descs=[ArgSlot(TYPE_FLOAT)]))
        palette.add_block('asin',
                          style='number-style-1arg',
                          label='asin',
                          string_or_number=True,
                          prim_name='asin',
                          help_string=_('Arcsine'))
        self._parent.lc.def_prim(
            'asin', 1, Primitive(lambda self, x: math.degrees(math.asin(x)),
                                 return_type=TYPE_FLOAT,
                                 arg_descs=[ArgSlot(TYPE_FLOAT)]))
        palette.add_block('acos',
                          style='number-style-1arg',
                          label='acos',
                          string_or_number=True,
                          prim_name='acos',
                          help_string=_('Arccosine'))
        self._parent.lc.def_prim(
            'acos', 1, Primitive(lambda self, x: math.degrees(math.acos(x)),
                                 return_type=TYPE_FLOAT,
                                 arg_descs=[ArgSlot(TYPE_FLOAT)]))
        palette.add_block('atan',
                          style='number-style-1arg',
                          label='atan',
                          string_or_number=True,
                          prim_name='atan',
                          help_string=_('Arctangent'))
        self._parent.lc.def_prim(
            'atan', 1, Primitive(lambda self, x: math.degrees(math.atan(x)),
                                 return_type=TYPE_FLOAT,
                                 arg_descs=[ArgSlot(TYPE_FLOAT)]))

        palette.add_block('degrees',
                          style='number-style-1arg',
                          label='degrees',
                          string_or_number=True,
                          prim_name='degrees',
                          help_string=_('From radians to degrees'))
        self._parent.lc.def_prim(
            'degrees', 1, lambda self, x: math.degrees(x))
        palette.add_block('radians',
                          style='number-style-1arg',
                          label='radians',
                          string_or_number=True,
                          prim_name='radians',
                          help_string=_('From degrees to degrees'))
        self._parent.lc.def_prim(
            'radians', 1, lambda self, x: math.radians(x))

        palette.add_block('pi',
                          style='box-style',
                          label=_('π'),
                          special_name=_('pi'),
                          prim_name='pi',
                          help_string=_('Pi number'))
        self._parent.lc.def_prim(
            'pi', 0, Primitive(lambda arg: math.pi, return_type=TYPE_FLOAT,
                               arg_descs=[]))
        palette.add_block('e',
                          style='box-style',
                          label=_('e'),
                          prim_name='e',
                          help_string=_('e number'))
        self._parent.lc.def_prim(
            'e', 0, Primitive(lambda arg: math.e, return_type=TYPE_FLOAT,
                              arg_descs=[]))

        palette.add_block('exponentiation',
                          style='number-style-block',
                          label=[_('xⁿ'), _('base'), '         ' + _('exp')],
                          special_name=_('exponentiation'),
                          prim_name='exponentiation',
                          help_string=_(
                          'Exponentiation having base and exponent as inputs'))
        self._parent.lc.def_prim('exponentiation', 2,
                                 Primitive(self.exponentiation,
                                 return_type=TYPE_FLOAT,
                                 arg_descs=[ArgSlot(TYPE_FLOAT),
                                            ArgSlot(TYPE_FLOAT)]))

    @staticmethod
    def exponentiation(b, n):
        return float(b) ** n
