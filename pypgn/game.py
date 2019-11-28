from typing import List
from pypgn.game_utils import (
    _get_tags, _get_pgn_list, _get_moves, Move)


class Game:
    """A class used to represent a chess game round.

    ...

    Attributes
    ----------
    pgn: list
        a list of lines of the original PGN file
    tags: Mapping
        a map of the parsed PGN file game tags
    moves: List[Move]
        a list of Moves, with [0] - move number,
                              [1] - white ply,
                              [2] - black ply

    """

    def __init__(self, path: str = None):
        """

        :param path: path to pgn file or Lichess game ID or
        :type path: str
        """
        self.pgn: list = _get_pgn_list(path)
        self.tags: dict = _get_tags(self.pgn)
        self.moves: List[Move] = _get_moves(self.pgn)

    def get_pgn_list(self) -> list:
        """Gets and returns a list of lines of the PGN

        :return: a list of lines of the parsed PGN
        :rtype: list
        """
        return self.pgn

    def get_tag(self, name: str) -> str:
        """Gets and returns a tag for a given key name

        :param name: Key name
        :type name: str
        :return: Value of a tag
        :rtype: str
        """
        return self.tags[name]

    def get_tags(self) -> dict:
        """Gets and returns a map of metadata tags of the PGN

        :return: Map of PGN tags
        :rtype: dict
        """
        return self.tags

    def get_move(self, index: int) -> Move:
        """Gets and returns a move of a certain number

        :param index: Move number
        :type index: int
        :return: Move
        :rtype: Move
        """
        return self.moves[index - 1]

    def get_moves(self) -> List[Move]:
        """Gets and returns a list of moves

        :return: A list of Moves
        :rtype: List[Move]
        """
        return self.moves

    def get_ply(self, index: int, player: str) -> str:
        """Gets and returns a ply for a given move

        :param index: Move number
        :type index: int
        :param player: Player color (white or black)
        :type player: str
        :return: Ply of player of given color
        :rtype: str
        """
        return self.moves[index - 1][1 if 'w' in player.lower() else 2]

    def get_move_count(self) -> int:
        """Gets and returns the total number of moves in the game

        :return: Total number of moves
        :rtype: int
        """
        return len(self.moves)

    def get_result(self) -> str:
        """Gets and returns the game result

        :return: Result of the game
        :rtype: str
        """
        return self.get_tag('Result')

    def get_date(self) -> str:
        """Gets and returns the date of the game

        :return: Date of the game in format YYYY.MM.DD
        """
        return self.get_tag('Date')

    def get_move_range(self, start: int, end: int) -> List[Move]:
        """Gets and returns a range of moves

        :param start: Start index of moves to get
        :param end: End index of moves to get
        :return: List of moves in given range
        """
        return self.moves[start - 1:end]
