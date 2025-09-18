def checkmate(board_str):
    board = [list(row) for row in board_str.splitlines()]
    n = len(board)

    king_pos = None
    for r in range(n):
        for c in range(n):
            if board[r][c] == "K":
                king_pos = (r, c)
                break
        if king_pos:
            break

    if not king_pos:
        print("Fail") 
        return

    kr, kc = king_pos

    pawn_attacks = [(1, -1), (1, 1)] 
    for dr, dc in pawn_attacks:
        r, c = kr + dr, kc + dc
        if 0 <= r < n and 0 <= c < n and board[r][c] == "P":
            print("Success")
            return

    rook_dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    bishop_dirs = [(1,1), (1,-1), (-1,1), (-1,-1)]

    def scan_dirs(dirs, pieces):
        for dr, dc in dirs:
            r, c = kr, kc
            while True:
                r += dr
                c += dc
                if not (0 <= r < n and 0 <= c < n):
                    break
                if board[r][c] != ".":
                    if board[r][c] in pieces:
                        return True
                    else:
                        break
        return False

    if scan_dirs(rook_dirs, {"R", "Q"}):
        print("Success")
        return

    if scan_dirs(bishop_dirs, {"B", "Q"}):
        print("Success")
        return

    print("Fail")


