import pyautogui;
import mouse;
import keyboard;


def givePixelsGetRgb():
    while True:  # making a loop
        try:  # used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed('m'):
                while keyboard.is_pressed('m'):
                    continue;


                print(mouse.get_position())

        except:
            break

        # Press the green button in the gutter to run the script.


if __name__ == '__main__':
    givePixelsGetRgb()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/