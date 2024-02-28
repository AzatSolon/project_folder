import json
from typing import Any

import requests

from src.abstractHh import AbstractHh


class GetVacancies(AbstractHh):
    """
    Класс для рабооты с https://api.hh.ru/vacancies и получения файла формата json
    """

    def __init__(self, name_vacancy: str):
        self.name_vacancy: str = name_vacancy
        self.all_vacancy = self.get_vacancy_from_api()
        self.vacancy = self.save_info()[0]['name']
        self.url = self.save_info()[0]['url']
        self.area = self.save_info()[0]['area']['name']
        self.salary = self.save_info()[0]['salary']
        self.data = self.vacancy, self.url, self.area, self.salary

    def __str__(self):
        return f"{self.data}"

    def __repr__(self):
        return f"{self.all_vacancy}"

    def get_vacancy_from_api(self) -> str | Any:
        """
        Отправляет запрос на https://api.hh.ru/vacancies с поиском по выбранной вакансии
        """

        if isinstance(self.name_vacancy, str):
            keys_response = {'text': f'NAME:{self.name_vacancy}', 'area': None, 'per_page': 100, }
            info = requests.get(f'https://api.hh.ru/vacancies', keys_response)
            return json.loads(info.text)['items']
        else:
            print('Вакансия не найдена\nПопробуйте снова')

    def save_info(self) -> str or list:
        """Создает и заполняпет json фаил вакансиями"""

        if len(self.all_vacancy) == 0:
            print('Вакансия не найдена\nПопробуйте снова')
        else:
            with open('folder.json', 'w', encoding='utf-8') as file:
                file.write(json.dumps(self.all_vacancy, ensure_ascii=False))
            return self.all_vacancy


#print(GetVacancies("python").__str__())
