# coding: utf-8

"""
    Kalshi Trade API

    This documentation describes Kalshi's trading API (known as Trade API v2). By using this API, you agree to Kalshi's Developer Agreement (https://kalshi.com/developer-agreement).  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: support@kalshi.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PublicTrade(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'count': 'int',
        'created_time': 'OutputTime',
        'taker_side': 'str',
        'ticker': 'str',
        'trade_id': 'str',
        'yes_price': 'Cent'
    }

    attribute_map = {
        'count': 'count',
        'created_time': 'created_time',
        'taker_side': 'taker_side',
        'ticker': 'ticker',
        'trade_id': 'trade_id',
        'yes_price': 'yes_price'
    }

    def __init__(self, count=None, created_time=None, taker_side=None, ticker=None, trade_id=None, yes_price=None):  # noqa: E501
        """PublicTrade - a model defined in Swagger"""  # noqa: E501
        self._count = None
        self._created_time = None
        self._taker_side = None
        self._ticker = None
        self._trade_id = None
        self._yes_price = None
        self.discriminator = None
        if count is not None:
            self.count = count
        if created_time is not None:
            self.created_time = created_time
        if taker_side is not None:
            self.taker_side = taker_side
        if ticker is not None:
            self.ticker = ticker
        if trade_id is not None:
            self.trade_id = trade_id
        if yes_price is not None:
            self.yes_price = yes_price

    @property
    def count(self):
        """Gets the count of this PublicTrade.  # noqa: E501


        :return: The count of this PublicTrade.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this PublicTrade.


        :param count: The count of this PublicTrade.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def created_time(self):
        """Gets the created_time of this PublicTrade.  # noqa: E501


        :return: The created_time of this PublicTrade.  # noqa: E501
        :rtype: OutputTime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this PublicTrade.


        :param created_time: The created_time of this PublicTrade.  # noqa: E501
        :type: OutputTime
        """

        self._created_time = created_time

    @property
    def taker_side(self):
        """Gets the taker_side of this PublicTrade.  # noqa: E501


        :return: The taker_side of this PublicTrade.  # noqa: E501
        :rtype: str
        """
        return self._taker_side

    @taker_side.setter
    def taker_side(self, taker_side):
        """Sets the taker_side of this PublicTrade.


        :param taker_side: The taker_side of this PublicTrade.  # noqa: E501
        :type: str
        """
        allowed_values = ["yes", "no", "invalid", ""]  # noqa: E501
        if taker_side not in allowed_values:
            raise ValueError(
                "Invalid value for `taker_side` ({0}), must be one of {1}"  # noqa: E501
                .format(taker_side, allowed_values)
            )

        self._taker_side = taker_side

    @property
    def ticker(self):
        """Gets the ticker of this PublicTrade.  # noqa: E501


        :return: The ticker of this PublicTrade.  # noqa: E501
        :rtype: str
        """
        return self._ticker

    @ticker.setter
    def ticker(self, ticker):
        """Sets the ticker of this PublicTrade.


        :param ticker: The ticker of this PublicTrade.  # noqa: E501
        :type: str
        """

        self._ticker = ticker

    @property
    def trade_id(self):
        """Gets the trade_id of this PublicTrade.  # noqa: E501


        :return: The trade_id of this PublicTrade.  # noqa: E501
        :rtype: str
        """
        return self._trade_id

    @trade_id.setter
    def trade_id(self, trade_id):
        """Sets the trade_id of this PublicTrade.


        :param trade_id: The trade_id of this PublicTrade.  # noqa: E501
        :type: str
        """

        self._trade_id = trade_id

    @property
    def yes_price(self):
        """Gets the yes_price of this PublicTrade.  # noqa: E501


        :return: The yes_price of this PublicTrade.  # noqa: E501
        :rtype: Cent
        """
        return self._yes_price

    @yes_price.setter
    def yes_price(self, yes_price):
        """Sets the yes_price of this PublicTrade.


        :param yes_price: The yes_price of this PublicTrade.  # noqa: E501
        :type: Cent
        """

        self._yes_price = yes_price

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(PublicTrade, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PublicTrade):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
