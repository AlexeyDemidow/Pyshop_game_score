import random
import unittest
from gamescore import generate_game, get_score


class TestGetScore(unittest.TestCase):

    def test_wrong_game_offset(self):
        game = generate_game()
        game_offset = 999999
        self.assertEqual(get_score(game, game_offset), 'There is no data on this game.')

    def test_right_game_offset(self):
        game = generate_game()
        stamp = random.choice(game)
        game_offset = stamp['offset']
        game_score = (stamp['score']['home'], stamp['score']['away'])
        self.assertEqual(get_score(game, game_offset), game_score)

    def test_tuple_game_input_type(self):
        game = tuple(generate_game())
        stamp = random.choice(game)
        game_offset = stamp['offset']
        game_score = (stamp['score']['home'], stamp['score']['away'])
        self.assertEqual(get_score(game, game_offset), game_score)

    def test_str_gamescore_input_type(self):
        game = generate_game()
        game_offset = 'string'
        self.assertEqual(get_score(game, game_offset), 'The offset must be an integer.')

    def test_str_get_score_input_type(self):
        game = generate_game()
        stamp = random.choice(game)
        game_offset = stamp['offset']
        self.assertEqual(get_score('game', game_offset), 'Game stamps should be a list.')

    def test_str_input_type(self):
        game = 'game'
        game_offset = 'string'
        self.assertEqual(get_score(game, game_offset), 'Game stamps should be a list and offset must be a integer.')


if __name__ == '__main__':
    unittest.main()
