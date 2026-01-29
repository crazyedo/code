#!/usr/bin/env -S uv run
# /// script
# dependencies = ["readchar",]
# ///

from readchar import readchar

# Character position
x = 2
y = 1

world_x = 10
world_y = 10

while True:
    # Clear screen
    print("\n" * 50)

    # Draw grid
    for row in range(world_x):
        for col in range(world_y):
            if row == y and col == x:
                print("😊", end=" ")
            else:
                print("⬜", end=" ")
        print()


    print('x', x, 'y', y)

    # Get single keypress (no Enter needed!)
    key = readchar()

    # Move character
    if key == "w"  and y >0:
        y -= 1
    elif key == "s" and y < world_y - 1:
        y += 1
    elif key == "a" and x > 0:
        x -= 1
    elif key == "d" and x < world_x - 1:
        x += 1
    elif key == "q":  # quit key
        break
