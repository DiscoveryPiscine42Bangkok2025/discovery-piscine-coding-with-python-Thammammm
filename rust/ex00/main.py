import sys
import checkmate as c

def main():
    board1 = """\
R...
.K..
..P.
....\
"""
    c.checkmate(board1)

    board2 = """\
..
.K\
"""
    c.checkmate(board2)

if __name__ == "__main__":
    main() 