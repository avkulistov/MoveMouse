import pyautogui
from time import sleep


if __name__ == '__main__':
    step = 300
    sleep_time = 5

    while True:
        x, y = pyautogui.position()
        pyautogui.leftClick()
        sleep(sleep_time)

        pyautogui.scroll(-300)

        pyautogui.moveTo(x + step, y - step, 1, pyautogui.easeInExpo)
        pyautogui.leftClick()
        sleep(sleep_time)

        pyautogui.scroll(300)

        pyautogui.moveTo(x, y, 1, pyautogui.easeInExpo)
        sleep(7)
