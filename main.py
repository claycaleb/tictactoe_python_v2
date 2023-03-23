from player import Player
from random import choice
from os import name, system

grid = ("a".center(6) + "b".center(6) + "c".center(6)).rjust(21) + '''
  ┏━━━━━┳━━━━━┳━━━━━┓
1 ┃     ┃     ┃     ┃
  ┣━━━━━╋━━━━━╋━━━━━┫
2 ┃     ┃     ┃     ┃
  ┣━━━━━╋━━━━━╋━━━━━┫
3 ┃     ┃     ┃     ┃
  ┗━━━━━┻━━━━━┻━━━━━┛'''

grid_indices = {
    "a1": (49, 1),
    "b1": (55, 2),
    "c1": (61, 3),
    "a2": (93, 4),
    "b2": (99, 5),
    "c2": (105, 6),
    "a3": (137, 7),
    "b3": (143, 8),
    "c3": (149, 9)
}

user = Player("", "", [], None)
cpu = Player("", "", [], None)


def game_reset():
    global grid, grid_indices, user, cpu

    grid = ("a".center(6) + "b".center(6) + "c".center(6)).rjust(21) + '''
  ┏━━━━━┳━━━━━┳━━━━━┓
1 ┃     ┃     ┃     ┃
  ┣━━━━━╋━━━━━╋━━━━━┫
2 ┃     ┃     ┃     ┃
  ┣━━━━━╋━━━━━╋━━━━━┫
3 ┃     ┃     ┃     ┃
  ┗━━━━━┻━━━━━┻━━━━━┛'''

    grid_indices = {
        "a1": (49, 1),
        "b1": (55, 2),
        "c1": (61, 3),
        "a2": (93, 4),
        "b2": (99, 5),
        "c2": (105, 6),
        "a3": (137, 7),
        "b3": (143, 8),
        "c3": (149, 9)
    }

    user = Player("", "", [], None)
    cpu = Player("", "", [], None)


def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")


def select_x_or_o():
    char_choices = "XO"
    user.char = input("Choose X or O: ").upper()
    cpu.char = char_choices.replace(user.char, "")
    while user.char.upper() not in char_choices:
        print("Invalid input. Try again.")
        user.char = input("X or O? ").upper()
        cpu.char = char_choices.replace(user.char, "")


def grid_update(char, cell):
    global grid
    grid = grid[:grid_indices[cell][0]] + grid[grid_indices[cell][0]:].replace(' ', f'{char}', 1)

    grid_indices.pop(cell)


def user_select_spot():
    user.cell = input("Select a spot: ")
    while user.cell not in grid_indices:
        print("Invalid input. Try again.")
        user.cell = input("Select a spot: ")

    user.cells.append(grid_indices[user.cell][1])

    grid_update(user.char, user.cell)


def cpu_select_spot():
    cpu.cell = choice(list(grid_indices.keys()))

    cpu.cells.append(grid_indices[cpu.cell][1])

    grid_update(cpu.char, cpu.cell)


def play_again():
    play_again_choices = "yn"
    user_response = input("Play again? (Y/N) ")
    while user_response.lower() not in play_again_choices:
        user_response = input("Play again? (Y/N) ")

    if user_response.lower() == "y":
        game_reset()
        play_game()
    else:
        print("Thanks for playing!")


def play_game():
    clear()

    select_x_or_o()

    clear()

    user.goes_first = choice([True, False])

    if user.goes_first:
        print("You pick first!")
        print(grid)
        while True:
            user_select_spot()

            clear()

            if user.is_winner():
                print(grid)
                print("You win!\n")
                break

            if len(grid_indices) == 0:
                print(grid)
                print("It's a draw!\n")
                break

            cpu_select_spot()

            if cpu.is_winner():
                print(grid)
                print("You lose!\n")
                break

            print(grid)

    else:
        print("Computer picks first!")
        while True:
            cpu_select_spot()

            print(grid)

            if cpu.is_winner():
                print("You lose!")
                break

            if len(grid_indices) == 0:
                print(grid)
                print("It's a draw!")
                break

            user_select_spot()

            clear()

            if user.is_winner():
                print(grid)
                print("You win!")
                break

    play_again()


if __name__ == '__main__':
    play_game()
