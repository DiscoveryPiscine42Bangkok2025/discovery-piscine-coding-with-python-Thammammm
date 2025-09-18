import sys

def is_valid_board(board):
    n = len(board)
    if n == 0:
        return False
    for row in board:
        if len(row) != n:
            return False
    pieces = set("KQRBP.")
    king_count = sum(row.count("K") for row in board)
    if king_count != 1:
        return False
    for row in board:
        for c in row:
            if c not in pieces:
                return False
    return True

def attackers(board):
    n = len(board)
    attackers_list = []


    for r in range(n):
            for c in range(n):
                if board[r][c] == "K":
                    kr, kc = r, c
    
    pawn_attacks = [(1, -1), (1, 1)] 
    for dr, dc in pawn_attacks:
        r, c = kr + dr, kc + dc
        if 0 <= r < n and 0 <= c < n and board[r][c] == "P":
            attackers_list.append(("Pawn", r, c))

    rook_dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    for dr, dc in rook_dirs:
        r, c = kr, kc
        while True:
            r += dr
            c += dc
            if not (0 <= r < n and 0 <= c < n):
                break
            if board[r][c] != ".":
                if board[r][c] in {"R", "Q"}:
                    piece = "Rook" if board[r][c] == "R" else "Queen"
                    attackers_list.append((piece, r, c))
                break

    bishop_dirs = [(1,1), (1,-1), (-1,1), (-1,-1)]
    for dr, dc in bishop_dirs:
        r, c = kr, kc
        while True:
            r += dr
            c += dc
            if not (0 <= r < n and 0 <= c < n):
                break
            if board[r][c] != ".":
                if board[r][c] in {"B", "Q"}:
                    piece = "Bishop" if board[r][c] == "B" else "Queen"
                    attackers_list.append((piece, r, c))
                break

    return attackers_list

def checkmate_from_file(filename):
    try:
        with open(filename) as f:
            board = [line.strip() for line in f if line.strip()]
    except:
        print("Error")
        return

    if not is_valid_board(board):
        print("Error")
        return

    atks = attackers(board)
    if atks:
        details = ", ".join([f"{p} at ({r},{c})" for p, r, c in atks])
        print(f"Success ({details})")
    else:
        print("Fail")