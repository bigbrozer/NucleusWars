#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# NucleusWars
# Copyright (C) 2014 Vincent BESANCON <besancon.vincent@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
# OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""This module focus on the screen creation."""

import sdl2
import sdl2.ext


class Screen(object):
    """Initialize the game screen."""
    def __init__(self, title, width, height, fill=None):
        self.title = title
        self.width = width
        self.height = height
        self.fill = fill or sdl2.ext.Color(0, 0, 0)
        self.screen = sdl2.ext.Window(self.title, size=(self.width,
                                                        self.height))
        sdl2.ext.fill(self.screen.get_surface(), self.fill)

    def show(self):
        """Show the game screen (window)."""
        self.screen.show()

    def refresh(self):
        """Refresh the screen."""
        self.screen.refresh()
