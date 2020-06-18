import unittest

from app import create_app


class AbstractViewUnitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app()
        self.client = self.app.test_client()