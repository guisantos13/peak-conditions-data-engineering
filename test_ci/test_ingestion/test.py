import unittest
from ingestion_data.base_peak_condition import api_requests


class TestRequestGet(unittest.TestCase):
    def test_api(self):
        request = api_requests("https://peak-conditions.p.rapidapi.com/search")
        print(request)
        assert request == "Success" or request == 400