[![PyPI version](https://badge.fury.io/py/pypgn.svg)](https://badge.fury.io/py/pypgn)
[![Python 3.5](https://img.shields.io/badge/python-3.5-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/DaniruKun/pypgn.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/DaniruKun/pypgn/context:python)
# PyPGN
A pure Python 3 library to simplify parsing and manipulation of [PGN](http://portablegamenotation.com/FIDE.html) (Portable Game Notation) format files, which are often used for serializing games such as chess.

## Prerequisites

Python version `3.x` > `3.4` and `Pip`

## Install

Install or upgrade with `PiP`

```shell script
$ pip install pypgn 
```

You can also install from source:

```shell script
git clone https://github.com/DaniruKun/pypgn.git
cd pypgn
python setup.py install
```

## Examples

```python
from pypgn.game import Game

chess_game = Game('test.pgn')

print(chess_game.get_tag_value('Event'))
print(chess_game.get_tag_value('Result'))
# Print opening ply for white
print(chess_game.get_ply(1, 'w'))
```

Output:
```shell script
>> Rated Blitz game
>> 0-1
>> e4
```