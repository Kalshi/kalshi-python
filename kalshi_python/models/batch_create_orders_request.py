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

class BatchCreateOrdersRequest(object):
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
        'orders': 'list[CreateOrderRequest]'
    }

    attribute_map = {
        'orders': 'orders'
    }

    def __init__(self, orders=None):  # noqa: E501
        """BatchCreateOrdersRequest - a model defined in Swagger"""  # noqa: E501
        self._orders = None
        self.discriminator = None
        self.orders = orders

    @property
    def orders(self):
        """Gets the orders of this BatchCreateOrdersRequest.  # noqa: E501

        An array of individual orders to place.  # noqa: E501

        :return: The orders of this BatchCreateOrdersRequest.  # noqa: E501
        :rtype: list[CreateOrderRequest]
        """
        return self._orders

    @orders.setter
    def orders(self, orders):
        """Sets the orders of this BatchCreateOrdersRequest.

        An array of individual orders to place.  # noqa: E501

        :param orders: The orders of this BatchCreateOrdersRequest.  # noqa: E501
        :type: list[CreateOrderRequest]
        """
        if orders is None:
            raise ValueError("Invalid value for `orders`, must not be `None`")  # noqa: E501

        self._orders = orders

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
        if issubclass(BatchCreateOrdersRequest, dict):
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
        if not isinstance(other, BatchCreateOrdersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
