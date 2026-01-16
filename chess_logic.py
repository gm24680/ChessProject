'''
Goals:
Two-player move entry + legal validation + display + move list
PGN import + replay
Stockfish evaluation per move
Weakness summary (rules first)
ML model for higher-level pattern detection
'''
import chess.svg
from IPython.display import SVG, display

board = chess.Board()
SVG(chess.svg.board(board=board,size=400))  

def chessGame():
    moveNumber = 1
    askForMove = f"{moveNumber}:"
    print("Start Game")
    
    while True:
        if board.is_checkmate() is True:
            break
        
        move = input(askForMove)
        board.push_san(move)
        move = input(askForMove)     
        board.push_san(move)
        moveNumber += 1


def main():
    
    board = chess.Board()
    SVG(chess.svg.board(board=board,size=400))
    
    chessGame()



main()






