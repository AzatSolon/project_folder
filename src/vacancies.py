from typing import Any

from src.get_vacancies import GetVacancies
from collections import defaultdict


class CompareVacancies(GetVacancies):
    def __init__(self, name_vacancy: str):
        super().__init__(name_vacancy)
        self.sort_salary: dict = defaultdict(list)
        self.top_salary: dict = defaultdict(list)

    def sorted_salary(self, list_all: list, salary: int) -> dict:
        """
           Генерируйт словарь с необходимой зарплатой и списком вакансий
        """

        for vacancy in list_all:
            if vacancy["salary"] is not None and vacancy["salary"]["from"] is not None:
                if vacancy["salary"]['from'] >= salary and vacancy["salary"]['from'] is not None:
                    self.sort_salary[vacancy["salary"]['from']].append(vacancy)
        return self.sort_salary

    def get_top_vacancies(self, sort_salary) -> str | dict[Any, Any]:
        """
        Возвращает список топ вакансий по зп от max k min
        """

        for top, vacancy in sort_salary.items():
            for value in vacancy:
                if value["salary"] is not None and value["salary"]["to"] is not None:
                    self.top_salary[value["salary"]["to"]].extend(vacancy)

        self.top_salary = dict(sorted(self.top_salary.items(), reverse=True))

        if len(self.top_salary) < 1:
            message = "Vacancy not found"
            return message

        return self.top_salary
