from abc import ABC, abstractmethod
from builtins import list


class VacansABS(ABC):
    """Абстрактный (родительский) класс для работы с вакансиями."""

    @abstractmethod
    def __init__(self):
        """Инициализация."""
        pass

    @abstractmethod
    def __str__(self):
        """Метод для получение строковых значений."""
        pass


class Vacancy(VacansABS):
    """Дочерний класс для работы с вакансиями."""

    vac_list: list = []

    def __init__(
        self,
        id: int,
        name: str,
        city: str,
        salary_from: int,
        salary_to: int,
        url: str,
        requirement: str,
        responsibility: str,
    ):
        self.id = id
        self.name = name
        self.city = city
        self.salary_from = self._validate_salary(salary_from)
        self.salary_to = self._validate_salary(salary_to)
        self.url = url
        self.requirement = requirement
        self.responsibility = responsibility
        Vacancy.vac_list.append(self)

    def _validate_salary(self, salary):
        """Приватный метод для валидации зарплаты."""

        if salary is None:
            return 0
        if not isinstance(salary, int) or salary < 0:
            raise ValueError("Зарплата должна быть положительным целым числом")
        return salary

    def __eq__(self, other):
        """Метод для сравнения объектов. Это позволяет сравнивать списки объектов Vacancy в тестах."""

        if not isinstance(other, Vacancy):
            return False
        return (
                self.id == other.id
                and self.name == other.name
                and self.city == other.city
                and self.salary_from == other.salary_from
                and self.salary_to == other.salary_to
                and self.url == other.url
                and self.requirement == other.requirement
                and self.responsibility == other.responsibility
        )

    def __str__(self):
        """Метод для получения строковых значений объектов класса."""
        return (
            f"{self.name}\n"
            f"Id: {self.id}\n"
            f"Город: {self.city}\n"
            f"Зарплата от: {self.salary_from if self.salary_from else "Не указана"} \n"
            f"Зарплата до: {self.salary_to if self.salary_to else "Не указана"} \n"
            f"Ссылка: {self.url}\n"
            f"Требования: {self.requirement}\n"
            f"Обязанности: {self.responsibility}\n"
        )

    def vac_obj_to_dict(self):
        """Метод для преобразования объекта вакансий в словарь."""

        dict_of_vac = {
            "id": self.id,
            "name": self.name,
            "city": self.city,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "url": self.url,
            "requirement": self.requirement,
            "responsibility": self.responsibility,
        }
        return dict_of_vac

    @classmethod
    def vacancies_sort_salary(cls) -> list:
        """
        Класс - метод, который сортирует вакансии по зарплате и
        возвращает отфильтрованный список экземпляров класса по убыванию зарплаты.
        """

        cls.vac_list.sort(reverse=True)
        return cls.vac_list

    @classmethod
    def vacancies_filtered_city(cls, city) -> list:
        """
        Класс - метод, который сортирует вакансии по городам
        и возвращает список вакансий с нужным городом.
        """

        filter_city: list = []
        for item in cls.vac_list:
            if item.city == city:
                filter_city.append(item)
        return filter_city

    @classmethod
    def filter_vacancies(cls, vacancies_list: list, filter_words: list) -> list:
        """Класс - метод для фильтрации вакансий по ключевым словам."""

        filtered_list = []
        for vacancy in vacancies_list:
            for word in filter_words:
                if word.lower() in vacancy.requirement.lower().split():
                    filtered_list.append(vacancy)

        if len(filtered_list) == 0:
            print(*filter_words)
            print("Вакансий с такими критериями не найдено")
        return filtered_list

    def range_from_salary(self, salary_from, salary_to) -> bool:  # type: ignore
        """Метод проверки объекта - вакансии перекрытия зарплатной вилки
        salary_from: int - зарплата "ОТ"
        salary_to: int - зарплата "ДО"
        возвращает bool.
        """
        if isinstance(salary_from, int) is True and isinstance(salary_to, int) is True:
            if self.salary_from >= salary_from and self.salary_to >= salary_to:
                return True
            else:
                return False
                # return self

    def __lt__(self, other):
        """Метод для сравнения вакансий между собой."""

        if isinstance(other, Vacancy) is True:
            return self.salary_from < other.salary_from
        raise TypeError("сравнению подлежат элементы класса Vacancy")
