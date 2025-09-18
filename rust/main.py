import checkmate as c
import sys



def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <board1> [board2 ...]")
        return

    for filename in sys.argv[1:]:
        c.checkmate_from_file(filename)

if __name__ == "__main__":
    main()
