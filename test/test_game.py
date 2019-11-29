import pytest
import os
from pypgn.game import Game
from pathlib import Path
import time


@pytest.fixture(scope="module")
def game_pgn():
    pgn_file_path = Path('test/resources' if 'test' not in os.getcwd() else 'resources')

    return Game(str(pgn_file_path / 'test.pgn'))


class TestGame:
    def test_get_pgn_list(self, game_pgn):
        assert len(game_pgn.pgn_list()) == 20

    def test_get_tag(self, game_pgn):
        assert game_pgn.tag('Event') == "Rated Blitz game"
        assert game_pgn.tag('Site') == "https://lichess.org/#"
        assert game_pgn.tag('UTCDate') == "2019.11.06"

    def test_get_non_existing_tag(self, game_pgn):
        tag = 'SomeTag'
        with pytest.raises(KeyError, match=fr'{tag}'):
            game_pgn.tag(tag)

    def test_get_move(self, game_pgn):
        assert game_pgn.move(4) == ["4.", "d4", "Nc6"]

    def test_get_moves(self, game_pgn):
        moves = game_pgn.moves
        assert type(moves) == list
        assert moves[0] == ["1.", "e4", "c6"]

    def test_get_ply(self, game_pgn):
        for i in range(1, game_pgn.move_count()):
            move = game_pgn.move(i)
            assert move[1] == game_pgn.ply(i, 'w') and move[2] == game_pgn.ply(i, 'b'), \
                "Non-matching ply pair at move %s !" % str(i)

    def test_get_result(self, game_pgn):
        assert game_pgn.result() == game_pgn.tag('Result')

    def test_get_date(self, game_pgn):
        assert game_pgn.date() == game_pgn.tag('UTCDate')

    def test_get_move_range(self, game_pgn):
        assert game_pgn.move_range(1, 28) == game_pgn.moves

    def test_init_from_lichess_id(self):
        game_lichess = Game('dGm3ND39')
        time.sleep(1)
        assert game_lichess.move_count() == 18

    def test_init_from_lichess_url(self):
        game_lichess = Game('https://lichess.org/dGm3ND39')
        time.sleep(1)
        assert game_lichess.move_count() == 18
