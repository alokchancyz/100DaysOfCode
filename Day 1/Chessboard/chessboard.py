def chessboard(s):
    pairing = {
        "a": 1, "b": 2, "c": 3, "d":4,
        "e": 5, "f": 6, "g":7, "h":8
        }
    
    col = pairing.get(s[0].lower())
    row = int(s[1])

    total = col + row

    if total % 2 == 0:
        return "Black"
    else:
        return "White"

    
if __name__ == "__main__":
    print(chessboard("b3"))
