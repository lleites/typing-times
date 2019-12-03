"""
Using dataclasses

In this example request and response types are dataclasses.
Type hinting works really well and we have our code typed.

"""

from dataclasses import dataclass
from typing import Optional

from storage import players


@dataclass
class Request:
    key: int
    country: str


@dataclass
class Response:
    player_name: str


# Lets go full turbo with types
def get_player(request: Request) -> Optional[Response]:
    try:
        player_name = players[request.country][request.key]
        return Response(player_name)
    except KeyError:
        return None


if __name__ == "__main__":
    # Use case with dataclasses
    response = get_player(Request(9, "UY"))
    if response:
        name = response.player_name
    else:
        name = "UNKNOWN"
    print(f" My first player is {name}")
