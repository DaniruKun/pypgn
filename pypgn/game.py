def _get_pgn_string(path: str) -> str:
    with open(file=path, mode='r') as f:
        pgn: str = f.read()
        return pgn


class Game:
    def __init__(self, file_path):
        self.pgn = _get_pgn_string(file_path)

    def get_tag(self, name: str):
        pass

    def get_tags(self):
        pass

    def get_movetext(self):
        pass

    def get_move(self):
        pass

    def get_move_count(self):
        pass