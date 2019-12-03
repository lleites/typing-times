"""
Making function result Optional

Steps
  1 - Check how we have an error because of the wrong return type (A)
  2 - Change the return type to be Optional[str], do not forget the import
  3 - Now we have a problem because our print code does not handle Optional (B)
      Let's fix it!
  4 - Run the code and see that we do not have any issues :)

"""

from storage import players


# Lets give support for parameters of the right type but not available
# EAFP (easier to ask for forgiveness than permission)
def get_player(key: int, country: str) -> str:
    try:
        return players[country][key]
    except KeyError:
        return None  # A - It seems that the return type is wrong now


if __name__ == "__main__":
    # B - We should handle Optional here
    player_name = get_player(9, "UY")
    print(f"My first player is " + player_name)
