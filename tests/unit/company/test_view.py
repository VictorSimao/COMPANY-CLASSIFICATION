from unittest.mock import patch

from tests.unit import AbstractViewUnitTest


class TestView(AbstractViewUnitTest):

    @patch('app.company.view.get_all_company')
    def test_get_all_must_return_a_list_with_company(self, mock_get_all):
        mock_get_all.return_value = (1, 'teste', 1, 1, 50)

        return_get_all = self.client.get('/company')
        return_expected = [1, 'teste', 1, 1, 50]

        self.assertEqual(return_get_all.json, return_expected)
        self.assertEqual(return_get_all.status_code, 200)

    @patch('app.company.view.get_company_by_id')
    def test_get_by_id_should_be_1(self, mock_get_by_id):
        mock_get_by_id.return_value = (1, 'teste', 1, 1, 50)

        id = '1'

        return_get_one = self.client.get(f'/company/{id}')
        return_expected = [1, 'teste', 1, 1, 50]

        self.assertEqual(return_get_one.json, return_expected)
        self.assertEqual(return_get_one.status_code, 200)
