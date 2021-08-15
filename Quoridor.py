# Author: Allison Land
# Date: 8/14/2021
# Description: Portfolio project - defines a QuoridorGame class which allows a Player class (also defined here) to
# play the board game Quoridor.

class QuoridorGame:
	"""
	Represents a two player version of the Quoridor board game. This class is responsible for initializing instances of
	the Player class for Player 1 and Player 2, storing and creating the board, tracking whose turn it is, and tracking
	the status of the game. The board contains current placement of fences as well as current player positions.
	The game itself is played using an instance of the QuoridorGame class. The QuoridorGame
	class interacts with the Player class because the player class contains data that is specific to each player:
	mainly the number of fences left to play, and the current position of the player on the board. This makes it more
	streamlined to implement certain methods.
	"""
	def __init__(self):
		"""Initializes QuoridorGame object."""
		self._player_one = Player(1)
		self._player_two = Player(2)
		self._board = {}  # stores board
		for x in range(9):
			for y in range(9):
				self._board[(x, y)] = []  # generates board coordinates
				if x == 0:
					self._board[(x, y)].append("v")  # places fence on leftmost side of board (prevents accidental fence placement)
				if y == 0:
					self._board[(x, y)].append("h")  # places fences on topmost side of board (prevents accidental fence placement)
				if x == 4 and y == 0:
					self._board[(x, y)].append("P1")  # initializes player one start space
				if x == 4 and y == 8:
					self._board[(x, y)].append("P2")  # initializes player two start space

		self._turn = self._player_one  # initializes first turn to player one
		self._status = "IN PROGRESS"  # "IN PROGRESS", "PLAYER ONE WINS", "PLAYER TWO WINS"

	def get_player_one(self):
		""":returns: player one object."""
		return self._player_one

	def get_player_two(self):
		""":returns: player two object."""
		return self._player_two

	def get_turn(self):
		""":returns: which player's turn it currently is."""
		return self._turn

	def get_status(self):
		""":returns: whether game is in progress or has been won."""
		return self._status

	def get_board(self):
		""":returns: the current status of the board, including player and fence locations."""
		return self._board

	def set_turn(self, player):  # takes player object
		""":param: which player's turn it is."""
		self._turn = player

	def set_status(self, status):  # STATUS ::string:: "IN PROGRESS", "PLAYER 1 WON", "PLAYER 2 WON"
		""":param: the current states of the game."""
		self._status = status

	def check_player(self, player):
		if player == 1:
			return self.get_player_one()
		elif player == 2:
			return self.get_player_two()
		else:
			return "not a valid player number"

	def is_on_board(self, coordinate):
		if coordinate in self.get_board():
			return True
		else:
			return False

	def is_adjacent(self, old_coord, new_coord):
		adjacent_spaces = [(old_coord[0] + 1, old_coord[1] + 1), (old_coord[0] + 1, old_coord[1] - 1),
						   (old_coord[0] + 1, old_coord[1]), (old_coord[0], old_coord[1] + 1),
						   (old_coord[0], old_coord[1] - 1), (old_coord[0] - 1, old_coord[1]),
						   (old_coord[0] - 1, old_coord[1] + 1), (old_coord[0] - 1, old_coord[1] - 1)]
		if new_coord in adjacent_spaces:
			return True
		else:
			return False

	def move_direction(self, old_coord, new_coord):
		if self.is_adjacent(old_coord, new_coord) is True:
			if new_coord[0] == old_coord[0] - 1 and new_coord[1] == old_coord[1]:
				return "left"
			elif new_coord[0] == old_coord[0] + 1 and new_coord[1] == old_coord[1]:
				return "right"
			elif new_coord[0] == old_coord[0] and new_coord[1] == old_coord[1] + 1:
				return "up"
			elif new_coord[0] == old_coord[0] and new_coord[1] == old_coord[1] - 1:
				return "down"
			elif new_coord[0] == old_coord[0] - 1 and new_coord[1] == old_coord[1] + 1:
				return "diagonal up left"
			elif new_coord[0] == old_coord[0] - 1 and  new_coord[1] == old_coord[1] - 1:
				return "diagonal down left"
			elif new_coord[0] == old_coord[0] + 1 and  new_coord[1] == old_coord[1] - 1:
				return "diagonal down right"
			elif new_coord[0] == old_coord[0] + 1 and new_coord[1] == old_coord[1] + 1:
				return "diagonal up right"
		else:
			return False

	# MOVES TO ACCOUNT FOR
	# Horizontal move: left: check for vertical fence current space
	# 	right: check for vertical fence right space
	# Vertical move: up: check for horizontal fence current space,
	# 	down: check for horizontal fence below space
	# Diagonal move:
	#	up left:
	#	up right:
	#	down left:
	#	down right:

	def is_pawn_jump(self, old_coord, new_coord):
		pass

	def check_fence_block(self, old_coord, new_coord):
		move_direction = self.move_direction(old_coord, new_coord)
		if (move_direction == "left" and "h" in self.get_board()[old_coord]) or \
			(move_direction == "right" and "h" in self.get_board()[(old_coord[0] + 1, old_coord[1])]) or \
			(move_direction == "up" and "v" in self.get_board()[old_coord]) or \
			(move_direction == "down" and "v" in self.get_board()[(old_coord[0], old_coord[1] - 1)]) or \
			(move_direction == "diagonal up left" and "v" in self.get_board()[(old_coord[0], old_coord[1] + 1)]) or \
			(move_direction == "diagonal up right" and "v" in self.get_board()[(old_coord[0] + 1, old_coord[1] + 1)]) or \
			(move_direction == "diagonal down right" and "v" in self.get_board()[(old_coord[0] - 1, old_coord[1] -1)]) or \
			(move_direction == "diagonal down left" and "v" in self.get_board()[(old_coord[0], old_coord[1] - 1)]):
			return True  # move blocked by fence
		else:
			return False  # move not blocked by fence


		# 	if "h" in self.get_board()[old_coord] or "h" in self.get_board()[(old_coord[0] + 1, old_coord[1])]:
		# 		return True
		# 	else:
		# 		return False
		# elif self.move_direction(old_coord, new_coord) == "vertical":
		# 	if "v" in self.get_board()[old_coord] or "v" in self.get_board()[(old_coord[0], old_coord[1] + 1)]:
		# 		return True
		# 	else:
		# 		return False
		# elif self.move_direction(old_coord, new_coord) == "diagonal":
		# 	if "h" or "v" in self.get_board()[(old_coord[0] + 1, old_coord[1] + 1)] or \
		# 		self.get_board()[(old_coord[0] + 1, old_coord[1] - 1)] or \
		# 		self.get_board()[(old_coord[0] - 1, old_coord[1] + 1)] or \
		# 		self.get_board()[(old_coord[0] - 1, old_coord[1] - 1)]:
		# 		return True
		# 	else:
		# 		return False


	def move_pawn(self, player, coordinate):
		""" Moves the player's pawn to a valid space.
		method takes following two parameters in order: an integer that represents which player (1 or 2) is making
		the move and a tuple with the coordinates of where the pawn is going to be moved to.
		:return:
		if the move is forbidden by the rule or blocked by the fence, return False
		if the move was successful or if the move makes the player win, return True
		if the game has been already won, return False"""
		player_object = self.check_player(player)
		validation = self.validate_pawn_move(player, coordinate)
		if validation is True:
			self.get_board()[player_object.get_player_position()].remove("P" + str(player))
			self.get_board()[coordinate].append("P" + str(player))
			player_object.set_position(coordinate)
			self.set_turn(player_object)
			if self.is_winner(player) == True:
				self.set_status("PLAYER " + player + " WINS")
		return validation


	def validate_pawn_move(self, player, coordinate):
		"""
		Checks to see if pawn move is valid.
		:param: an integer that represents which player (1 or 2) is making the move,
		a tuple of integers that represents the position on which the pawn is to be placed.
		:return:
		If valid, returns True.
		If invalid, returns False.
		"""
		player_object = self.check_player(player)
		if player_object == self.get_player_one():
			opponent_object = self.get_player_two()
		else:
			opponent_object = self.get_player_one()

		# self.is_pawn_jump()
		player_location = player_object.get_player_position()
		if self.get_status() == "IN PROGRESS":  # game is not won
			if self.get_turn() == player_object:  # is player's turn
				if self.is_on_board(coordinate) and self.is_adjacent(player_location, coordinate) is True: # is on board and adjacent
					if opponent_object.get_player_position() != coordinate:  # opponent not on space
						if self.check_fence_block(player_location, coordinate) == False: # not blocked by fence
							return True
		else:
			return False
		# add jump move

	def place_fence(self, player, fence_direction, coordinate):
		"""
		Places a fence on a valid coordinate. Fences are one space long.
		:param: an integer that represents which player (1 or 2) is making the move,
		a letter indicating whether it is vertical (v) or horizontal (h) fence,
		a tuple of integers that represents the position on which the fence is to be placed.
		:return:
		if player has no fence left, or if the fence is out of the boundaries of the board, or if there is already
		a fence there and the new fence will overlap or intersect with the existing fence, return False.
		If the fence can be placed, return True.
		If it breaks the fair-play rule (and if you are doing the extra credit part), return exactly the string breaks
		the fair play rule.
		If the game has been already won, return False
		"""
		player_1 = self.get_player_one()
		player_2 = self.get_player_two()
		validation = self.validate_fence_placement(player, fence_direction, coordinate)
		if validation is True:  # if move is valid
			self.get_board()[coordinate].append(fence_direction)  # adds fence to board
			if player == 1:     # decreases fences for player placing fence
				player_1.decrease_fences()
			elif player == 2:
				player_2.decrease_fences()
			return True
		else:  # if move invalid
			return validation

	def check_for_fence(self, fence_direction, coordinate):  # helper function for validate fence placement
		if fence_direction in self.get_board()[coordinate]:
			return True   # fence found
		else:
			return False  # no fence found

	def fair_play_rule(self, fence_direction, coordinate):
		pass
		# recursively check for path to winning side
		# If fair play, returns true
		# else, returns false
	# player
	# vertical or horizontal (tuple)  v(0,0)
	# game must still be in play
	# can't fully block player from reaching goal line
	# fair play rule

	def validate_fence_placement(self, player, fence_direction, coordinate):  # helper function for place fence
		"""
		Checks to see if a fence placement is valid.
		:param: an integer that represents which player (1 or 2) is making the move,
		a letter indicating whether it is vertical (v) or horizontal (h) fence,
		a tuple of integers that represents the position on which the fence is to be placed.
		:return:
		If valid, returns True.
		If invalid, returns False.
		"""
		player_1 = self.get_player_one()
		player_2 = self.get_player_one()
		if self.check_for_fence(fence_direction, coordinate) is False and self.get_status() == "IN PROGRESS":  # if no fence already there and game in progress
			if player == 1 and player_1.get_fences() > 0:  # if player one still has fences
				return self.fair_play_rule(fence_direction, coordinate)
			elif player == 2 and player_2.get_fences() > 0:
				return self.fair_play_rule(fence_direction, coordinate)
		else:
			return False

	def is_winner(self, player):
		"""To be used after making a move - checks to see whether player has won.
		:param:
		a single integer representing the player number as a parameter
		:return:
		returns True if that player has won and False if that player has not won."""
		p1_win = []
		p2_win = []
		for x in range(9):
			for y in range(9):
				if y == 8:
					p1_win.append((x, y))
				if y == 0:
					p2_win.append((x, y))
		if player == 1:
			if self.get_player_one().get_player_position() in p1_win:
				return True
		if player == 2:
			if self.get_player_two().get_player_position() in p2_win:
				return True
		else:
			return False
	# used in make_move: if player has won, updates game status after making move
	# player 1 wins by reaching y == 8
	# player 2 wins by reaching y == 0

	# def print_board(self):
	# 	"""Prints visual representation of current board."""
	# 	board = "+==+==+==+==+==+==+==+==+==+\n" \
	# 	        "|            P1            |\n" \
	# 	        "+  +  +  +  +  +  +  +  +  +\n" \
	# 	        "|                          |\n" \
	# 	        "+  +  +  +  +  +  +  +  +  +\n" \
	# 	        "|                          |\n" \
	# 	        "+  +  +  +  +  +  +  +  +  +\n" \
	# 	        "|                          |\n" \
	# 	        "+  +  +  +  +  +  +  +  +  +\n" \
	# 	        "|                          |\n" \
	# 	        "+  +  +  +  +  +  +  +  +  +\n" \
	# 	        "|                          |\n" \
	# 	        "+  +  +  +  +  +  +  +  +  +\n" \
	# 	        "|                          |\n" \
	# 	        "+  +  +  +  +  +  +  +  +  +\n" \
	# 	        "|                          |\n" \
	# 	        "+  +  +  +  +  +  +  +  +  +\n" \
	# 	        "|            P2            |\n" \
	# 	        "+==+==+==+==+==+==+==+==+==+\n"
	# 	# for coord in self.get_board():  # add in player positions and fences
	# 	print(board)


