import random 
n = input("enter your name: ")
while True:
    b = list("123456789")
    print(f"Choose X or 0 {n}")
    p = input().upper()
    a = "0" if p == "X" else "X"

    while True:
        print(b[0], "|", b[1], "|", b[2])
        print("--+--+--")
        print(b[3], "|", b[4], "|", b[5])
        print("--+--+--")
        print(b[6], "|", b[7], "|", b[8])

        x=int(input(f"{n}, choose a number from 1 to 9:"))

        if b[x].isdigit():
            b[x] = p
        else:
            print("Invalid move. Try again.")
            continue
        w = [
            (0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)
        ]
        if any(b[i] == b[j] == b[k] for i, j, k in w):
            print(f"{n} congrats you fabulously won the game!!")
            break
        e =[i for i in range(9) if b[i].isdigit()]

        if not e:
            print("It's a tie!")
            break
        b[random.choice(e)] = a

        if any(b[i] == b[j] == b[k] for i, j, k in w):
            print(f"{n} you lost to a ai lol!!")
            break
    if input("Play again? (yes/no): ").lower() != "yes":
            print("Thanks for playing!")
            break