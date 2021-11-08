import unittest
from statistics import Statistics
from player import Player
from player_reader import PlayerReader

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_print_correct_player(self):
        player = PlayerReaderStub()
        io = player.get_players()

        self.assertEqual(str(io[0]), "Semenko EDM 4 + 12 = 16")

    def test_search_correct_player_name(self):
        player = PlayerReaderStub()
        io = player.get_players()

        self.assertEqual(str(io[0].name), "Semenko")

    def test_search_correct_players_of_the_team(self):
        player = PlayerReaderStub()
        io = player.get_players()

        test_list = []
        test_list.append(Player("Semenko", "EDM", 4, 12))
        test_list.append(Player("Kurri",   "EDM", 37, 53))
        test_list.append(Player("Gretzky", "EDM", 35, 89))

        self.assertListEqual(str([io]), test_list)
            




                
      

   