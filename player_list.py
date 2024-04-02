from dataclasses import dataclass
import hashlib
import random


def hash_sid(sid):
    return hashlib.sha256(sid.encode()).hexdigest()


class PlayerList:
    def __init__(self):
        self.players: dict[str, Player] = {}
        self.player_counter = 1

    def add_player(self, sid):
        self.players[hash_sid(sid)] = Player(f"Player {self.player_counter}")
        self.player_counter += 1

    def remove_player(self, sid):
        del self.players[hash_sid(sid)]

    def as_dict(self):
        return {hash_sid(sid): profile.__dict__ for sid, profile in self.players.items()}


@dataclass
class Player:
    name: str
    color: str = None

    def __post_init__(self):
        self.color = (
            f"rgb("
            f"{random.randint(0, 255)},"
            f"{random.randint(0, 255)},"
            f"{random.randint(0, 255)}"
            f")"
        )