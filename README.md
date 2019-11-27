[![PyPI version](https://badge.fury.io/py/pypgn.svg)](https://badge.fury.io/py/pypgn)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/DaniruKun/pypgn.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/DaniruKun/pypgn/context:python)
[![Documentation Status](https://readthedocs.org/projects/pypgn/badge/?version=latest)](https://pypgn.readthedocs.io/en/latest/?badge=latest)
[![Build Status](https://travis-ci.org/DaniruKun/pypgn.svg?branch=master)](https://travis-ci.org/DaniruKun/pypgn)
# PyPGN
A pure Python 3 library to simplify parsing and manipulation of [PGN](http://portablegamenotation.com/FIDE.html) (Portable Game Notation) format files, which are often used for serializing games such as chess.

## Prerequisites

Python version `3.x` > `3.6` and `Pip`

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

print(chess_game.get_tag('Event'))
print(chess_game.get_result())
# Print opening ply for white
print(chess_game.get_ply(1, 'w'))
```

Output:
```shell script
$ Rated Blitz game
$ 0-1
$ e4
```

## Contributing

### Local setup
Setup a virtual environment with `virtualenv`
```shell script
$ virtualenv venv
$ source venv/bin/activate
```

Install requirements
```shell script
$ make install
```

Run unit tests locally with `pytest`
```shell script
$ make test
```

Run `flake8` lint with
```shell script
$ make lint
```

### Docker

You can also build and run tests in a Docker container:
```shell script
$ make docker-build
$ make docker-run
```
## Authors

[@DaniruKun](https://github.com/DaniruKun) aka Daniils Petrovs

## License
[Mozilla Public License 2.0](https://opensource.org/licenses/MPL-2.0) see [LICENSE](LICENSE) for more details.