class Player:
	"""Represents a player in the Quoridor game. The player class contains data that is specific to each player:
	the player number, the number of fences left to play, and the current position of the player on the board. This
	makes it more streamlined to implement certain methods.

	Note: fences placed on board are not stored in player class because they are no longer unique to the player.

	The Player class interacts with the QuoridorGame instance which is the mechanism for playing the game. The
	Player class must interact with the QuoridorGame class because it stores all game specific information
	such as the board, current game status, etc, as well as the methods to actually play the game."""

	def __init__(self, player_number):
		"""Initializes player object"""
		self._player_number = player_number  # 1 or 2
		self._fences = 10  # both players start with 10 unplaced fences
		if self.get_player_number() == 1:
			self._position = (4, 0)
		elif self.get_player_number() == 2:
			self._position = (4, 8)

	def get_player_number(self):
		""":returns: player number."""
		return self._player_number

	def get_fences(self):
		""":returns: current number of fences player has off the board."""
		return self._fences

	def get_player_position(self):
		""":returns: current board position of the player."""
		return self._position

	def decrease_fences(self):
		"""Decreases the number of fences by 1.
		:return:
		if unable to decrease fences, returns False"""
		if self.get_fences() > 0:
			self._fences -= 1
		else:
			return False

	def set_position(self, position):
		"""Updates player's current position.
		:param: tuple representing coordinates as a parameter
		:return: None"""
		self._position = position


# DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS

# 1. Storing the board: The board will be stored in a dictionary in the init method of the QuoridorGame class. The
#  coordinates of the board will be saved as keys, while the fences and player positions will be stored as a list of
#  values for each coordinate. If a coordinate doesn't have any fences or players, the value will be an empty list.

# 2. Initializing the board: The board will be initialized in the init method of the QuoridorGame class as a dictionary.
#  In order to generate the coordinates as keys, I will use for loops to add each coordinate to the dictionary, as well
#  as any existing fences (I am treating fences as starting from the top left corner of each space, so the top and
#  left sides of the board will be initialized with fences, since the edges cannot have fences. You will not be able to
#  place fences on the bottom and right most sides of the board, since each coordinate can only have a fence placed on
#  the top and left sides.

# 3. Tracking current turn (which player): The turn will be stored in the init method of the QuoridorGame class. Upon
#  initialization it will begin with Player 1's turn. The turn will be represented by an instance of the Player object.

# 4. Validate pawn move:
#	Check that game has not already been won.
#   Check other player location: if other player adjacent, cannot move to other player's position
#			If other player adjacent and move is jumping opponent, check that fence is not behind player
#			If other player adjacent, fence behind player, and move is diagonally adjacent, check that fence
#			is not blocking move
#	Else check that move is adjacent, that fence is not blocking move (ie. Vertical fence present on (6,6) would block move
#	between (5,6) and (6,6)), and that other player is not on desired space. Returns true if move is valid, else returns
#	false.

