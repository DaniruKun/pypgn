import re

from typing import Mapping, List


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


def _get_moves(pgn: list) -> List[List]:
    for line in pgn:
        if re.search(r'^1\. ', line):
            movetext: str = line

    movetext_items = movetext.split(" ")
    moves = []
    for i, item in enumerate(movetext_items):
        if re.search(r'\d\.', item):
            moves.append([movetext_items[i],
                                 movetext_items[i + 1],
                                 movetext_items[i + 2]])

    return moves


class Game:
    def __init__(self, file_path):
        self.pgn: list = _get_pgn_list(file_path)
        self.tags: Mapping = _get_tags(self.pgn)
        self.moves: List[List] = _get_moves(self.pgn)

    def get_tag_value(self, name: str) -> str:
        return self.tags[name]

    def get_move(self, index: int, player: str = None):
        pass

    def get_move_count(self) -> int:
        return len(self.moves)


game = Game('test.pgn')
