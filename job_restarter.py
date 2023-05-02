from pynput import keyboard
from PIL import ImageGrab
import time
import random
import cv2
import numpy as np
import os
from datetime import datetime

pattern = cv2.imread(os.path.join(os.getcwd(), "./pattern.png"))

time_offset = 0


def waitOnPress(key):
    pass


def waitOnRelease(key):
    if key == keyboard.Key.space:
        return False
    else:
        print("foo")


def stopOnPress(key):
    pass


def stopOnRelease(key):
    if key == keyboard.Key.space:
        global stop
        stop = True
        return False
    else:
        pass


def screenshot():
    screenshot = ImageGrab.grab().convert("RGB")
    open_cv_image = np.array(screenshot)
    open_cv_image = open_cv_image[:, :, ::-1].copy()
    return open_cv_image


def wait():
    with keyboard.Listener(
        on_press=waitOnPress, on_release=waitOnRelease
    ) as listener:
        listener.join()


def afkStep():
    k = keyboard.Controller()
    k.press(keyboard.Key.ctrl_l)
    time.sleep(random.random())
    k.release(keyboard.Key.ctrl_l)


endMenuPos = (309, 668)
endMenuSize = (1306, 286)


def loop():
    global stop
    listener = keyboard.Listener(on_press=stopOnPress, on_release=stopOnRelease)
    listener.start()

    k = keyboard.Controller()

    stop = False

    with open("log.txt", "a", encoding="UTF-8") as f:
        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        f.write("\n" + date_time + " -- started")

    time_started = 0

    while True:
        if stop:
            return

        screen = screenshot()

        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

        if isPatternThere(pattern, screen):
            print(date_time, " -- ", "Restarting...")
            cv2.imwrite(
                os.path.join(os.getcwd(), "screenshots", str(time.time()) + ".png"),
                screen,
            )

            clickRestart()

            time.sleep(20 + time_offset)

            if stop:
                return

            f = open("log.txt", "a")
            f.write("\n" + date_time + " -- restarted")

            if time_started > 0:
                t = time.time() - time_started
                f.write(", lasted for " + str(t) + " secs")
            f.close()

            time_started = time.time()

            confirmMenu1()
            time.sleep(2 + time_offset)
            confirmMenu1()

            time.sleep(0.1)

            k.press(keyboard.Key.enter)
            time.sleep(0.05)
            k.release(keyboard.Key.enter)

            time.sleep(0.1)

            k.press(keyboard.Key.enter)
            time.sleep(0.05)
            k.release(keyboard.Key.enter)

            time.sleep(0.1)

            k.press(keyboard.Key.enter)
            time.sleep(0.05)
            k.release(keyboard.Key.enter)
        else:
            print(date_time, " -- ", "Continue")
            afkStep()

        time.sleep(5)


def confirmMenu1():
    global stop

    if stop:
        return

    k = keyboard.Controller()
    time.sleep(0.2)

    k.press("z")
    time.sleep(0.1)
    k.release("z")
    time.sleep(0.1)

    k.press(keyboard.Key.enter)
    time.sleep(0.05)
    k.release(keyboard.Key.enter)


def clickRestart():
    k = keyboard.Controller()

    k.press("s")
    time.sleep(0.1)
    k.release("s")

    time.sleep(0.1)

    k.press("s")
    time.sleep(0.1)
    k.release("s")

    time.sleep(0.1)

    k.press(keyboard.Key.enter)
    time.sleep(0.1)
    k.release(keyboard.Key.enter)


def isPatternThere(template, img):
    template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)

    (yCoords, xCoords) = np.where(res >= 0.35)
    return len(yCoords) > 0


stop = False
wait()
loop()

# confirmMenu1()
