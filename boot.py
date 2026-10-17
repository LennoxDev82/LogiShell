import sys

sys.path.insert(0, "/scripts")

import storage
import supervisor
import usb_cdc
import usb_hid

import device_config

cfg = device_config.load()
vid = cfg["usb_vid"]
pid = cfg["usb_pid"]

supervisor.set_usb_identification(
    manufacturer=cfg["usb_manufacturer"],
    product=cfg["usb_product"],
    vid=vid,
    pid=pid,
)

label = cfg["volume_label"]
if label:
    try:
        storage.remount("/", False)
        storage.getmount("/").label = label[:11]
        storage.remount("/", True)
    except Exception:
        storage.remount("/", True)

try:
    import usb_midi
    usb_midi.disable()
except (ImportError, AttributeError):
    pass

maintenance = False
try:
    open("/debug").close()
    maintenance = True
    usb_cdc.enable()
except OSError:
    usb_cdc.disable()

if cfg["hide_usb_storage"] and not maintenance:
    storage.disable_usb_drive()

usb_hid.enable(
    (usb_hid.Device.KEYBOARD, usb_hid.Device.CONSUMER_CONTROL),
    vid=vid,
    pid=pid,
)