# 5. Validate fence placement:
#	When board is initialized, fences will be placed on topmost side and leftmost side of board to ensure that no fences
#	can be accidentally placed there. Due to the design of the fence placements being on the top and left side of the
#	coordinates, the bottommost and rightmost sides of the board cannot have fences placed on them.
#	If fence not on same coordinate and same orientation (vertical vs. horizontal) and fence placement does not block
#	access of opponent to winning side of the board, returns True. Else returns False.

# 6. Tracking fences on/off board: Fences off the board are stored in the Player object. Each player starts with 10
#	fences. Each time a player places a fence their total number of fences decreases. When a fence is placed on the
#	board, it is then no longer associated with the player, and is simply stored in the board.

# 7. Tracking pawn's position on board: The pawn's position will be stored in two places: both on the board in the
#	QuoridorGame class, as well as an attribute of the Player class. This will enable better functionality in
#	implementing methods, and will require that the pawn's location is updated in both spots simultaneously when a move
#	is made.

pass

# MOVES TO ACCOUNT FOR
# Horizontal move: left: check for vertical fence current space
# 	right: check for veritcal fence right space
# Vertical move: up: check for horizontal fence current space,
# 	down: check for horizontal fence below space
# Diagonal move:
#	up left:
#	up right:
#	down left:
#	down right:

# INITIAL TESTS
q = QuoridorGame()
# q.print_board()
print(q.is_winner(1))
q.get_player_one().set_position((7, 8))
print(q.is_winner(1))
