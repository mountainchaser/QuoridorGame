# Quoridor Game

Quoridor is a board game where players navigate fences placed by their opponents while attempting to reach the other side of the board.

Currently this repository contains the back end of the game. I will be building a UI for it as well.

You can see the rules of the game in this [video](https://www.youtube.com/watch?v=6ISruhN0Hc0) and [this rule summary](http://lode.ameije.com/quoridor/Rules/quoridor_rules.html).


## Gameplay

Here's an example of how the QuoridorGame class can be used:

```
q = QuoridorGame()
q.move_pawn(2, (4,7)) #moves the Player2 pawn -- invalid move because only Player1 can start, returns False
q.move_pawn(1, (4,1)) #moves the Player1 pawn -- valid move, returns True
q.place_fence(1, 'h',(6,5)) #places Player1's fence -- out of turn move, returns False 
q.move_pawn(2, (4,7)) #moves the Player2 pawn -- valid move, returns True
q.place_fence(1, 'h',(6,5)) #places Player1's fence -- returns True
q.place_fence(2, 'v',(3,3)) #places Player2's fence -- returns True
q.is_winner(1) #returns False because Player 1 has not won
q.is_winner(2) #returns False because Player 2 has not won

```
