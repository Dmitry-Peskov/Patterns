from abc import ABC, abstractmethod


class IProduct(ABC):
    @abstractmethod
    def release(self):
        pass


class IFactory(ABC):
    @abstractmethod
    def create(self) -> IProduct:
        pass


class Apple(IProduct):
    def release(self):
        print('Произведено яблоко')


class Banana(IProduct):
    def release(self):
        print('Произведен банан')


class AppleFactory(IFactory):
    def create(self) -> IProduct:
        return Apple()


class BananaFactory(IFactory):
    def create(self) -> IProduct:
        return Banana()


if __name__ == "__main__":
    factory = AppleFactory()
    apple = factory.create()

    factory = BananaFactory()
    banana = factory.create()

    apple.release()
    banana.release()
