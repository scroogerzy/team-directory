import json
import os

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "team.json")


def load_members():
    """Read team.json and return a list of member dictionaries."""
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Could not find {}.".format(DATA_FILE))
        return []
    except json.JSONDecodeError as error:
        print("{} is not valid JSON: {}".format(DATA_FILE, error))
        return []


def format_member(member):
    return "{} - {}".format(member["name"], member["role"])


def display_members(members):
    print("Team Directory")
    print("----------------")

    for member in members:
        print(format_member(member))

def display_member_count(members):
    print("\nTeam Summary")
    print("------------")
    print("Total members: {}".format(len(members)))


def search_member(members, keyword):
    keyword = keyword.lower()

    print("\nSearch Results:")
    for member in members:
        if keyword in member["name"].lower() or keyword in member["role"].lower():
            print(format_member(member))


def filter_by_role(members, role):
    role = role.lower()

    print("\nFiltered Results:")
    for member in members:
        if role in member["role"].lower():
            print(format_member(member))


members = load_members()

display_members(members)
display_member_count(members)
search_member(members, "Developer")
filter_by_role(members, "Developer")
