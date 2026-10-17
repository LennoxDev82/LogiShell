import json

# Please use the config.json to configure!
_DEFAULTS = {
    "usb_manufacturer": "Logitech",
    "usb_product": "Gaming Keyboard G213",
    "usb_vid": 0x046D,
    "usb_pid": 0xC336,
    "volume_label": "GHUB MEMORY",
    "boot_wait_time": 1, #You can change boot_wait_time & shell_wait if your pc is from the 1980s.
    "shell_wait": 1,
    "payload_file": "configuration/payload.txt",
    "autorun_on_boot": True, # Please be aware that this fires off the payload on boot, set it to "False" if you want to configure (in config.json).
    "hide_usb_storage": False, #IMPORTANT: Only change this if you know what you are doing. Otherwise, you will lock yourself out!
    "close_shell_after_payload": False,
    "close_shell_delay": 1,
}


def _parse_int(value):
    if isinstance(value, int):
        return value
    return int(str(value).strip(), 0)


def load():
    cfg = dict(_DEFAULTS)
    try:
        with open("/configuration/config.json", "r") as f:
            raw = json.load(f)
    except (OSError, ValueError):
        return cfg
    for key in _DEFAULTS:
        if key not in raw:
            continue
        val = raw[key]
        if key in ("usb_vid", "usb_pid"):
            try:
                cfg[key] = _parse_int(val)
            except ValueError:
                pass
        elif key in ("boot_wait_time", "shell_wait", "close_shell_delay"):
            try:
                cfg[key] = int(val)
            except (TypeError, ValueError):
                pass
        elif key in ("autorun_on_boot", "hide_usb_storage", "close_shell_after_payload"):
            if isinstance(val, bool):
                cfg[key] = val
            else:
                cfg[key] = str(val).strip().lower() in ("1", "true", "yes")
        else:
            cfg[key] = val
    return cfg
