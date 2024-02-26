from collections import defaultdict
from src.vacancies import CompareVacancies


class UserInteraction(CompareVacancies):
    def __init__(self, name_vacancy):
        super().__init__(name_vacancy)
        self.get_vacancy_from_api()
        self.vacancies_list = defaultdict(list)
        self.message = "Error"

    def __str__(self):
        self.message = "Vacancy not found" if len(self.all_vacancy) == 0 else self.message
        return (f"Name of vacancy for search: {self.name_vacancy}\n"
                f"Count vacancies: {len(self.all_vacancy)}\n")

    def make_info(self, top_salary: dict):
        """
        заполняет список вакансиями по запросу пользователя
        """
        print("Зп от большего к меньшему:")

        count = 1
        for top, vacancies in top_salary.items():

            print(f"{count}. Зарплата: {top} - число вакансий {len(vacancies)}", end='\n')

            for value in vacancies:
                self.vacancies_list[count].extend([{"Вакансия": value['name']},
                                                   {"Зп от": value['salary']['from']},
                                                   {"Зп до": value['salary']['to']},
                                                   {"Город": value['area']['name']},
                                                   {"URL": f"{value['alternate_url']}\n"}])
            count += 1

    @staticmethod
    def last_info(top_salary: dict, number_of_vacancies: int):
        """
        Выводит информацию о топе вакансий
        """
        info = []
        for params_vacancy in top_salary[int(number_of_vacancies)]:
            for key, val in params_vacancy.items():
                info.append("{0}: {1}".format(key, val))
        return '\n'.join(info)
