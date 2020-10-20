import logging
import requests

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from django.contrib.auth.mixins import LoginRequiredMixin

logger = logging.getLogger(__name__)


class ListCompanies(LoginRequiredMixin, APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'companies_list.html'
    login_url = '/login/'

    def get(self, request, format=None):
        """
        Return a list of all compaines.
        """
        try:
            response = requests.get(
                "https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=Micro&apikey=demo")

            companies_data = response.json()['bestMatches']
            res = []

            for company in companies_data:
                res.append({'name': company['2. name'], 'symbol': company['1. symbol']})

            return Response({'companies': res}, status=status.HTTP_200_OK)

        except Exception as e:

            logger.exception(f"Error {e} while listing companies")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CompanyStockPrice(LoginRequiredMixin, APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'stock.html'
    login_url = '/login/'

    def get(self, request, format=None):
        """
        Return a stock prices for given companies.
        """
        try:
            company_symbol = request.GET.get('symbol')

            assert company_symbol, "You must provide Company Symbol"
            response = requests.get(
                f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={company_symbol}&apikey=demo" # noqa
            )
            stock_data = response.json()['Time Series (Daily)']
            stock_prices = []

            for date, stock in stock_data.items():
                stock_prices.append({
                    "date": date,
                    "open": float(stock['1. open']),
                    "close": float(stock['4. close']),
                    "high": float(stock['2. high']),
                    "low": float(stock['3. low']),
                    "volume": float(stock['5. volume'])
                })

            return Response({'stock_prices': stock_prices}, status=status.HTTP_200_OK)

        except Exception as e:

            logger.exception(f"Error {e} while getting stock prices")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
