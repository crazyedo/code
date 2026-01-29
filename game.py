#!/usr/bin/env -S uv run
# /// script
# dependencies = ["readchar",]
# ///

from readchar import readchar

# Character position
hero_x = 2
hero_y = 1

world_x = 10
world_y = 10

while True:
    # Clear screen
    print("\n" * 50)

    # Draw grid
    for row in range(world_x):
        for col in range(world_y):
            if row == hero_y and col == hero_x:
                print("😊", end=" ")
            else:
                print("⬜", end=" ")
        print()


    print('x', hero_x, 'y', hero_y)

    # Get single keypress (no Enter needed!)
    key = readchar()

    # Move character
    if key == "w"  and hero_y >0:
        hero_y -= 1
    elif key == "s" and hero_y < world_y - 1:
        hero_y += 1
    elif key == "a" and hero_x > 0:
        hero_x -= 1
    elif key == "d" and hero_x < world_x - 1:
        hero_x += 1
    elif key == "q":  # quit key
        break
