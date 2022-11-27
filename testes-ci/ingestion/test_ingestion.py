from unittest import TestCase
from ingestion_data.ingestion_data_peak_condition import *

class TestIngestion(TestCase):
    def test_ingestion(self):
        self.assertEqual(soma(2, 2), 4)
    