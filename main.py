from src.user_vacancy import UserInteraction


def main():
    print('Платформа поиска = "HeadHunter"')
    user_input = input("Введите вакансию для поиска: ")

    while True:
        users_salary = input("Минимальное значение зп: ")
        if users_salary.isdigit():
            break
        else:
            print("\nВведите количество вакансий для вывода в топ N или 'Enter...\n")

    user = UserInteraction(user_input)
    user.sorted_salary(user.all_vacancy, int(users_salary))
    user.get_top_vacancies(user.sort_salary)

    user.make_info(user.top_salary)

    while True:
        number_vacancy = input("Введите номер строки\n"
                               "Чтобы открыть более подробную инфомацию: ")
        if number_vacancy.isdigit():
            break

    print(user.last_info(user.vacancies_list, number_vacancy))


if __name__ == '__main__':
    main()
