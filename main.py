from src.user_vacancy import UserInteraction


def main():
    print('Платформа поиска = "HeadHunter"')
    user_input = input("Введите вакансию для поиска: ")
    user = UserInteraction(user_input)

    if len(user.all_vacancy) != 0:
        while True:
            users_salary = input("Минимальное значение зп: ")
            if users_salary.isdigit():
                break
            else:
                print("\nВведите зарплату цифрами. Пример: 100000\n")
        user.sorted_salary(user.all_vacancy, int(users_salary))
        user.get_top_vacancies(user.sort_salary)
        user.make_info(user.top_salary)
        user.save_info()

        number_vacancy = input("Введите номер строки\n"
                               "Чтобы открыть более подробную инфомацию по вакансиям : ")
        if int(number_vacancy) <= len(user.vacancies_list) and int(number_vacancy) != 0:
            print(user.last_info(user.vacancies_list, int(number_vacancy)))

        else:
            print("Error: Неверный выбор строки")

    else:
        print("Error: Ненайдено такой вакансии")


if __name__ == '__main__':
    main()
