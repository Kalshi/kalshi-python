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

class CancelOrderResponse(object):
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
        'order': 'Order',
        'reduced_by': 'int'
    }

    attribute_map = {
        'order': 'order',
        'reduced_by': 'reduced_by'
    }

    def __init__(self, order=None, reduced_by=None):  # noqa: E501
        """CancelOrderResponse - a model defined in Swagger"""  # noqa: E501
        self._order = None
        self._reduced_by = None
        self.discriminator = None
        self.order = order
        self.reduced_by = reduced_by

    @property
    def order(self):
        """Gets the order of this CancelOrderResponse.  # noqa: E501


        :return: The order of this CancelOrderResponse.  # noqa: E501
        :rtype: Order
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this CancelOrderResponse.


        :param order: The order of this CancelOrderResponse.  # noqa: E501
        :type: Order
        """
        if order is None:
            raise ValueError("Invalid value for `order`, must not be `None`")  # noqa: E501

        self._order = order

    @property
    def reduced_by(self):
        """Gets the reduced_by of this CancelOrderResponse.  # noqa: E501

        ReducedBy is how much the count of the order was reduced by because of this operation.  # noqa: E501

        :return: The reduced_by of this CancelOrderResponse.  # noqa: E501
        :rtype: int
        """
        return self._reduced_by

    @reduced_by.setter
    def reduced_by(self, reduced_by):
        """Sets the reduced_by of this CancelOrderResponse.

        ReducedBy is how much the count of the order was reduced by because of this operation.  # noqa: E501

        :param reduced_by: The reduced_by of this CancelOrderResponse.  # noqa: E501
        :type: int
        """
        if reduced_by is None:
            raise ValueError("Invalid value for `reduced_by`, must not be `None`")  # noqa: E501

        self._reduced_by = reduced_by

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
        if issubclass(CancelOrderResponse, dict):
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
        if not isinstance(other, CancelOrderResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
