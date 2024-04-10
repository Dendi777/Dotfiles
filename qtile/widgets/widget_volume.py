from os import system
from libqtile import bar
from libqtile.widget import base

class Volume(base.ThreadPoolText):
    """
    Widget draw volume
    """

    def __init__(self, **config):
        base.ThreadPoolText.__init__(self, "0", **config)
        self.volume = None

    def _configure(self, qtile, bar):
        base.ThreadPoolText._configure(self, qtile, bar) 

    def get_volume(self):
        self.volume = system("wpctl get-volume @DEFAULT_AUDIO_SINK@ | awk -F. '{print $2}'")

    def poll(self):
        self.get_volume()
        return self.format.format(self.volume)
