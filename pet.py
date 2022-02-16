class Pet:
    def __init__(
        self,
        name="неизвестно",
        fullness=0,
        health=0,
        mood=0,
        cleanness=0,
        energy=0
    ):
        self.portrait = "assets/calm.png"
        self.name = name
        self.fullness = fullness
        self.health = health
        self.mood = mood
        self.cleanness = cleanness
        self.energy = energy
        self.fullness_change = -1
        self.health_change = -1
        self.mood_change = -1
        self.cleanness_change = -1
        self.energy_change = -1

    def feed(self, num):
        self.fullness += num
        print(f"{self.name} съел {num} и теперь у него {self.fullness} сытости")

    def change_portrait(self):
        pass

    def decrease_stats(self):
        self.fullness += self.fullness_change
        self.health += self.health_change
        self.mood += self.mood_change
        self.cleanness += self.cleanness_change
        self.energy += self.energy_change