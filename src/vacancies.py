from abc import ABC
import json

from src.get_vacancies import GetVacancies


class CompareVacancies(GetVacancies, ABC):
    def __init__(self, name_vacancy: str):
        super().__init__(name_vacancy)
        self.all_vacancy = self.get_vacancy_from_api()
        self.top_salary = []

    def sorted_salary(self, data, salary):
        """
           Генерируйт словарь со списком экземпляров класса вакансий
        """
        for vacancy in data:
            if vacancy['salary_from'] and vacancy['salary_to'] is not None:
                if vacancy['salary_from'] >= int(salary):
                    self.top_salary.append(vacancy)
        return sorted(self.top_salary, key=lambda x: x['salary_from'], reverse=True)

    def save_request(self):
        """
        Записывает результат поиска по вакансии и зп в фаил json
        """
        if len(self.top_salary) == 0:
            print('Вакансия не найдена\nПопробуйте снова')
        else:
            with open('user_request.json', 'w', encoding='utf-8') as file:
                return file.write(json.dumps(self.top_salary, indent=2, ensure_ascii=False))
