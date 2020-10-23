# Tic Tac Toe
Goal: Build a Tic Tac Toe game using a dictionary to model the game board.

## The board
* Give a name to every space on the board. For example, TL might be "top left", ML might be "middle left", etc. Be sure they all have unique names.
* The names will be your keys in the dictionary. Your values will be the symbol in that space. Start with `' '` (space - meaning it's blank). Therefore a key:value pair might be `'TL': ' '`
* Build your dictionary so all 9 spaces of the Tic Tac Toe board are defined.

## Printing the board
* Make a function that uses the dictonary as a parameter.
* Print the top row of the board using `|` as dividers between each space.
* Print the first horizontal divider `-+-+-`
* Print the middle row
* etc
* Call the function to make sure it looks OK. Add spaces as needed to make it look better.

## The game
* Print the board at the start, between every turn, and at the end.
* X goes first. Ask the player which space to choose, using the keys.
* O goes next. 
* Repeat

## Ending the game
* How do you want to end? 
  * Fill all 9 spaces and then check for a winner?
  * Check for a winner after each turn. End if somebody won - or it's a tie.
* Think through this before you start typing. You'll want a plan!

