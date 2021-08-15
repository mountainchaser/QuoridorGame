import unittest
from Quoridor import QuoridorGame, Player


class MyTestCase(unittest.TestCase):
	"""Quoridor.py test suite"""

	def setUp(self):
		"""Creates test objects"""
		self.q1 = QuoridorGame()
		self.q1.move_pawn(self.q1.get_player_one().get_player_number(), (4, 1))
		self.q1.move_pawn(self.q1.get_player_two().get_player_number(), (3, 8))
		self.q1.move_pawn(self.q1.get_player_two().get_player_number(), (2, 8))
		self.q1.place_fence(self.q1.get_player_one().get_player_number(), "h", (4,2))

	def test_object_can_be_created(self):
		self.assertIsInstance(self.q1, QuoridorGame)
		self.assertIsInstance(self.q1.get_player_one(), Player)
		self.assertIsInstance(self.q1.get_player_two(), Player)

	def test_moves(self):
		self.assertEqual(self.q1.get_player_one().get_player_position(), (4,1))
		self.assertEqual(self.q1.get_player_two().get_player_position(), (3, 8))
		self.assertFalse(self.q1.move_pawn(self.q1.get_player_two().get_player_number(), (2, 8)))
		self.assertIn("P2", self.q1.get_board()[(3, 8)])
		self.assertIn("P1", self.q1.get_board()[(4, 1)])

	def test_placing_fences(self):
		self.assertEqual(["h"], self.q1.get_board()[(4,2)])

# PLACING FENCES

# test QuoridorGame is instance
# test player is instance

# test pawn cannot be placed outside of board
# test pawn cannot be placed on same space as other opponent
# test pawn can be placed on board edges
# test pawn jump
# test horizontal moves
# test vertical moves (with and without blocking fences)
# test backwards moves
# test diagonal moves
# test can't make move when game is won
# test game is won when P1 is on y == 8
# test game is won when P2 is on y == 0

# test fence can't be placed outside of board
# test fence can't be placed on top of other fence
# test fence can't be placed when game is won
# test fence can only be placed if player has fences left
# test fence placement can't block other player from winning side of board (fair play rule)

if __name__ == '__main__':
	unittest.main()
