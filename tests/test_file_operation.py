import unittest
from unittest.mock import patch, mock_open
from src.file_operation import FileOperation


class TestFileOperation(unittest.TestCase):

    @patch('src.file_operation.FileOperation.load_file', return_value=[
        {"id": 1, "name": "Developer"},
        {"id": 2, "name": "Designer"},
        {"id": 3, "name": "Manager"}
    ])
    @patch('src.file_operation.FileOperation.write_file')
    def test_delete_by_id(self, mock_write_file, mock_load_file):

        file_op = FileOperation(filename="test_file")

        ids_to_delete = [1, 3]

        file_op.delete_by_id(id_list=ids_to_delete)

        mock_load_file.assert_called_once()

        expected_data = [{"id": 2, "name": "Designer"}]
        mock_write_file.assert_called_once_with(expected_data)
