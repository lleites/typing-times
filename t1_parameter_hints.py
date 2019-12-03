"""
Adding type hints for parameters only

Steps
  1 - See how we have now an error because of the wrong parameter types (A)
  2 - Put parameters in the correct order
  3 - Run the code and see that we still have problems with the result type

"""

from storage import players


# we add now the types to the parameters, : (colon) and the type
def get_player(key: int, country: str):
    return players[country][key]


if __name__ == "__main__":
    # This is OK
    player = get_player(9, "UY")
    print(f" My first player is {player}")

    # A - Wrong order of parameters
    player = get_player("AR", 10)
    print(f" My second player is {player}")

    # B - player is a string, string + int is not defined
    player_and_number = player + 10
