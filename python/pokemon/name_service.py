import abc


class NameService(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def changeName(self, new_name):
        pass

    @abc.abstractmethod
    def getName(self):
        pass
