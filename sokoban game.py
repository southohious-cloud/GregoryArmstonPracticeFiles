def main():
    size = 5
    player = [size // 2, size // 2]   # row, col
    history = []

    moves = {
        "move up":    (-1, 0),
        "move down":  (1, 0),
        "move left":  (0, -1),
        "move right": (0, 1)
    }

    while True:
        draw_grid(size, player)
        action = input("Action: ").strip().lower()

        if action in moves:
            dr, dc = moves[action]
            new_r = player[0] + dr
            new_c = player[1] + dc

            # Stay inside the grid
            if 0 <= new_r < size and 0 <= new_c < size:
                history.append(tuple(player))
                player[0], player[1] = new_r, new_c
            else:
                print("You can't move outside the grid.")

        elif action == "undo":
            if history:
                player[0], player[1] = history.pop()
            else:
                print("Nothing to undo.")

        elif action == "restart":
            history.clear()
            player[:] = [size // 2, size // 2]

        elif action == "quit":
            print("Goodbye.")
            break

        else:
            print("Invalid action.")


def draw_grid(size, player):
    print("\n" + "=" * 20)
    for r in range(size):
        row = ""
        for c in range(size):
            if [r, c] == player:
                row += " P "
            else:
                row += " . "
        print(row)
    print("=" * 20 + "\n")


main()
