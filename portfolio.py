import json

class Portfolio:
    def __init__(self):
        with open("data.json", "r", encoding="utf-8") as f:
            self.data = json.load(f)

    def show_aboutme(self):
        info = self.data["me"]
        print(f"  Имя        : {info['name']}")
        print(f"  Возраст    : {info['age']}")
        print(f"  Чем занимаюсь: {info['description']}")
        print(f"  Факты      : {info['facts']}")

    def show_goal(self):
        info = self.data["goal"]
        print(f"  Цель       : {info['text']}")

    def show_story(self):
        info = self.data["story"]
        print(f"  История    : {info['text']}")

    def show_mentor(self):
        info = self.data["mentor"]
        print(f"  Ментор     : {info['text']}")

    def show_progress(self):
        info = self.data["progress"]
        print(f"  Точка А    : {info['point_a']}")
        print(f"  Точка Б    : {info['pont_b']}")

    def show_hobby(self):
        info = self.data["hobby"]
        hobbies = info['hobby']
        if isinstance(hobbies, list):
            print("  Хобби:")
            for i, h in enumerate(hobbies, 1):
                print(f"     {i}. {h}")
        else:
            print(f"  Хобби      : {hobbies}")

    def show_works(self):
        info = self.data["works"]
        print(f"  Работа 1   : {info['work1']}\n")
        print(f"  Работа 2   : {info['work2']}\n")
        print(f"  Работа 3   : {info['work3']}")

    def show_GitHub(self):
        info = self.data["GitHub"]
        print(f"  GitHub     : {info['GitHub']}")