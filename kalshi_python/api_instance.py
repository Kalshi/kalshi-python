# coding: utf-8
"""
    Kalshi Trade API

    This documentation describes Kalshi's trading API (known as Trade API v2). By using this API, you agree to Kalshi's Developer Agreement (https://kalshi.com/developer-agreement).  # noqa: E501

    OpenAPI spec version: 2.0.0
"""
from __future__ import absolute_import

from kalshi_python import ApiClient
from kalshi_python.api import AuthApi, PortfolioApi, MarketApi, ExchangeApi
from kalshi_python.models import LoginRequest
from pprint import pprint


class ApiInstance(object):

    def __init__(self, email=None, password=None, configuration=None, header_name=None, header_value=None,
                 cookie=None):
        # Store credentials if provided
        if email is not None and password is not None:
            self.email = email
            self.password = password

        self.api_client = ApiClient(configuration=configuration, header_name=header_name, header_value=header_value,
                                    cookie=cookie)
        # Set up individual apis
        self.exchange_api = ExchangeApi(self.api_client)
        self.auth_api = AuthApi(self.api_client)
        self.portfolio_api = PortfolioApi(self.api_client)
        self.market_api = MarketApi(self.api_client)

    def set_api_token(self, token):
        self.api_client.configuration.api_key_prefix['Authorization'] = 'Bearer'
        self.api_client.configuration.api_key['Authorization'] = token

    def auto_login_if_possible(self):
        if 'Authorization' in self.api_client.configuration.api_key.keys():
            return

        if hasattr(self, 'email') and hasattr(self, 'password'):
            loginResponse = self.login(LoginRequest(
                email=self.email,
                password=self.password,
            ))
            self.set_api_token(loginResponse.token)

    # Proxy exchange methods
    def get_exchange_status(self, **kwargs):
        return self.exchange_api.get_exchange_status(**kwargs)

    # Proxy auth methods
    def login(self, body, **kwargs):
        response = self.auth_api.login(body, **kwargs)
        return response

    def logout(self, **kwargs):
        return self.auth_api.logout(**kwargs)

    # Proxy market methods
    def get_event(self, event_ticker, **kwargs):
        return self.market_api.get_event(event_ticker, **kwargs)

    def get_events(self, **kwargs):
        return self.market_api.get_events(**kwargs)

    def get_market(self, ticker, **kwargs):
        return self.market_api.get_market(ticker, **kwargs)

    def get_market_history(self, ticker, **kwargs):
        self.auto_login_if_possible()
        return self.market_api.get_market_history(ticker, **kwargs)

    def get_market_orderbook(self, ticker, **kwargs):
        self.auto_login_if_possible()
        return self.market_api.get_market_orderbook(ticker, **kwargs)

    def get_markets(self, **kwargs):
        self.auto_login_if_possible()
        return self.market_api.get_markets(**kwargs)

    def get_series(self, series_ticker, **kwargs):
        return self.market_api.get_series(series_ticker, **kwargs)

    def get_trades(self, **kwargs):
        return self.market_api.get_trades(**kwargs)

    # Proxy portfolio methods
    def batch_cancel_orders(self, body, **kwargs):
        self.auto_login_if_possible()
        return self.portfolio_api.batch_cancel_orders(body, **kwargs)

    def batch_create_orders(self, body, **kwargs):
        self.auto_login_if_possible()
        return self.portfolio_api.batch_create_orders(body, **kwargs)

    def cancel_order(self, order_id, **kwargs):
        self.auto_login_if_possible()
        return self.portfolio_api.cancel_order(order_id, **kwargs)

    def create_order(self, body, **kwargs):
        self.auto_login_if_possible()
        return self.portfolio_api.create_order(body, **kwargs)

    def decrease_order(self, body, order_id, **kwargs):
        self.auto_login_if_possible()
        return self.portfolio_api.decrease_order(body, order_id, **kwargs)

    def get_balance(self, **kwargs):
        self.auto_login_if_possible()
        return self.portfolio_api.get_balance(**kwargs)

    def get_fills(self, **kwargs):
        self.auto_login_if_possible()
        return self.portfolio_api.get_fills(**kwargs)

    def get_order(self, order_id, **kwargs):
        self.auto_login_if_possible()
        return self.portfolio_api.get_order(order_id, **kwargs)

    def get_orders(self, **kwargs):
        self.auto_login_if_possible()
        return self.portfolio_api.get_orders(**kwargs)

    def get_portfolio_settlements(self, **kwargs):
        self.auto_login_if_possible()
        return self.portfolio_api.get_portfolio_settlements(**kwargs)

    def get_positions(self, **kwargs):
        self.auto_login_if_possible()
        return self.portfolio_api.get_positions(**kwargs)
