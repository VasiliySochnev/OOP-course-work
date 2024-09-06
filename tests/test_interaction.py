import pytest
from unittest.mock import patch
from src.vacancy import Vacancy
from src.interaction import select_top_vac_from_salary

@pytest.fixture
def mock_vacancies():
    """Фикстура для тестовых данных: список объектов вакансий"""
    return [
        Vacancy(
            id=1,
            name='Python Developer',
            city='New York',
            salary_from=50000,
            salary_to=70000,
            url='http://example.com/python-developer',
            requirement='Experience with Python',
            responsibility='Develop software',
        ),
        Vacancy(
            id=2,
            name='Data Scientist',
            city='San Francisco',
            salary_from=60000,
            salary_to=90000,
            url='http://example.com/data-scientist',
            requirement='Experience with Data Analysis',
            responsibility='Analyze data',
        ),
        Vacancy(
            id=3,
            name='Junior Developer',
            city='Los Angeles',
            salary_from=30000,
            salary_to=50000,
            url='http://example.com/junior-developer',
            requirement='Basic knowledge of Python',
            responsibility='Assist in software development',
        )
    ]

@pytest.fixture(autouse=True)
def clear_vacancy_list():
    """Автоматическая фикстура для очистки списка вакансий после каждого теста"""
    yield
    Vacancy.vac_list.clear()

@patch('builtins.input', return_value="2")
@patch('src.vacancy.Vacancy.vacancies_sort_salary', return_value=[
    Vacancy(
        id=2,
        name='Data Scientist',
        city='San Francisco',
        salary_from=60000,
        salary_to=90000,
        url='http://example.com/data-scientist',
        requirement='Experience with Data Analysis',
        responsibility='Analyze data',
    ),
    Vacancy(
        id=1,
        name='Python Developer',
        city='New York',
        salary_from=50000,
        salary_to=70000,
        url='http://example.com/python-developer',
        requirement='Experience with Python',
        responsibility='Develop software',
    ),
    Vacancy(
        id=3,
        name='Junior Developer',
        city='Los Angeles',
        salary_from=30000,
        salary_to=50000,
        url='http://example.com/junior-developer',
        requirement='Basic knowledge of Python',
        responsibility='Assist in software development',
    ),
])
def test_select_top_vac_from_salary(mock_sort, mock_input, mock_vacancies):
    """
    Тест функции select_top_vac_from_salary,
    которая выбирает топ вакансий по зарплате.
    """
    count_vac = len(mock_vacancies)

    # Ожидаемый результат: топ-2 вакансии с самой высокой зарплатой
    expected_output = [
        Vacancy(
            id=2,
            name='Data Scientist',
            city='San Francisco',
            salary_from=60000,
            salary_to=90000,
            url='http://example.com/data-scientist',
            requirement='Experience with Data Analysis',
            responsibility='Analyze data',
        ),
        Vacancy(
            id=1,
            name='Python Developer',
            city='New York',
            salary_from=50000,
            salary_to=70000,
            url='http://example.com/python-developer',
            requirement='Experience with Python',
            responsibility='Develop software',
        ),
    ]

    # Вызов функции
    result = select_top_vac_from_salary(count_vac)

    # Проверка результата
    assert result == expected_output


@patch('builtins.input', return_value="")
@patch('src.vacancy.Vacancy.vacancies_sort_salary', return_value=[
    Vacancy(
        id=2,
        name='Data Scientist',
        city='San Francisco',
        salary_from=60000,
        salary_to=90000,
        url='http://example.com/data-scientist',
        requirement='Experience with Data Analysis',
        responsibility='Analyze data',
    ),
    Vacancy(
        id=1,
        name='Python Developer',
        city='New York',
        salary_from=50000,
        salary_to=70000,
        url='http://example.com/python-developer',
        requirement='Experience with Python',
        responsibility='Develop software',
    ),
    Vacancy(
        id=3,
        name='Junior Developer',
        city='Los Angeles',
        salary_from=30000,
        salary_to=50000,
        url='http://example.com/junior-developer',
        requirement='Basic knowledge of Python',
        responsibility='Assist in software development',
    ),
])
def test_select_top_vac_from_salary_empty_input(mock_sort, mock_input, mock_vacancies):
    """
    Тест функции select_top_vac_from_salary, когда пользователь не вводит количество вакансий.
    """
    count_vac = len(mock_vacancies)

    # Ожидаемый результат: все вакансии будут возвращены
    expected_output = [
        Vacancy(
            id=2,
            name='Data Scientist',
            city='San Francisco',
            salary_from=60000,
            salary_to=90000,
            url='http://example.com/data-scientist',
            requirement='Experience with Data Analysis',
            responsibility='Analyze data',
        ),
        Vacancy(
            id=1,
            name='Python Developer',
            city='New York',
            salary_from=50000,
            salary_to=70000,
            url='http://example.com/python-developer',
            requirement='Experience with Python',
            responsibility='Develop software',
        ),
        Vacancy(
            id=3,
            name='Junior Developer',
            city='Los Angeles',
            salary_from=30000,
            salary_to=50000,
            url='http://example.com/junior-developer',
            requirement='Basic knowledge of Python',
            responsibility='Assist in software development',
        ),
    ]

    # Вызов функции
    result = select_top_vac_from_salary(count_vac)

    # Проверка результата
    assert result == expected_output

