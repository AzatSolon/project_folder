from src.Json_saver import JsonSaver
from src.vacancies import CompareVacancies


def main():
    print('Платформа поиска = "HeadHunter"')
    user_input = input("Введите вакансию для поиска: ")
    vacancies = CompareVacancies(user_input)
    json_connector = JsonSaver()
    json_vacancy = json_connector.save(vacancies.vacancy_list)

    if len(json_vacancy) != 0:
        users_salary = input("Минимальное значение зп: ")
        while True:
            if users_salary.isdigit():
                break
            else:
                print("Введите зарплату цифрами. Пример: 100000\n")

        vacancies_top_list = vacancies.sorted_salary(json_vacancy, users_salary)
        print(f"Найдено: {len(vacancies_top_list)} вакансий.")
        print(vacancies.last_info(vacancies_top_list))
        users_save = input("Хотите сохранить результат поиска в json фаил: да/нет?\n")
        if "да" in users_save.lower():
            vacancies.save_request()
        else:
            print("Досвидания, приходите еще ...")

    else:
        print("Error: Ненайдено такой вакансии")


if __name__ == '__main__':
    main()
