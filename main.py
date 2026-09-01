def load_team():
    with open("team.txt") as file:
        return file.readlines()

def show_team():
    team = load_team()
    for member in team:
        print(member.strip())

show_team()