def load_members():
    with open("team.txt", "r") as file:
        return file.readlines()


def display_members():
    members = load_members()

    print("Team Directory")
    print("----------------")

    for member in members:
        print(member.strip())


display_members()