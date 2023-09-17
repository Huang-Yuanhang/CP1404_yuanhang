class Band:

    def __init__(self, name=""):
        self.name = name
        self.musicians = []

    def __str__(self):
        musician_strings = []
        for musician in self.musicians:
            musician_strings.append(str(musician))
        band_string = str(", ".join(musician_strings))
        return f"{self.name} ({band_string})"

    def __repr__(self):
        return str(vars(self))

    def add(self, musician):
        self.musicians.append(musician)

    def play(self):
        musician_play_strings = []
        for musician in self.musicians:
            musician_play_strings.append(musician.play())
        return str("\n".join(musician_play_strings))
