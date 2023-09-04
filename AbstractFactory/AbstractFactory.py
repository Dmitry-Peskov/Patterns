from abc import ABCMeta, abstractmethod


class IProcessor(metaclass=ABCMeta):
    @abstractmethod
    def release(self):
        pass


class ISmartphone(metaclass=ABCMeta):
    @abstractmethod
    def create(self, processor: IProcessor):
        pass


class IFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_processor(self) -> IProcessor:
        pass

    @abstractmethod
    def create_smartphone(self) -> ISmartphone:
        pass


class ProcessorIOS(IProcessor):
    def release(self):
        print('Процессор под IOS', end=' ')


class ProcessorAndroid(IProcessor):
    def release(self):
        print('Процессор под Android', end=' ')


class AndroidPhone(ISmartphone):
    def create(self, processor: IProcessor):
        processor.release()
        print('Собрали смартфон на Android')


class IOSPhone(ISmartphone):
    def create(self, processor: IProcessor):
        processor.release()
        print('Собрали смартфон на IOS')


class AndroidFactory(IFactory):
    def create_processor(self) -> IProcessor:
        return ProcessorAndroid()

    def create_smartphone(self) -> ISmartphone:
        return AndroidPhone()


class IOSFactory(IFactory):
    def create_processor(self) -> IProcessor:
        return ProcessorIOS()

    def create_smartphone(self) -> ISmartphone:
        return IOSPhone()


if __name__ == "__main__":
    factory = IOSFactory()
    processor = factory.create_processor()
    phone = factory.create_smartphone()

    phone.create(processor)

    factory = AndroidFactory()
    processor = factory.create_processor()
    phone = factory.create_smartphone()

    phone.create(processor)
