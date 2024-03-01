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
        self.vacancies_list = self.get_format_vacancies()

    def __str__(self):
        return f""

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

        if len(self.vacancies_list) == 0:
            print('Вакансия не найдена\nПопробуйте снова')
        else:
            with open('folder.json', 'w', encoding='utf-8') as file:
                file.write(json.dumps(self.vacancies_list, indent=2, ensure_ascii=False))
            return self.vacancies_list

    def get_format_vacancies(self):
        formatted_vacancies = []
        for vacancy in self.all_vacancy:
            formatted_vacancy = {
                "title": vacancy["name"],
                "url": vacancy["url"],
                "salary_from": vacancy["salary"]["from"] if vacancy["salary"] else None,
                "salary_to": vacancy["salary"]["to"] if vacancy["salary"] else None,
                "area": vacancy["area"]["name"]
            }
            formatted_vacancies.append(formatted_vacancy)
        return formatted_vacancies
