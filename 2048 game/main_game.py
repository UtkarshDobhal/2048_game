# 2048.py

import logic

def print_grid(mat):
    for row in mat:
        print(row)
    print()


if __name__ == '__main__':
    mat = logic.start_game()

    while True:
        print_grid(mat)
        x = input("Press the command: ")

        if x in ['W', 'w']:
            mat, flag = logic.move_up(mat)
        elif x in ['S', 's']:
            mat, flag = logic.move_down(mat)
        elif x in ['A', 'a']:
            mat, flag = logic.move_left(mat)
        elif x in ['D', 'd']:
            mat, flag = logic.move_right(mat)
        else:
            print("Invalid Key Pressed")
            continue

        status = logic.get_current_state(mat)
        print(status)
        
        if status == 'GAME NOT OVER':
            if flag:
                logic.add_new_2(mat)
        else:
            break

    print_grid(mat)
    if status == 'WON':
        print("Congratulations, you have won!")
    else:
        print("Game Over!")
