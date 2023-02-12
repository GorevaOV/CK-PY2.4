class Tank:
    def __init__(self, capacity: (int, float), volume: (int, float)):
        """
        Создание базового класса "Танкер"
        :param capacity: Вместимость танкера
        :param volume: Занятый объем танкера
        """
        self._capacity = None  # protected: Вместимость танкера не может меняться
        self._init_capacity(capacity)
        self._volume = None  # protected: константа для танкера после загрузки
        self._init_volume(volume)

    def __str__(self) -> str:
        return f"Танкер: Максимальная вместимость {self.capacity} (м3), занятый объем {self.volume} (м3)."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(capacity={self.capacity},volume={self.volume})"

    def _init_capacity(self, capacity: (int, float)) -> None:
        """
        Инициализация атрибута _capacity:
        Protected: используется только при инициализации экземпляра класса
        :param capacity: Вместимость для определенной модели танкера
        """
        if not isinstance(capacity, (int, float)):
            raise TypeError('Вместимость танкра должна быть типа int или float')
        if capacity < 0:
            raise ValueError('Вместимость танкера должна быть не меньше 0')
        self._capacity = capacity

    def _init_volume(self, volume: (int, float)) -> None:
        """
        Инициализация атрибута _volume:
        Protected: используется только при инициализации экземпляра класса
        :param volume: Занятый объем данного типа танкера
        """
        if not isinstance(volume, (int, float)):
            raise TypeError('Занятый объем должнен быть типа int или float')
        if volume <= 0:
            raise ValueError('Занятый объем должен быть больше 0')
        self._volume = volume

    @property
    def capacity(self) -> (int, float):
        """
        Используем getter для атрибута _capacity (не setter: protected атрибут)
        """
        return self._capacity

    @property
    def volume(self) -> (int, float):
        """
        Используем getter для атрибута _volume (не setter: protected атрибут)
        """
        return self._volume

    def fill_fuel(self, added_fuel: (int, float)) -> None:
        """
        Дозаправка - увеличить занятый объем танкера
        :param added_fuel: объем добавляемого содержимого
        """
        if not isinstance(added_fuel, (int, float)):
            raise TypeError('Объем добавляемого содержимого должен быть типа int или float')
        if added_fuel < 0:
            raise ValueError('Объем добавляемого содержимого должен быть не меньше 0')
        self._volume += added_fuel

    def lost_fuel(self, route_time: (int, float)) -> None:
        """
        Во время перевозки возможна потеря определенного количества содержимого, которая зависит от времени в пути
        :param route_time: Время в пути
        """
        if not isinstance(route_time, (int, float)):
            raise TypeError('Время в пути должно быть типа int или float')
        if route_time < 0:
            raise ValueError('Время в пути должно быть не меньше 0')
        ...


class GasTank(Tank):
    def __init__(self, capacity: (int, float), volume: (int, float), gas_type: str):
        """
        Создание дочернего класса "Газовый танкер", унаследован от класса "Танкер"
        :param capacity: Вместимость газового танкера
        :param volume: Занятый объем танкера
        :param gas_type: Тип перевозимого топлива
        """
        super().__init__(capacity, volume)
        self._gas_type = None  # protected: константа для конкретного танкера
        self._init_gas_type(gas_type)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(tank_capacity={self.capacity},tank_volume={self.volume}," \
               f"type={self._gas_type})"

    def _init_gas_type(self, gas_type: str) -> None:
        """
        Инициализация атрибута _gas_type - Перевозимый тип топлива
        Protected: используется только при инициализации экземпляра класса
        :param gas_type: Тип топлива первозимого танкером
        """
        if not isinstance(gas_type, str):
            raise TypeError('Тип содержимого газа может быть только str ')

        self._gas_type = gas_type

    @property
    def type(self) -> str:
        """
        Используем getter для атрибута _gas_type (не setter: protected атрибут)
        """
        return self._gas_type

    def lost_fuel(self, route_time: (int, float)) -> None:
        """
        Во время перевозки возможна потеря определенного количества содержимого, которая зависит от времени в пути
        Перегрузка метода базового класса ввиду того, что потеря газа при перевозке может отличается у разных видов топлива
        :param route_time: время в пути
        """
        if not isinstance(route_time, (int, float)):
            raise TypeError('Время в пути должно быть типа int или float')
        if route_time < 0:
            raise ValueError('Время в пути должно быть не меньше 0')
        ...


if __name__ == "__main__":
    # Write your solution here
    pass
