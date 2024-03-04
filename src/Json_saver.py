import json

from src.abstractHh import AbstractSaver


class JsonSaver(AbstractSaver):
    def save(self, save):

        if len(save) == 0:
            print('Vacancy not found\nPlease repute')
        else:
            json.dumps(save, indent=2, ensure_ascii=False)
            return save

        # логика добавления вакансий в файл

    pass

    def load_all(self, source: str) -> list[dict]:
        # логика чтения файла и получения всех вакансий
        pass

    def get_vacancy(self, vacancy) -> dict:
        # логика получения вакансии из файла (например по названию или ID)
        # можно оставить pass, если не предполагается использовать
        pass

    def delete_vacancy(self, vacancy) -> None:
        # логика удаления вакансии из файла (например по названию или ID)
        # можно оставить pass, если не предполагается использовать
        pass
