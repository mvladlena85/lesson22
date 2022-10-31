# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:

    def __init__(self, state, field, x_coord, y_coord, speed=1):
        self.state = state
        self.field = field
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.speed = speed

    def move(self, field, direction):
        speed = self._get_speed()

        if direction == 'UP':
            field.set_unit(x=self.x_coord, y=self.y_coord + speed, unit=self)
        elif direction == 'DOWN':
            field.set_unit(x=self.x_coord, y=self.y_coord - speed, unit=self)
        elif direction == 'LEFT':
            field.set_unit(x=self.x_coord - speed, y=self.y_coord, unit=self)
        elif direction == 'RIGHT':
            field.set_unit(x=self.x_coord + speed, y=self.y_coord, unit=self)

    def _get_speed(self):
        if self.state == 'fly':
            return 1.2 * self.speed
        elif self.state == 'crawl':
            return 0.5 * self.speed
        else:
            raise ValueError('Рожденный ползать летать не должен!')
