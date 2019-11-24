import re

from typing import Mapping


def _get_pgn_list(path: str) -> list:
    with open(file=path, mode='r') as f:
        lines = f.read().splitlines()
        return lines


def _get_tags(pgn: list) -> Mapping:
    tag_list = [tag for tag in pgn if re.search(r'^\[', tag)]
    tag_dict: dict = {}
    for tag in tag_list:
        key = tag.split(" ", 1)[0][1:]
        val = tag.split(" ", 1)[1][1:-2]
        tag_dict[key] = val

    return tag_dict


class Game:
    def __init__(self, file_path):
        self.pgn: list = _get_pgn_list(file_path)
        self.tags: Mapping = _get_tags(self.pgn)

    def get_tag(self, name: str):
        pass

    def get_movetext(self):
        pass

    def get_move(self):
        pass

    def get_move_count(self):
        pass


game = Game('test.pgn')
game.get_tags()
