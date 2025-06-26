def rps(p1, p2):
    if p1 == "rock":
        if p2 == "rock":
            return "Draw!"
        elif p2 == "paper":
            return "Player 2 won!"
        elif p2 == "scissors":
            return "Player 1 won!"
    elif p1 == "paper":
        if p2 == "rock":
            return "Player 1 won!"
        elif p2 == "paper":
            return "Draw!"
        elif p2 == "scissors":
            return "Player 2 won!"
    elif p1 == "scissors":
        if p2 == "rock":
            return "Player 2 won!"
        elif p2 == "paper":
            return "Player 1 won!"
        elif p2 == "scissors":
            return "Draw!"
    else:
        return "Invalid input!"
def abbrev_name(name):
    
    return name[0].upper() + '.' + name[name.index(' ') + 1].upper()