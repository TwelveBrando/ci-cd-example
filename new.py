class Car:
    def __init__(self, color, max_velocity, weight, mark):
        self.color = color
        self.max_velocity = max_velocity
        self.weight = weight
        self.mark = mark
        self.__is_on = False

    def get_is_one(self):
        return self.__is_on

    def set_is_on(self, new_is_on):
        self.__is_on = new_is_on
        print("Статус is_on изменен")

    def turn_on(self):
        if not self.__is_on:
            self.__is_on = True
            print("Машина заведена")
        else:
            print("Машина уже заведена")

    def turn_off(self):
        if self.__is_on:
            self.__is_on = False
            print("Машина заглушена")
        else:
            print("Машина уже заглушена")