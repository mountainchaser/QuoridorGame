
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
                    self._board[(x, y)].append(
                        "v")  # places fence on leftmost side of board (prevents accidental fence placement)
                if y == 0:
                    self._board[(x, y)].append(
                        "h")  # places fences on topmost side of board (prevents accidental fence placement)
                if x == 4 and y == 0:
                    self._board[(x, y)].append("P1")  # initializes player one start space
                if x == 4 and y == 8:
                    self._board[(x, y)].append("P2")  # initializes player two start space

        self._turn = 1  # initializes first turn to player one
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

    def set_turn(self, player):  # takes integer
        """:param: integer representing which player's turn it is."""
        self._turn = player

    def set_status(self, status):  # STATUS ::string:: "IN PROGRESS", "PLAYER 1 WON", "PLAYER 2 WON"
        """:param: the current status of the game."""
        self._status = status

    def check_player(self, player):
        """Looks up player object by number.
        :param: player number (int)
        :returns: player_object, or "not a valid player number"""
        if player == 1:
            return self.get_player_one()
        elif player == 2:
            return self.get_player_two()
        else:
            return "not a valid player number"

    def get_opponent(self, player):
        """:returns: opponent object"""
        player_object = self.check_player(player)
        if player_object == self.get_player_one():
            opponent_object = self.get_player_two()
        else:
            opponent_object = self.get_player_one()
        return opponent_object

    def is_on_board(self, coordinate):
        """Checks to see if coordinate is on the board.
        :param: coordinate tuple
        :returns: True if on board
        False if not on board."""
        if coordinate in self.get_board():
            return True
        else:
            return False

    def is_adjacent(self, old_coord, new_coord):
        """Checks to see if coordinates are adjacent.
        :param: coordinate tuple with current location,
        new coordinate tuple
        :returns: True if adjacent, else returns False"""
        adjacent_spaces = [(old_coord[0] + 1, old_coord[1] + 1), (old_coord[0] + 1, old_coord[1] - 1),
                           (old_coord[0] + 1, old_coord[1]), (old_coord[0], old_coord[1] + 1),
                           (old_coord[0], old_coord[1] - 1), (old_coord[0] - 1, old_coord[1]),
                           (old_coord[0] - 1, old_coord[1] + 1), (old_coord[0] - 1, old_coord[1] - 1)]
        if new_coord in adjacent_spaces:
            return True
        else:
            return False

    def is_adjacent_plus_1(self, old_coord, new_coord):
        """Checks to see if coordinates are two spaces away from each other.
        :param: coordinate tuple with current location,
        new coordinate tuple
        :returns: True if adjacent+1, else returns False"""
        adjacent_plus_1_spaces = [(old_coord[0] + 2, old_coord[1]), (old_coord[0], old_coord[1] + 2),
                                  (old_coord[0], old_coord[1] - 2), (old_coord[0] - 2, old_coord[1])]
        if new_coord in adjacent_plus_1_spaces:
            return True
        else:
            return False

    def move_direction(self, old_coord, new_coord):
        """Returns the direction of a move from one coordinate to another."""
        if self.is_adjacent(old_coord, new_coord) is True:
            if new_coord[0] == old_coord[0] - 1 and new_coord[1] == old_coord[1]:
                return "left"
            elif new_coord[0] == old_coord[0] + 1 and new_coord[1] == old_coord[1]:
                return "right"
            elif new_coord[0] == old_coord[0] and new_coord[1] == old_coord[1] - 1:
                return "up"
            elif new_coord[0] == old_coord[0] and new_coord[1] == old_coord[1] + 1:
                return "down"
            elif new_coord[0] == old_coord[0] - 1 and new_coord[1] == old_coord[1] + 1:
                return "diagonal up left"
            elif new_coord[0] == old_coord[0] - 1 and new_coord[1] == old_coord[1] - 1:
                return "diagonal down left"
            elif new_coord[0] == old_coord[0] + 1 and new_coord[1] == old_coord[1] - 1:
                return "diagonal down right"
            elif new_coord[0] == old_coord[0] + 1 and new_coord[1] == old_coord[1] + 1:
                return "diagonal up right"
        else:
            return False

    def pawn_jump_coordinates_for_check_fence(self, old_coord, new_coord):
        """Generates proper coordinates to check for fence blocks for pawn jump scenarios."""
        move_direction = self.move_direction(old_coord, new_coord)
        if move_direction == "left":
            x = old_coord[0] - 2
            y = old_coord[1]
            return (x, y)
        elif move_direction == "right":
            x = old_coord[0] + 2
            y = old_coord[1]
            return (x, y)
        elif move_direction == "up":
            x = old_coord[0]
            y = old_coord[1] + 2
            return (x, y)
        elif move_direction == "down":
            x = old_coord[0]
            y = old_coord[1] - 2
            return (x, y)

    def is_pawn_jump(self, player, old_coord, new_coord):
        """Determines if a move is a pawn jump.
        :returns: True if a pawn jump, else returns False."""
        opponent_object = self.get_opponent(player)
        opponent_location = opponent_object.get_player_position()
        opponent_direction = self.move_direction(old_coord, opponent_location)
        move_direction = self.move_direction(old_coord, new_coord)
        if opponent_direction == move_direction and \
                self.is_adjacent(old_coord, opponent_location) and \
                self.is_adjacent_plus_1(old_coord, new_coord):
            # if opponent and move are in same direction and move is 2 spaces, and opponents are adjacent
            if self.check_fence_block(old_coord, self.pawn_jump_coordinates_for_check_fence(old_coord, new_coord)) \
                    is False:
                return True  # is a valid pawn jump
        else:
            return False

    def check_fence_block(self, old_coord, new_coord):
        """Checks to see if a fence is blocking a move.
        :param: current location tuple coordinate, new location tuple coordinate
        :returns: True if fence is blocking, else returns False."""
        move_direction = self.move_direction(old_coord, new_coord)
        if (move_direction == "left" and "v" in self.get_board()[old_coord]) or \
                (move_direction == "right" and "v" in self.get_board()[(old_coord[0] + 1, old_coord[1])]) or \
                (move_direction == "up" and "h" in self.get_board()[old_coord]) or \
                (move_direction == "down" and "h" in self.get_board()[(old_coord[0], old_coord[1] + 1)]) or \
                (move_direction == "diagonal up left" and "v" in self.get_board()[(old_coord[0], old_coord[1] + 1)]) or\
                (move_direction == "diagonal up right" and "v" in self.get_board()[
                    (old_coord[0] + 1, old_coord[1] + 1)]) or \
                (move_direction == "diagonal down right" and "v" in self.get_board()[
                    (old_coord[0] - 1, old_coord[1] - 1)]) or \
                (move_direction == "diagonal down left" and "v" in self.get_board()[(old_coord[0], old_coord[1] - 1)]):
            return True  # move blocked by fence
        else:
            return False  # move not blocked by fence

    def move_pawn(self, player, coordinate):
        """ Moves the player's pawn to a valid space.
        method takes following two parameters in order: an integer that represents which player (1 or 2) is making
        the move and a tuple with the coordinates of where the pawn is going to be moved to.
        :return:
        if the move is forbidden by the rule or blocked by the fence, return False
        if the move was successful or if the move makes the player win, return True
        if the game has been already won, return False"""
        player_object = self.check_player(player)
        opponent_object = self.get_opponent(player)
        validation = self.validate_pawn_move(player, player_object.get_player_position(), coordinate)
        if validation is True:
            self.get_board()[player_object.get_player_position()].remove("P" + str(player))
            self.get_board()[coordinate].append("P" + str(player))
            player_object.set_position(coordinate)
            self.set_turn(opponent_object.get_player_number())
            if self.is_winner(player):
                self.set_status("PLAYER " + str(player) + " WINS")
        return validation

    def validate_pawn_move(self, player, player_location, coordinate):
        """
        Checks to see if pawn move is valid.
        :param: an integer that represents which player (1 or 2) is making the move,
        a tuple of integers that represents the position on which the pawn is to be placed.
        :return:
        If valid, returns True.
        If invalid, returns False.
        """
        opponent_location = self.get_opponent(player).get_player_position()
        directions = ["up", "down", "left", "right"]
        if self.get_status() == "IN PROGRESS" and \
                self.get_turn() == player and \
                self.is_on_board(coordinate) and \
                opponent_location != coordinate:
            # if game is not won, is player's turn, coordinate on board, and opponent not on space
            if self.is_adjacent(player_location, opponent_location):  # if players are adjacent
                if self.is_pawn_jump(player, player_location, coordinate) is True and \
                        self.check_fence_block(player_location,
                            self.pawn_jump_coordinates_for_check_fence(player_location, coordinate)) \
                        is False:  # if a pawn jump and not blocked by fence
                    return True  # valid move
                elif self.move_direction(player_location, coordinate) != self.move_direction(player_location, opponent_location):
                    if self.check_fence_block(player_location, coordinate) is False:
                        return True
                        # if players are adjacent, no fence block, move is not location of other pawn, valid move
                else:
                    return False  # invalid move
            elif self.is_adjacent(player_location, coordinate) is True and \
                    self.check_fence_block(player_location, coordinate) is False and \
                    self.move_direction(player_location, coordinate) in directions:
                # is adjacent not blocked by fence, not diagonal
                return True  # valid move
            else:
                return False  # invalid move
        else:
            return False  # invalid move

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
        player_object = self.check_player(player)
        validation = self.validate_fence_placement(player, fence_direction, coordinate)

        if validation is True:  # if placement is valid # and self.fair_play_rule(player, fence_direction, coordinate)
            self.get_board()[coordinate].append(fence_direction)  # adds fence to board to check fair play rule
            opponent_number = self.get_opponent(player).get_player_number()
            fair_play = self.fair_play_rule(opponent_number)  # remove to deactivate fair_play
            if fair_play == "breaks the fair play rule":  # remove to deactivate fair_play
                self.get_board()[coordinate].remove(fence_direction)
                return "breaks the fair play rule"
            else:
                player_object.decrease_fences()
                self.set_turn(opponent_number)
                return True
        else:
            return False

    def check_for_fence(self, fence_direction, coordinate):  # helper function for validate fence placement
        if fence_direction in self.get_board()[coordinate]:
            return True  # fence found
        else:
            return False  # no fence found

    def fair_play_rule(self, opponent, opponent_location=None, used=None):
        """Checks to see if fence placement breaks the game's fair play rule, meaning that
        the fence placement blocks the other player from the possibility of winning and reaching
        the other side.
        :param: integer representing the opponent of the player placing the fence,
        :returns: True if move doesn't block other player from possibility of winning
        breaks fair play rule if move blocks player from winning side of board"""
        if used is None:  # first iteration
            used = {}
            self.set_turn(opponent)
            opponent_location = self.check_player(opponent).get_player_position()

        left_move = (opponent_location[0] - 1, opponent_location[1])
        right_move = (opponent_location[0] + 1, opponent_location[1])
        up_move = (opponent_location[0], opponent_location[1] - 1)
        down_move = (opponent_location[0], opponent_location[1] + 1)

        if opponent == self.get_player_one().get_player_number() and opponent_location[1] == 8:
            return True  # if player one can get to the other side

        if opponent == self.get_player_two().get_player_number() and opponent_location[1] == 0:
            return True  # if player two can get to the other side

        if self.validate_pawn_move(opponent, opponent_location, left_move) is True and left_move not in used:  # check left move
            used[opponent_location] = opponent_location
            return self.fair_play_rule(opponent, left_move, used)
            return True

        if self.validate_pawn_move(opponent, opponent_location, right_move) is True and right_move not in used:  # check right move
            used[opponent_location] = opponent_location
            self.fair_play_rule(opponent, right_move, used)
            return True

        if self.validate_pawn_move(opponent, opponent_location, up_move) is True and up_move not in used:  # check up move
            used[opponent_location] = opponent_location
            return self.fair_play_rule(opponent, up_move, used)
            return True

        if self.validate_pawn_move(opponent, opponent_location, down_move) is True and down_move not in used:  # check down move
            used[opponent_location] = opponent_location
            return self.fair_play_rule(opponent, down_move, used)
            return True

        else:
            player_object = self.get_opponent(opponent)
            player_number = player_object.get_player_number()
            self.set_turn(player_number)
            return "breaks the fair play rule"

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
        player_object = self.check_player(player)
        if self.check_for_fence(fence_direction, coordinate) is False and \
                self.get_status() == "IN PROGRESS" and \
                player_object.get_fences() > 0 and \
                coordinate[0] >= 0 and coordinate[1] >= 0 and coordinate[0] <= 8 and coordinate[1] <= 8 \
                and self.get_turn() == player:
            # if no fence already there and game in progress and player has remaining fences and not negative
            return True
        else:
            return False

    def is_winner(self, player):
        """To be used after making a move - checks to see whether player has won.
        :param:
        a single integer representing the player number as a parameter
        :return:
        returns True if that player has won and False if that player has not won."""
        player_object = self.check_player(player)
        player_location = player_object.get_player_position()
        if player == 1:
            if player_location[1] == 8:
                return True
            else:
                return False
        elif player == 2:
            if player_location[1] == 0:
                return True
            else:
                return False


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
        if self.get_player_number() == 1:  # starting positions
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
