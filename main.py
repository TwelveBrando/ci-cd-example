from new import Car
from gruzovik import Gruzovik
new_car = Car("green", 110, 13, "Mark II")
new_car.turn_off()
new_car.turn_on()
new_car.set_is_on(True)
print(new_car.get_is_one())
new_gruzovik = Gruzovik('Black', 100, 15, 'MAN', 500)
new_gruzovik.turn_on()
new_gruzovik.pick_up(1000)
new_gruzovik.pick_up(400)
new_gruzovik.pick_off()
new_gruzovik.turn_off()
