<div align="center">

# LogiShell
<img width="50%" height="562" alt="logishell bg" src="https://github.com/user-attachments/assets/bf7b6f32-8656-4458-b68d-81ed78e8abf6" />

</div>

---

Logishell is a CircuitPython firmware for the Waveshare RP2040 Geek, that emulates a Logitech Keyboard and works as a Keystroke Injection Device, that fires off a powershell payload of your choice. It is fully customizable.

It was originally made to load cheating software quickly via powershell for LAN tournaments. But is now a universal tool for powershell payloads.

**Educational! Please only use this on permitted systems!**

---

### Installation

1. You need a Waveshare RP2040 GEEK (Retail: 10-20$) (Or a similar Board)
2. Install [CircuitPython UF2](https://circuitpython.org/board/waveshare_rp2040_geek/)
3. Install the [adafruit_hid & adafruit_imageload libary](https://circuitpython.org/libraries). (You can download the whole bundle)
4. Plug in your GEEK and paste this whole repo into the drive.
5. Upon Replugging your GEEK, the test payload "winver" should fire off.

---

### Configuration

**Payload:** Open [payload.txt](configuration/payload.txt) and paste in your payload. (Supports Multi Line)

**Config:** Open [config.json](configuration/config.json) and change what you need.

Disable autorun_on_boot if you want to update in peace.

Enable close_shell_after_payload if you want the shell to be closed after the payload fired.

**Only Enable hide_usb_storage if you know what you are doing! You can lock yourself out!**

---

### Efficiency

From plugging in, till the payload is fired off, it takes around 5-7 seconds. (Depends on the lenght of the payload)

---

### Additional Information

• Only tested on Windows 11 Systems.

• Only US Keyboard Layout Supported.

• This is no 1:1 Emulation, you can still find traces of the GEEK.
