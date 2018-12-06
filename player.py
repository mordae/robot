#!/usr/bin/python3 -tt
# -*- coding: utf-8 -*-

from robot import play, left, right

def ai(direction, tile):
    if tile != '#':
        return '^'

play(ai)

# vim:set sw=4 ts=4 et:
