from unittest import TestCase

from app.company.model import CompanyModel


class TestCompanyModel(TestCase):
    def test_return_company_str(self):
        company = CompanyModel(1, 'Teste', 0, 0, 50)

        return_company = company.__str__()
        return_expected = {'id': 1, 'name': 'Teste', 'invoice': 0, 'debit': 0, 'score': 50}

        self.assertIsInstance(company, CompanyModel)
        self.assertEqual(return_company, return_expected)
