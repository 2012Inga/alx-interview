N Queens Problem Solver
This project solves the N Queens problem using the backtracking algorithm. The goal is to place N non-attacking queens on an N×N chessboard. The solution is implemented in Python and provides a command-line interface for user interaction.

Description
The N Queens problem involves placing N queens on an N×N chessboard such that no two queens can attack each other. This means that no two queens can be on the same row, column, or diagonal. The provided script uses a backtracking algorithm to find all possible solutions and prints them in a specific format.

Usage
To run the script, use the following command:


./0-nqueens.py N
Arguments
N: An integer representing the size of the chessboard and the number of queens. N must be greater than or equal to 4.
Error Handling
If the user provides the wrong number of arguments, the script will print Usage: nqueens N and exit with status 1.
If N is not an integer, the script will print N must be a number and exit with status 1.
If N is less than 4, the script will print N must be at least 4 and exit with status 1.
Output
The script prints all possible solutions to the N Queens problem. Each solution is represented as a list of lists, where each inner list represents the position of a queen on the board.

For example, for N = 4, the output will be:


[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
Each solution represents the positions of queens on the board, where each pair [row, column] specifies the position of a queen.

Requirements
Python 3.x (tested with version 3.4.3)
The script should be executable: chmod +x 0-nqueens.py
Example
To solve the N Queens problem for N = 4, run:


./0-nqueens.py 4
You should see output similar to:


[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For any questions or issues, please contact [your email or contact information].

This README file provides an overview of the project, usage instructions, and information about the requirements and outputs. Adjust the "Contact" section and any other specific details as needed for your project.
