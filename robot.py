#!/usr/bin/python3 -tt
# -*- coding: utf-8 -*-

__all__ = ['play', 'left', 'right']

from console import bg, fg
from console.utils import cls

from time import sleep


# Tady se bude hrat:
arena = '''
##############################
# # #       #    # #      #! #
#     ##### # ## # # #### ## #
##### #       #  # #    # ## #
##    # # ##### ## #### #    #
## #### # #        #    ######
#  #    #   ###### # #########
# #####   ###      #         #
# #   ## #    ############## #
#^# #    # #                 #
##############################
'''.strip()

cols = len(arena.split('\n')[0]) + 1
rows = len(arena.split('\n'))
direction = '^'
won = False


def draw():
    # Pripravit barevnou verzi.
    colored = arena.replace('#', bg.lightblack + ' ' + bg.default)
    colored = colored.replace(direction, fg.lightyellow + direction + fg.default)
    colored = colored.replace('!', fg.lightred + '!' + fg.default)

    # Vymazat obrazovku.
    cls()

    # Zobrazit nadpis a herni plochu.
    print(' ' * 11, 'Robot!')
    print(colored)


def scout():
    pos = arena.index(direction)

    if direction == '^':
        return arena[pos - cols]
    elif direction == 'v':
        return arena[pos + cols]
    elif direction == '<':
        return arena[pos - 1]
    elif direction == '>':
        return arena[pos + 1]


def move():
    global arena, won

    pos = arena.index(direction)

    if direction == '^':
        newpos = pos - cols
    elif direction == 'v':
        newpos = pos + cols
    elif direction == '<':
        newpos = pos - 1
    elif direction == '>':
        newpos = pos + 1

    assert arena[newpos] != '#', 'cannot walk into a wall'

    if arena[newpos] == '!':
        cls()
        print('Congratulations, you have won!')
        won = True

    arena = arena[:pos] + ' ' + arena[pos + 1:]
    arena = arena[:newpos] + direction + arena[newpos + 1:]


def left(d):
    if d == '^':
        return '<'
    elif d == '<':
        return 'v'
    elif d == 'v':
        return '>'
    elif d == '>':
        return '^'


def right(d):
    if d == '^':
        return '>'
    elif d == '>':
        return 'v'
    elif d == 'v':
        return '<'
    elif d == '<':
        return '^'


def play(next_move, delay=0.3):
    global direction, arena, won

    won = False

    # Porad dokola, dokud nevyhrajeme...
    while not won:
        # Vykreslit situaci.
        draw()

        # Chvili pockat.
        sleep(delay)

        # Zeptat se hrace na dalsi tah.
        action = next_move(direction, scout())

        assert action in ('<', '>', '^', None), 'invalid action'

        if action == '<':
            pos = arena.index(direction)
            direction = left(direction)
            arena = arena[:pos] + direction + arena[pos + 1:]
        elif action == '>':
            pos = arena.index(direction)
            direction = right(direction)
            arena = arena[:pos] + direction + arena[pos + 1:]
        elif action == '^':
            move()


# vim:set sw=4 ts=4 et:
