class Individual:
    def __init__(self, id, gender, age, intro, habits, coord):
        self.id = id
        self.gender = gender
        self.age = age
        self.intro = intro
        self.habits = habits
        self.coord = coord

    def get_habits_set(self):
        return set(self.habits.split(', '))

