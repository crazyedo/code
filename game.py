#!/usr/bin/env -S uv run
# /// script
# dependencies = ["readchar",]
# ///

from readchar import readchar

# Character position
x = 2
y = 2

while True:
    # Clear screen
    print("\n" * 50)

    # Draw grid
    for row in range(5):
        for col in range(5):
            if row == y and col == x:
                print("😊", end=" ")
            else:
                print("⬜", end=" ")
        print()

    # Get single keypress (no Enter needed!)
    key = readchar()

    # Move character
    if key == "w" and y > 0:
        y -= 1
    elif key == "s" and y < 4:
        y += 1
    elif key == "a" and x > 0:
        x -= 1
    elif key == "d" and x < 4:
        x += 1
    elif key == "q":  # quit key
        break
