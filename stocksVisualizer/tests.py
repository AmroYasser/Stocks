from django.test import TestCase
from django.contrib.auth.models import User


class CompaniesTests(TestCase):
    def test_return_all_companies(self):
        User.objects.create_superuser('admin', 'foo@foo.com', 'admin')
        self.client.login(username='admin', password='admin')

        response = self.client.get('/')
        self.assertEquals(200, response.status_code)

    def test_return_error_incase_no_symbol_provided(self):
        User.objects.create_superuser('admin', 'foo@foo.com', 'admin')
        self.client.login(username='admin', password='admin')
        response = self.client.get('/api/stock_price/')
        self.assertEquals(500, response.status_code)

    def test_return_stock_price_for_company(self):
        User.objects.create_superuser('admin', 'foo@foo.com', 'admin')
        self.client.login(username='admin', password='admin')

        response = self.client.get('/api/stock_price/?symbol=IBM')

        self.assertEquals(200, response.status_code)
