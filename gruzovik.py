from new import Car


class Gruzovik(Car):
    def __init__(self, color, max_velocity, weight, mark, max_weight_gruz):
        super().__init__(color, max_velocity, weight, mark)
        self.max_weight_gruz = max_weight_gruz
        self.is_have_gruz = False

    def pick_up(self, weight):
        if weight <= self.max_weight_gruz:
            print("Груз погружен")
            self.is_have_gruz = True
        else:
            print("Груз превышает максимально допустимый вес груза")

    def pick_off(self):
        if self.is_have_gruz:
            print("Груз сгружен")
        else:
            print("Груза нет")

    def turn_on(self):
        if not super().get_is_one():
            super().set_is_on(True)
            print("Грузовик заведен")
        else:
            print("Грузовик уже заведен")

    def turn_off(self):
        if super().get_is_one():
            super().set_is_on(False)
            print("Грузовик заглушен")
        else:
            print("Грузовик уже заглушен")
