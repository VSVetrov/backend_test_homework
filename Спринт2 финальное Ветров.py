class InfoMessage:
    """Класс для создания объектов сообщения."""
    def __init__(self,
                 training_type: str,
                 duration: float,
                 distance: float,
                 speed: float,
                 calories: float) -> None:
        self.training_type = training_type
        self.distance = distance
        self.speed = speed
        self.calories = calories
        self.duration = duration

    def get_message(self) -> str:
        """Выводит итоги тренировки."""
        return (f'Тип тренировки: {self.training_type}; '
                f'Длительность: {self.duration} ч.; '
                f'Дистанция: {self.distance:.3f} км; '
                f'Ср. скорость: {self.speed:.3f} км/ч; '
                f'Потрачено ккал: {self.calories:.3f}.')


class Training:
    """Базоый класс для исходных данных тренировки."""
    def __init__(self, action: int, duration: float, weight: float) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    LEN_STEP: float = 0.65
    M_IN_KM: int = 1000
    training_type = ''

    def get_distance(self) -> float:
        """Возвращает дистианцию, которую преодолел пользователь за время тренировки."""
        distance = self.action * self.LEN_STEP / self.M_IN_KM
        return distance

    def get_mean_speed(self) -> float:
        """Возвращает значение средней скорости."""
        speed: float = self.get_distance() / self.duration
        return speed

    def get_spent_calories(self) -> float:
        """Возвращает количество килокалорий, израсходованных за время тренировки."""
        pass

    def show_training_info(self):
        """Возвращает объект класса сообщения."""
        info_message = InfoMessage(self.training_type,
                                   self.duration,
                                   self.get_distance(),
                                   self.get_mean_speed(),
                                   self.get_spent_calories())
        return info_message


class Running(Training):
    """Расчет данных для Бега."""
    training_type = 'RUN'

    def __init__(self, action, duration, weight) -> None:
        super().__init__(action, duration, weight)

    def get_spent_calories(self) -> float:
        """Возвращает количество килокалорий, израсходованных за время тренировки."""
        calories = (18 * self.get_mean_speed() - 20) * self.weight / self.M_IN_KM * self.duration * 60
        return calories


class SportsWalking(Training):
    """Расчет данных для Спортивной ходьбы."""
    training_type = 'WLK'

    def __init__(self, action, duration, weight, height: float) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        """Возвращает количество килокалорий, израсходованных за время тренировки."""
        element = self.get_mean_speed() ** 2 // self.height * 0.029 * self.weight
        # переменная для промежуточных расчетов
        calories = (0.035 * self.weight) + element * self.duration * 60
        return calories


class Swimming(Training):
    """Расчет данных для Плавания."""
    LEN_STEP = 1.28
    training_type = "SWM"

    def __init__(self, action, duration, weight, length_pool: float, count_pool: float) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        speed = self.length_pool * self.count_pool / super().M_IN_KM / self.duration
        return speed

    def get_spent_calories(self) -> float:
        """Возвращает количество килокалорий, израсходованных за время тренировки."""
        calories = (self.get_mean_speed() + 1.1) * 2 * self.weight
        return calories


def read_package(workout_type: str, data: list) -> Training:
    """Функция чтения принятых пакетов."""
    type_dict = {'SWM': Swimming, 'RUN': Running, 'WLK': SportsWalking}  # переменная для вида тренировки
    return type_dict[workout_type](*data)


def main(training):
    """Функция для печати данных о тренировке."""
    info = training.show_training_info()
    print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
