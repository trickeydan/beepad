"""Save this file as code.py."""
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