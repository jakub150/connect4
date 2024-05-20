# connect 4

<b>Cover Notes</b>

I am using Python to code the connect four game as it is more convenient than using other languages.

The code will start by the Initiate_Game_Grid function. Inside the Initiate_Game_Grid, it will ask player to enter the size of game grid and the winning row length. Then, it will create the game grid according to the size with the 2D list, and show the created grid to the players.

Then, it will run into a loop which will run continuosly until a player wins or it comes to a draw. Inside the loop, the player will take turn to choose a column in the game grid. Error will be raised if the input is invalid or the column is full. After that, the system will check if the current player won the game. The winning conditions are a row, a column or a diagonal that lengths longer than the winning row length. If one of the conditions is achieved, that player in that turn wins the game and it comes to the end. If not, the system will check if it is a draw. The condition for a draw is every grid slots are filled and no player still achieve the winning conditions, and the game will also come to the end.

After that, if no conditions for winning or draw is matched, then the other player will take his/her turn. It will repeat until the game ends.

I think there is no extra requirement for running this code in a Linux/Mac environment since I am not using any extra python libraries. So, just run this python file and it should be fine.

I know there is room for improvement for this code, but I don't have enough time to perfect the code.

Thanks.