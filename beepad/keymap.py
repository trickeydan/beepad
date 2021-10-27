from time import sleep

class Action:

    def __init__(self, name: str):
        self.name = name

    def exec(self, pad: 'BeePad'):
        pass

class TypeAction:

    def __init__(self, name: str, command: str):
        self.name = name
        self.command = command

    def exec(self, pad: 'BeePad'):
        pad.keyboard_layout.write(self.command)

class LambdaAction:
    def __init__(self, name: str, callable):
        self.name = name
        self.callable = callable

    def exec(self, pad: 'BeePad'):
        self.callable(pad)


class ResetEncoderAction:

    def __init__(self, name: str):
        self.name = name

    def exec(self, pad: 'BeePad'):
        sleep(5)
        pad.encoder.position = 0



class Keymap:

    def __init__(
        self,
        title: str,
        actions: 'List[Action]',
    ):
        self.title = title
        self.actions = actions

        assert len(self.actions) <= 12

        # Change the missing buttons
        for _ in range(12 - len(self.actions)):
            self.actions.append(Action("-"))
