"""
Adding type hints for return value

Steps
  1 - Now we have an error from Mypy because of the wrong return type (B)
  2 - Handle the result as a string
  3 - Run the code and see that we do not have problems thanks to Mypy

"""

from storage import players


def get_player(key: int, country: str) -> str:
    return players[country][key]


if __name__ == "__main__":
    # This is OK
    player = get_player(9, "UY")
    print(f" My first player is {player}")

    player = get_player(10, "AR")
    print(f" My second player is {player}")

    # B - player is a string, string + int is not defined
    player_and_number = player + 10
