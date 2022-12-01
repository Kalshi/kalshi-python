# swagger_client.ExchangeApi

All URIs are relative to *https://trading-api.kalshi.com/trade-api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_exchange_status**](ExchangeApi.md#get_exchange_status) | **GET** /exchange/status | GetExchangeStatus

# **get_exchange_status**
> ExchangeStatus get_exchange_status()

GetExchangeStatus

Endpoint for getting the exchange status.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExchangeApi()

try:
    # GetExchangeStatus
    api_response = api_instance.get_exchange_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExchangeApi->get_exchange_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ExchangeStatus**](ExchangeStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

