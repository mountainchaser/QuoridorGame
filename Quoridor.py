# Author: Allison Land
# Date: 8/8/2021
# Description: Portfolio project -

class QuoridorGame:
	"""
	Represents a two player version of the Quoridor game.

	"""
	def __init__(self):
		self._player_one = Player(1)
		self._player_two = Player(2)
		self._board = # list of lists?
		self._turn = self._player_one
		self._status = "IN_PROGRESS"

	def get_player_one(self):
		return self._player_one

	def get_player_two(self):
		return self._player_two

	def get_turn(self):
		return self._turn

	def get_status(self):
		return self._status

	def set_turn(self, player): # takes player object
		self._turn = player

	def set_status(self, status):  # STATUS ::string:: "IN_PROGRESS", "PLAYER ONE WON", "PLAYER TWO WON"
		self._status = status

	def move_pawn(self, player, coordinate):
		pass
		# one space at a time
		# check to see what is adjacent

	def validate_pawn_move(self):
		pass

	def place_fence(self, player, fence_direction, coordinate):
		#player
		# vertical or horizontal (tuple)  v(0,0)
		# game must still be in play
		# fair play rule
	def validate_fence_placement(self):
		pass
	def is_winner(self, player):
		"""Checks to see if player has won"""
		# updates game status after making move

	def print_board(self):
		pass


class Player:
	"""Represents a player in the Quoridor game."""
	def __init__(self, player_number):
		self._player_number = player_number
		self._fences = 10
		self._position = XX

	def get_player_number(self):
		return self._player_number

	def get_fences(self):
		return self._fences

	def get_player_position(self):
		return self._position

	def decrease_fences(self):  #what happens if no fences left?
		self._fences -= 1

	def set_position(self, position):
		self._position = position



# make sure fence and pawns can only be placed in appropriate spots (not each others spots)


# DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS
# 1. Storing the board:
# 2. Initializing the board:
# 3. Tracking current turn (which player):
# 4. Validate pawn move:
# 5. Validate fence placement:
# 6. Tracking fences on/off board:
# 7. Tracking pawn's position on board: