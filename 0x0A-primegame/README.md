# Prime Game

## Project Overview

The Prime Game project involves implementing an algorithm to determine the winner of a game where players take turns choosing prime numbers from a set of consecutive integers. The chosen prime number and its multiples are removed from the set. The player who cannot make a move loses the game. Maria and Ben play the game for a number of rounds, and the goal is to determine who wins the most rounds.

## Requirements

- **Python Version:** 3.4.3 (or higher)
- **Allowed Editors:** vi, vim, emacs
- **File Naming:** All files should end with a new line, and the first line should be exactly `#!/usr/bin/python3`.
- **Coding Style:** PEP 8 style (version 1.7.x)
- **Executable Files:** All code files must be executable.
- **No External Packages:** You cannot import any packages for this task.

## Task

Implement the function `isWinner(x, nums)` which determines the winner of each game round and returns the name of the player who won the most rounds.

### Function Prototype

```python
def isWinner(x, nums):
    """
    Determine who won the most rounds of the Prime Game.

    Args:
        x (int): Number of rounds.
        nums (List[int]): List of integers representing the value of n for each round.

    Returns:
        str: Name of the player who won the most rounds ("Maria" or "Ben").
             If the winner cannot be determined, return None.
    """
    pass

Example

>>> isWinner(3, [4, 5, 1])
"Ben"

Installation and Usage

1. Clone the repository :-

git clone https://github.com/2012Inga/alx-interview/0x0A-primegame

2. Navigate to the project directory:

cd alx-interview/0x0A-primegame

3. Run the test script:

./main_0.py

4. Example output:

Winner: Ben


Resources
Prime Numbers
Sieve of Eratosthenes
Game Theory Basics
Dynamic Programming

License
This project is licensed under the MIT License - see the LICENSE file for details.

