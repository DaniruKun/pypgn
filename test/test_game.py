import pytest
import os


@pytest.fixture(scope="module")
def game_obj():
    from pypgn.game import Game
    from pathlib import Path
    pgn_file_path = Path('test/resources') if 'test' not in os.getcwd() else Path('resources')

    return Game(str(pgn_file_path / 'test.pgn'))


class TestGame:
    def test_get_pgn_list(self, game_obj):
        assert len(game_obj.get_pgn_list()) == 20

    def test_get_tags(self, game_obj):
        assert type(game_obj.get_tags()) == dict

    def test_get_tag_value(self, game_obj):
        assert game_obj.get_tag('Event') == "Rated Blitz game"
        assert game_obj.get_tag('Site') == "https://lichess.org/#"
        assert game_obj.get_tag('UTCDate') == "2019.11.06"

    def test_get_move(self, game_obj):
        assert game_obj.get_move(4) == ["4.", "d4", "Nc6"]

    def test_get_moves(self, game_obj):
        moves = game_obj.get_moves()
        assert type(moves) == list
        assert moves[0] == ["1.", "e4", "c6"]

    def test_get_ply(self, game_obj):
        for i in range(1, game_obj.get_move_count()):
            move = game_obj.get_move(i)
            assert move[1] == game_obj.get_ply(i, 'w') \
                   and move[2] == game_obj.get_ply(i, 'b'), \
                f"Non-matching ply pair at move {i} !"

    def test_get_move_count(self, game_obj):
        assert game_obj.get_move_count() == len(game_obj.get_moves())

    def test_get_result(self, game_obj):
        assert game_obj.get_result() == game_obj.get_tag('Result')

    def test_get_date(self, game_obj):
        assert game_obj.get_date() == game_obj.get_tag('UTCDate')

    def test_get_move_range(self, game_obj):
        assert game_obj.get_move_range(1, 28) == game_obj.get_moves()
