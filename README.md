# BeePad

A MacroPad full of bees.

This is a library for building bee-powered RGB macro keys using the [Adafruit RP2040 Macropad](https://www.adafruit.com/product/5128).

It supports 20 pages of 12 macros, so 240 individual macros.

It is written using [CircuitPython 7](https://circuitpython.org/).

## Usage

You will need to write a `code.py` to define your macros.

```python
from beepad import BeePad
from beepad.keymap import Keymap, TypeAction

pad = BeePad([
    Keymap("Git", [
        TypeAction("gst", "git status\n"),
        TypeAction("gc", "git commit\n"),
        TypeAction("gc -m", "git commit -m @"), # US Keyboard :(

        TypeAction("gca!", "git commit --amend\n"),
        TypeAction("gd", "git diff \n"),
        TypeAction("gd -s", "git diff --staged\n"),

        TypeAction("ga .", "git add .\n"),        
        TypeAction("ggpush", "git push origin $(git rev-parse --abbrev-ref HEAD)\n"),
        TypeAction("ggpull", "git pull origin $(git rev-parse --abbrev-ref HEAD)\n"),

        TypeAction("main", "git checkout main\n"),
        TypeAction("grm", "git rebase origin/main\n"),
        TypeAction("dgt", "git checkout -b dgt/"),
    ]),
    # Add more keymaps here!
])

while True:
    pad.buzz()
```

## Updating

The `boot.py` file disables the serial port and USB flash drive in normal operation.

You can re-enable them by holding the top-left key when resetting the device.

Alternatively you can just not copy the `boot.py` to your device, although this will mean that there is always an additional flash drive connected to your computer, risking corruption of the flash on the RP2040.

## Requirements

The following CircuitPython libraries are required.

You will need to install them in `lib/`.

```
adafruit_bus_device
adafruit_debouncer
adafruit_displayio_sh1106
adafruit_display_text
adafruit_hid
adafruit_macropad
adafruit_midi
adafruit_simple_text_display
neopixel
```