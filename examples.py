from pypgn.game import Game

chess_game = Game('pypgn/test.pgn')

print(chess_game.get_tag_value('Event'))
print(chess_game.get_tag_value('Result'))
# Print opening ply for white
print(chess_game.get_ply(1, 'w'))