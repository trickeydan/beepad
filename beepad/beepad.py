from beepad.beepad_base import BeePadBase
from beepad.keymap import Keymap, Action

from .constants import PIXEL_NUM
from .colours import colorwheel

from .display_layout import DisplayLayout

class BeePad(BeePadBase):
    
    def __init__(self, keymaps) -> None:
        super().__init__()

        self.tick_count = 0

        assert len(keymaps) <= 20
        self._keymaps = keymaps
        
        self._keymaps += [Keymap(str(i + len(keymaps)), []) for i in range(20 - len(keymaps))]

        self.layout = DisplayLayout(self.display)
        self._current_screen: int = 0
        self.layout.show_keymap(self._keymaps[0])
        
    @property
    def current_screen(self) -> int:
        return self._current_screen

    @property
    def current_keymap(self) -> Keymap:
        return self._keymaps[self.current_screen]

    @current_screen.setter
    def current_screen(self, val: int): 
        if val != self._current_screen:
            self._current_screen = val
            self.layout.show_keymap(self._keymaps[val])

    def buzz(self):
        self.tick_count += 1
        self.current_screen = self.encoder.position % 20
        event = self.keys.events.get()
        if event:
            if event.pressed:
                action = self.current_keymap.actions[event.key_number]
                action.exec(self)

        for i in range(PIXEL_NUM):
            pixel_index = (i * 256 // PIXEL_NUM) + (self.tick_count % 256)
            self.pixels[i] = colorwheel(pixel_index & 255)
            self.pixels.show()

        self.layout.refresh()
