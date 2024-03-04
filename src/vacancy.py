class Vacancy:

    def __init__(self, title: str, url: str, salary_from: int, salary_to: int, area: str):
        self.title = title
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.area = area

    def __str__(self):
        return f"{self.title}\n{self.salary_from} {self.salary_to}\n{self.url}\n{self.area}."

    def __ge__(self, other):
        if self.salary_from and other.salary_from is not None:
            return self.salary_from >= other.salary_from

    def __lt__(self, other):
        if self.salary_from and other.salary_from is not None:
            return self.salary_from < other.salary_from
