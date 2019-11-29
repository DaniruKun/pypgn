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
        assert len(game_pgn.get_pgn_list()) == 20

    def test_get_tag(self, game_pgn):
        assert game_pgn.get_tag('Event') == "Rated Blitz game"
        assert game_pgn.get_tag('Site') == "https://lichess.org/#"
        assert game_pgn.get_tag('UTCDate') == "2019.11.06"

    def test_get_non_existing_tag(self, game_pgn):
        with pytest.raises(KeyError):
            game_pgn.get_tag('SomeTag')

    def test_get_move(self, game_pgn):
        assert game_pgn.get_move(4) == ["4.", "d4", "Nc6"]

    def test_get_moves(self, game_pgn):
        moves = game_pgn.get_moves()
        assert type(moves) == list
        assert moves[0] == ["1.", "e4", "c6"]

    def test_get_ply(self, game_pgn):
        for i in range(1, game_pgn.get_move_count()):
            move = game_pgn.get_move(i)
            assert move[1] == game_pgn.get_ply(i, 'w') and move[2] == game_pgn.get_ply(i, 'b'), \
                "Non-matching ply pair at move %s !" % str(i)

    def test_get_move_count(self, game_pgn):
        assert game_pgn.get_move_count() == len(game_pgn.get_moves())

    def test_get_result(self, game_pgn):
        assert game_pgn.get_result() == game_pgn.get_tag('Result')

    def test_get_date(self, game_pgn):
        assert game_pgn.get_date() == game_pgn.get_tag('UTCDate')

    def test_get_move_range(self, game_pgn):
        assert game_pgn.get_move_range(1, 28) == game_pgn.get_moves()

    def test_init_from_lichess_id(self):
        game_lichess = Game('dGm3ND39')
        time.sleep(1)
        assert game_lichess.get_move_count() == 18

    def test_init_from_lichess_url(self):
        game_lichess = Game('https://lichess.org/dGm3ND39')
        time.sleep(1)
        assert game_lichess.get_move_count() == 18
