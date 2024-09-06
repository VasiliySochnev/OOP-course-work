import unittest
from unittest.mock import patch
from src.get_data_api import HeadHunterAPI


class TestHeadHunterAPI(unittest.TestCase):
    @patch('src.get_data_api.requests.get')
    def test_get_vacans_short(self, mock_get):
        # Задаем фейковые данные, которые вернет запрос к API
        mock_response = {
            "items": [
                {
                    "id": "12345",
                    "name": "Python Developer",
                    "area": {"name": "Москва"},
                    "salary": {"from": 100000, "to": 150000},
                    "url": "http://example.com/python-developer",
                    "snippet": {
                        "requirement": "Опыт работы с Python",
                        "responsibility": "Разработка и поддержка кода",
                    },
                }
            ]
        }

        # Настраиваем mock для requests.get
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        # Создаем экземпляр класса и вызываем метод
        hh_api = HeadHunterAPI("Python Developer")
        vacancies = hh_api.get_vacans_short()

        # Проверяем результат
        expected_result = [
            {
                "id": 12345,
                "name": "Python Developer",
                "city": "Москва",
                "salary_from": 100000,
                "salary_to": 150000,
                "url": "http://example.com/python-developer",
                "requirement": "Опыт работы с Python",
                "responsibility": "Разработка и поддержка кода",
            }
        ]

        self.assertEqual(vacancies, expected_result)


if __name__ == "__main__":
    unittest.main()
