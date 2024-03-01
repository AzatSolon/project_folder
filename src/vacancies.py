from typing import Any
import json

from src.get_vacancies import GetVacancies


class CompareVacancies(GetVacancies):
    def __init__(self, name_vacancy: str):
        super().__init__(name_vacancy)
        self.sort_salary = []
        self.top_salary = []

    def sorted_salary(self, salary: int) -> list[Any]:
        """
           Генерируйт словарь с необходимой зарплатой и списком вакансий
        """

        for vacancy in self.vacancies_list:
            if vacancy["salary_from"] is not None and vacancy["salary_to"] is not None:
                if vacancy["salary_from"] >= int(salary):
                    self.sort_salary.append(vacancy)
        return self.sort_salary

    def get_top_vacancies(self) -> str | list[Any]:
        """
        Возвращает список топ вакансий по зп от max k min
        """

        for vacancy in self.sort_salary:
            if vacancy["salary_from"] is not None and vacancy["salary_to"] is not None:
                self.top_salary.append(vacancy)

        if int(len(self.top_salary)) < 1:
            message = "Vacancy not found"
            return message
        else:
            return self.top_salary

    def save_request(self):
        if len(self.top_salary) == 0:
            print('Вакансия не найдена\nПопробуйте снова')
        else:
            with open('user_request.json', 'w', encoding='utf-8') as file:
                return file.write(json.dumps(self.top_salary, indent=2, ensure_ascii=False))
