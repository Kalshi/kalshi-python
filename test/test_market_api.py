# coding: utf-8

"""
    Kalshi Trade API

    This documentation describes Kalshi's trading API (known as Trade API v2). By using this API, you agree to Kalshi's Developer Agreement (https://kalshi.com/developer-agreement).  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: support@kalshi.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import kalshi_python
from kalshi_python.api.market_api import MarketApi  # noqa: E501
from kalshi_python.rest import ApiException


class TestMarketApi(unittest.TestCase):
    """MarketApi unit test stubs"""

    def setUp(self):
        self.api = MarketApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_event(self):
        """Test case for get_event

        GetEvent  # noqa: E501
        """
        pass

    def test_get_market(self):
        """Test case for get_market

        GetMarket  # noqa: E501
        """
        pass

    def test_get_market_history(self):
        """Test case for get_market_history

        GetMarketHistory  # noqa: E501
        """
        pass

    def test_get_market_orderbook(self):
        """Test case for get_market_orderbook

        GetMarketOrderbook  # noqa: E501
        """
        pass

    def test_get_markets(self):
        """Test case for get_markets

        GetMarkets  # noqa: E501
        """
        pass

    def test_get_series(self):
        """Test case for get_series

        GetSeries  # noqa: E501
        """
        pass

    def test_get_trades(self):
        """Test case for get_trades

        GetTrades  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()