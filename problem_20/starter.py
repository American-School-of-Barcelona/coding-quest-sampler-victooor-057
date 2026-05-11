"""
CodingQuest Problem 20: Tic tac toe

Your input data is in input.txt.
The data has been loaded into a list called `data` for you.
Each item in the list is one line from the file, as a string.

Each line represents one game of tic-tac-toe.
The numbers on each line are the squares played, in order (X goes first).
Squares are numbered like this:

 1 | 2 | 3
---|---|---
 4 | 5 | 6
---|---|---
 7 | 8 | 9

Process each game until someone wins (3 in a row), then stop.
If nobody wins after 9 moves, it's a draw.

Your answer is: (games won by X) * (games won by O) * (drawn games)

Write your solution below the comment line.
"""

# --- Load the data (don't change this) ---
with open("input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]

# Take a look at the first few lines
print(f"Loaded {len(data)} lines.")
print("First 5 lines:")
for line in data[:5]:
    print("  ", line)
print()

# --- Your code here ---
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9},
    {1, 4, 7},
    {2, 5, 8},
    {3, 6, 9},
    {1, 5, 9},
    {3, 5, 7}
]

x_wins = 0
o_wins = 0
draws = 0

for line in data:
    moves = list(map(int, line.split()))

    x_moves = set()
    o_moves = set()

    winner = None

    for i, move in enumerate(moves):

        if i % 2 == 0:
            x_moves.add(move)

            for combo in wins:
                if combo.issubset(x_moves):
                    winner = "X"
                    break

        else:
            o_moves.add(move)

            for combo in wins:
                if combo.issubset(o_moves):
                    winner = "O"
                    break

        if winner:
            break

    if winner == "X":
        x_wins += 1
    elif winner == "O":
        o_wins += 1
    else:
        draws += 1

answer = x_wins * o_wins * draws

print("X wins:", x_wins)
print("O wins:", o_wins)
print("Draws:", draws)
print("Answer:", answer)