def load_team():
    with open("team.txt") as file:
        return [x.strip() for x in file.readlines()]

def show_team():
    for member in load_team():
        print(member)

show_team()