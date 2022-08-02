import random

opts = ['Rock', 'Scissors', 'Paper']
games = int(input("how many wins to define the winner?\n "))


def rsp(i, j):
    lst = []

    if i == "Rock" and j == "Paper":
        lst.append("j")
    elif i == "Rock" and j == "Scissors":
        lst.append("i")
    elif i == "Paper" and j == "Rock":
        lst.append("i")
    elif i == "Paper" and j == "Scissors":
        lst.append("j")
    elif i == "Scissors" and j == "Paper":
        lst.append("i")
    elif i == "Scissors" and j == "Rock":
        lst.append("j")
    else:
        return "0"

    return lst


s, p, q, k = 0, 0, 0, True
while k:
    res = []
    pc = random.choice(opts)
    # print(pc)
    player_val = input("choose between <Rock> , <Paper> and <Scissors> ?\n ")
    res = rsp(pc, player_val)
    if res[s] == 'i':
        p += 1
        print(f"pc = {p}  -  player = {q}")
    elif res[s] == 'j':
        q += 1
        print(f"pc = {p}  -  player = {q}")
    else:
        print(f"\033[31;1meven \033[0m \npc = {p}  -  player = {q}")

    if p == games:
        print("\033[34;7m Pc is winner \033[0m")
        k = False
    elif q == games:
        print("\033[34;7m Player is winner \033[0m")
        k = False
    else:
        continue
