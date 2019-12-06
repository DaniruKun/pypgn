import re
from typing import List, NewType, Union
from http.client import HTTPException, HTTPSConnection

Move = NewType('Move', Union[str, List])

PGN_REGEX = r'(?i)(\.pgn)$'
URL_REGEX = r'(\/\/)|(http)'


def _get_pgn_list(path: str) -> list:
    if re.search(PGN_REGEX, path):
        with open(file=path, mode='r') as f:
            lines = f.read().splitlines()
            return lines
    else:
        return _get_lichess_pgn_lines(path)


def _get_tags(pgn: list) -> dict:
    tag_list = [tag for tag in pgn if re.search(r'^\[', tag)]
    tag_dict: dict = {}
    for tag in tag_list:
        key = tag.split(" ", 1)[0][1:]
        val = tag.split(" ", 1)[1][1:-2]
        tag_dict[key] = val

    return tag_dict


def _get_moves(pgn: list) -> List[Move]:
    movetext = ''
    for line in pgn:
        if re.search(r'^1\. ', line):
            movetext: str = line

    movetext_items = movetext.split(" ")
    moves = []
    for i, item in enumerate(movetext_items):
        if re.search(r'\d\.', item):
            move = [movetext_items[i],
                    movetext_items[i + 1],
                    movetext_items[i + 2]]
            moves.append(move)

    return moves


def _get_lichess_pgn_lines(src: str) -> list:
    conn = HTTPSConnection("lichess.org")

    payload = ""
    endpoint = "/game/export/"
    params = "?evals=0&clocks=0&opening=0&literate=0"

    if re.search(URL_REGEX, src):
        tmp = re.split(r'org/', src)
        game_id = tmp[-1]
    else:
        game_id = src

    conn.request("GET", endpoint + game_id + params, payload)
    res = conn.getresponse()

    if res.status == 200:
        data = res.read()
        conn.close()
        return data.decode("utf-8").splitlines()
    else:
        conn.close()
        raise HTTPException(f'Unexpected status code! Expected: 200 Actual: {res.status}')
