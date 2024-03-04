import json
from abc import ABC
from typing import Any

import requests

from src.abstractHh import AbstractHh


class GetVacancies(AbstractHh, ABC):
    """
    Класс для рабооты с https://api.hh.ru/vacancies и получения файла формата json
    """

    def __init__(self, name_vacancy: str):
        self.name_vacancy: str = name_vacancy
        self.all_vacancy = self.get_vacancy_from_api()
        self.vacancy_list = self.get_format_vacancies()

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

    def get_format_vacancies(self):
        """
        Преобразует результат запроса  по полям title, url, salary_from, salary_to, area
        """
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

    @staticmethod
    def last_info(top_salary: dict):
        """
        Выводит информацию о топе вакансий
        """
        info = []
        for params_vacancy in top_salary:
            if params_vacancy["salary_from"] is not None and params_vacancy["salary_to"] is not None:
                info.append("Вакансия: {0} зарплата от: {1}, зарплата до:{2}. Город: {3}, url:{4}".format(
                    params_vacancy['title'],
                    params_vacancy['salary_from'],
                    params_vacancy['salary_to'],
                    params_vacancy['area'],
                    params_vacancy['url']))
        return '\n'.join(info)
