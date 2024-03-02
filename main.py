from src.user_vacancy import UserInteraction


def main():
    print('Платформа поиска = "HeadHunter"')
    user_input = input("Введите вакансию для поиска: ")
    user = UserInteraction(user_input)
    user.save_info()

    if len(user.vacancies_list) != 0:
        while True:
            users_salary = input("Минимальное значение зп: ")
            if users_salary.isdigit():
                break
            else:
                print("\nВведите зарплату цифрами. Пример: 100000\n")
        user.get_top_vacancies()
        user.sorted_salary()
        #user.get_top_vacancies()
        user.make_info(user.sort_salary)

        number_vacancy = input("Введите номер строки\n"
                               "Чтобы открыть более подробную инфомацию по вакансиям : ")
        if int(number_vacancy) <= len(user.get_top_vacancies()) and int(number_vacancy) != 0:
            print(user.last_info(user.top_salary))
            user.save_request()

        else:
            print("Error: Неверный выбор строки")

    else:
        print("Error: Ненайдено такой вакансии")


if __name__ == '__main__':
    main()
