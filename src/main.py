from pprint import pprint

from src.get_vacancies import GetVacancies

def user_interaction():
    print("HeadHunter")
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    #filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    #salary_range = input("Введите диапазон зарплат: ")  # Пример: 100000 - 150000
    GetVacancies()


if __name__ == "__main__":
    user_interaction()
