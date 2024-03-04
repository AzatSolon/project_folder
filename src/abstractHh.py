from abc import ABC, abstractmethod


class AbstractSaver(ABC):

    @abstractmethod
    def save(self, data):
        raise NotImplementedError

    @abstractmethod
    def load_all(self, source):
        raise NotImplementedError

    @abstractmethod
    def get_vacancy(self, vacancy):
        raise NotImplementedError

    @abstractmethod
    def delete_vacancy(self, vacancy):
        raise NotImplementedError


class AbstractHh(ABC):

    @abstractmethod
    def get_vacancy_from_api(self):
        pass

