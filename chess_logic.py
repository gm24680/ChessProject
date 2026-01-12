import chess
import chess.svg

from IPython.display import SVG, display

board = chess.Board()
SVG(chess.svg.board(board=board,size=400))  

board.push_san("e4")
