from player_stats import PlayerStats, PlayerReader

def main():
    reader = PlayerReader()
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)

if __name__ == "__main__":
    main()       
