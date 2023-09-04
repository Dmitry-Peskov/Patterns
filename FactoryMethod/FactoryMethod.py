from abc import ABC, abstractmethod


class IProduct(ABC):
    @abstractmethod
    def release(self):
        pass


class IFactory(ABC):
    @abstractmethod
    def create(self) -> IProduct:
        pass


class Car(IProduct):
    def release(self):
        print('Создан автомобиль')


class Truck(IProduct):
    def release(self):
        print('Создан грузовик')


class CarFactory(IFactory):
    def create(self) -> IProduct:
        return Car()


class TruckFactory(IFactory):
    def create(self) -> IProduct:
        return Truck()


if __name__ == "__main__":
    creator = CarFactory()
    car = creator.create()

    creator = TruckFactory()
    truck = creator.create()

    car.release()
    truck.release()
