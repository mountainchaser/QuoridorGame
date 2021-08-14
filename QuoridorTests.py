import unittest
import Quoridor


class MyTestCase(unittest.TestCase):
	def test_something(self):
		self.assertEqual(True, False)

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
