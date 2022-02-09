import pyautogui;
import mouse;
import keyboard;



def givePixelsGetRgb():
    while True:  # making a loop
        try:  # used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed('q'):  # if key 'q' is pressed
                while keyboard.is_pressed('q'):
                    continue
                im = pyautogui.screenshot();
                #adamClick.click(222, 357)
                #print(im.getpixel((357, 222)));
                print(im.getpixel((696, 139)));
                # finishing the loop
        except:
            break

        # Press the green button in the gutter to run the script.


if __name__ == '__main__':
    givePixelsGetRgb()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
