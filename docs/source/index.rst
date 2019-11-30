PyPGN
========

A pure Python 3 library to simplify parsing and manipulation of PGN
(http://portablegamenotation.com/FIDE.html) format files, which are often used for sharing game rounds for chess.

It makes it very easy to work with PGN::

    from pypgn.game import Game
    # Importing game from file on disk
    chess_game = Game('test.pgn')

    # Import game from Lichess
    chess_game.pgn('dGm3ND39')

    print(chess_game.tag('Event'))
    print(chess_game.result())
    # Print opening ply for white
    print(chess_game.ply(1, 'w'))

Features
--------

- Import games from PGN file on disk or from Lichess
- Get tags, moves, plys or other key parts of a game

Installation
------------

Install `pypgn` by running::

    pip install pypgn

Contribute
----------

- Issue Tracker: https://github.com/DaniruKun/pypgn/issues
- Source Code: https://github.com/DaniruKun/pypgn

Support
-------

If you are having issues, please let us know.
Open an issue or message me on Telegram: https://t.me/danpetrov

License
-------

The project is licensed under the MPL-2 license.