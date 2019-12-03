"""
Finding problems at run-time

Steps
  1 - Run the code, and see all the errors we get at runtime
  2 - Fix them one by one

"""


from storage import players


def get_player(key, country):
    return players[country][key]


if __name__ == "__main__":
    # This is OK
    player = get_player(9, "UY")
    print(f" My first player is {player}")

    # Wrong order of parameters
    player = get_player("AR", 10)
    print(f" My second player is {player}")

    # player is a string, string + int is not defined
    player_and_number = player + 10
