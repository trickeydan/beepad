import board
import busio
import displayio
import digitalio
import rotaryio
import keypad
import usb_hid
import neopixel

from adafruit_displayio_sh1106 import SH1106
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.consumer_control import ConsumerControl

from .constants import OLED_HEIGHT, OLED_WIDTH, PIXEL_ORDER, PIXEL_BRIGHTNESS, PIXEL_NUM

class BeePadBase:

    def __init__(self):

        self._init_display()
        self._init_keypad()
        self._init_encoder()
        self._init_usb_hid()
        self._init_neopixel()

    def _init_display(self):
        displayio.release_displays()
        spi = busio.SPI(board.SCK, board.MOSI)
        display_bus = displayio.FourWire(
            spi,
            command=board.OLED_DC,
            chip_select=board.OLED_CS,
            reset=board.OLED_RESET,
            baudrate=1000000,
        )
        self.display = SH1106(display_bus, width=OLED_WIDTH, height=OLED_HEIGHT)
        self.display.auto_refresh = False

    def _init_keypad(self):
        """Initialise the keypad."""
        key_pins = (
            board.KEY1,
            board.KEY2,
            board.KEY3,
            board.KEY4,
            board.KEY5,
            board.KEY6,
            board.KEY7,
            board.KEY8,
            board.KEY9,
            board.KEY10,
            board.KEY11,
            board.KEY12,
        )
        self.keys = keypad.Keys(key_pins, value_when_pressed=False, pull=True)

    def _init_encoder(self):
        self.button = digitalio.DigitalInOut(board.BUTTON)
        self.button.switch_to_input(pull=digitalio.Pull.UP)
        self.encoder = rotaryio.IncrementalEncoder(board.ROTB, board.ROTA)
        self.encoder.position = 0

    def _init_usb_hid(self):
        self.keyboard = Keyboard(usb_hid.devices)
        self.keyboard_layout = KeyboardLayoutUS(self.keyboard)
        self.consumer_control = ConsumerControl(usb_hid.devices)

    def _init_neopixel(self):
        self.pixels = neopixel.NeoPixel(
            board.NEOPIXEL,
            PIXEL_NUM,
            brightness=PIXEL_BRIGHTNESS,
            auto_write=False,
            pixel_order=PIXEL_ORDER,
        )
