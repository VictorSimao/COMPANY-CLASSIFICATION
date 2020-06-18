from unittest import TestCase
from unittest.mock import patch, Mock, MagicMock, mock_open

from app.company.action import db, get_all, get_by_id, update, update_score, update_log, \
    function_for_ranking


class TestAction(TestCase):
    @patch('app.company.action.function_for_ranking')
    @patch('app.company.action.db.cursor')
    def test_action_get_must_must_return_company(self, mock_cursor, mock_function_for_ranking):
        mock_cursor.fetchall.return_value = [[1, "Teste", 1, 1, 1]]
        mock_function_for_ranking.return_value = 1

        return_get_all = get_all()

        db.cursor.fetchall.assert_called_once()
        self.assertEqual(len(return_get_all), 1)
        self.assertEqual(return_get_all[0][0], 1)
        self.assertEqual(return_get_all[0][1], 'Teste')
        self.assertEqual(return_get_all[0][2], 1)
        self.assertEqual(return_get_all[0][3], 1)
        self.assertEqual(return_get_all[0][4], 1)

    @patch('app.company.action.db.cursor')
    def test_action_get_by_id_must_return_company(self, mock_cursor):
        mock_cursor.fetchone.return_value = [1, "Teste", 1, 1, 1]

        company = get_by_id(1)

        db.cursor.fetchone.assert_called_once()
        self.assertEqual(company[0], 1)
        self.assertEqual(company[1], 'Teste')
        self.assertEqual(company[2], 1)
        self.assertEqual(company[3], 1)
        self.assertEqual(company[4], 1)

    @patch('app.company.action.db.cursor')
    @patch('app.company.action.update_log')
    @patch('app.company.action.update_score')
    @patch('app.company.action.os')
    @patch('app.company.action.get_by_id')
    def test_action_update_must_return_tuple(self, mock_get_by_id, mock_os, mock_update_score, mock_update_log,
                                               mock_cursor):
        with patch("builtins.open", mock_open(read_data="1;Empresa;10;0")) as mock_file:
            mock_get_by_id.return_value = [1, "Teste", 1, 1, 1]
            mock_open.return_value={'id': 1, 'name': 'Teste', 'invoice': 1, 'debit': 1, 'score': 1}
            mock_update_score.return_value = 100

            return_update = update(1, mock_file)

            self.assertEqual(return_update, ('Atualização feita com sucesso', 201))


    def test_action_update_score_must_return_score(self):
        return_value = update_score(1, 0)

        self.assertEqual(return_value, 51)

    def test_action_function_for_ranking_must_return_int(self):
        company = [0, 0, 0, 0, 100]

        return_value = function_for_ranking(company)

        self.assertEqual(return_value, 100)
