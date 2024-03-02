from src.vacancies import CompareVacancies


class UserInteraction(CompareVacancies):
    def __init__(self, name_vacancy):
        super().__init__(name_vacancy)
        self.get_vacancy_from_api()
        self.message = "Error"

    def __str__(self):
        self.message = "Vacancy not found" if len(self.all_vacancy) == 0 else self.message
        return (f"Name of vacancy for search: {self.name_vacancy}\n"
                f"Count vacancies: {len(self.all_vacancy)}\n")

    def make_info(self, top_salary: dict):
        """
        заполняет список вакансиями по запросу пользователя
        """
        print("Сортировка по з/п:")
        count = 1
        for item in top_salary:
            print(f"{count}, {item}")
            count += 1
        return self.vacancies_list

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
