from player_reader import PlayerReader
from datetime import datetime

def sort_by_points(player):
    return player.points


class PlayerStats:
    def __init__(self, reader: PlayerReader):
        self._players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        
        sorted_players = sorted(
            self._players,
            reverse=True,
            key=sort_by_points
        )
        result = []

        for player in sorted_players:
            if player.nationality == nationality:
                result.append(player)
        return result
      