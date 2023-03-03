# kalshi_python.PortfolioApi

All URIs are relative to *https://trading-api.kalshi.com/trade-api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_cancel_orders**](PortfolioApi.md#batch_cancel_orders) | **DELETE** /portfolio/orders/batched | BatchCancelOrders
[**batch_create_orders**](PortfolioApi.md#batch_create_orders) | **POST** /portfolio/orders/batched | BatchCreateOrders
[**cancel_order**](PortfolioApi.md#cancel_order) | **DELETE** /portfolio/orders/{order_id} | CancelOrder
[**create_order**](PortfolioApi.md#create_order) | **POST** /portfolio/orders | CreateOrder
[**decrease_order**](PortfolioApi.md#decrease_order) | **POST** /portfolio/orders/{order_id}/decrease | DecreaseOrder
[**get_balance**](PortfolioApi.md#get_balance) | **GET** /portfolio/balance | GetBalance
[**get_fills**](PortfolioApi.md#get_fills) | **GET** /portfolio/fills | GetFills
[**get_order**](PortfolioApi.md#get_order) | **GET** /portfolio/orders/{order_id} | GetOrder
[**get_orders**](PortfolioApi.md#get_orders) | **GET** /portfolio/orders | GetOrders
[**get_portfolio_settlements**](PortfolioApi.md#get_portfolio_settlements) | **GET** /portfolio/settlements | GetPortfolioSettlements
[**get_positions**](PortfolioApi.md#get_positions) | **GET** /portfolio/positions | GetPositions

# **batch_cancel_orders**
> BatchCancelOrdersResponse batch_cancel_orders(body)

BatchCancelOrders

Endpoint for cancelling up to 20 orders at once. Available to members with advanced access only.

### Example
```python
from __future__ import print_function
import time
import kalshi_python
from kalshi_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearer_token
configuration = kalshi_python.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kalshi_python.PortfolioApi(kalshi_python.ApiClient(configuration))
body = kalshi_python.BatchCancelOrdersRequest() # BatchCancelOrdersRequest | Batch orders cancel input data.

try:
    # BatchCancelOrders
    api_response = api_instance.batch_cancel_orders(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioApi->batch_cancel_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BatchCancelOrdersRequest**](BatchCancelOrdersRequest.md)| Batch orders cancel input data. | 

### Return type

[**BatchCancelOrdersResponse**](BatchCancelOrdersResponse.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_create_orders**
> BatchCreateOrdersResponse batch_create_orders(body)

BatchCreateOrders

Endpoint for submitting a batch of orders.  Each order in the batch is counted against the total rate limit for order operations. Consequently, the size of the batch is capped by the current per-second rate-limit configuration applicable to the user.  At the moment of writing, the limit is 20 orders per batch. Available to members with advanced access only.

### Example
```python
from __future__ import print_function
import time
import kalshi_python
from kalshi_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearer_token
configuration = kalshi_python.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kalshi_python.PortfolioApi(kalshi_python.ApiClient(configuration))
body = kalshi_python.BatchCreateOrdersRequest() # BatchCreateOrdersRequest | Batch order create input data.

try:
    # BatchCreateOrders
    api_response = api_instance.batch_create_orders(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioApi->batch_create_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BatchCreateOrdersRequest**](BatchCreateOrdersRequest.md)| Batch order create input data. | 

### Return type

[**BatchCreateOrdersResponse**](BatchCreateOrdersResponse.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_order**
> CancelOrderResponse cancel_order(order_id)

CancelOrder

Endpoint for canceling orders.  The value for the orderId should match the id field of the order you want to decrease. Commonly, DELETE-type endpoints return 204 status with no body content on success. But we can't completely delete the order, as it may be partially filled already. Instead, the DeleteOrder endpoint reduce the order completely, essentially zeroing the remaining resting contracts on it. The zeroed order is returned on the response payload as a form of validation for the client.

### Example
```python
from __future__ import print_function
import time
import kalshi_python
from kalshi_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearer_token
configuration = kalshi_python.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kalshi_python.PortfolioApi(kalshi_python.ApiClient(configuration))
order_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Order_id input for the current order.

try:
    # CancelOrder
    api_response = api_instance.cancel_order(order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioApi->cancel_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | [**str**](.md)| Order_id input for the current order. | 

### Return type

[**CancelOrderResponse**](CancelOrderResponse.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_order**
> CreateOrderResponse create_order(body)

CreateOrder

Endpoint for submitting orders in a market.

### Example
```python
from __future__ import print_function
import time
import kalshi_python
from kalshi_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearer_token
configuration = kalshi_python.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kalshi_python.PortfolioApi(kalshi_python.ApiClient(configuration))
body = kalshi_python.CreateOrderRequest() # CreateOrderRequest | Order create input data

try:
    # CreateOrder
    api_response = api_instance.create_order(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioApi->create_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateOrderRequest**](CreateOrderRequest.md)| Order create input data | 

### Return type

[**CreateOrderResponse**](CreateOrderResponse.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **decrease_order**
> DecreaseOrderResponse decrease_order(body, order_id)

DecreaseOrder

Endpoint for decreasing the number of contracts in an existing order. This is the only kind of edit available on order quantity. Cancelling an order is equivalent to decreasing an order amount to zero.

### Example
```python
from __future__ import print_function
import time
import kalshi_python
from kalshi_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearer_token
configuration = kalshi_python.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kalshi_python.PortfolioApi(kalshi_python.ApiClient(configuration))
body = kalshi_python.DecreaseOrderRequest() # DecreaseOrderRequest | Order data
order_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the order to be decreased.

try:
    # DecreaseOrder
    api_response = api_instance.decrease_order(body, order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioApi->decrease_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DecreaseOrderRequest**](DecreaseOrderRequest.md)| Order data | 
 **order_id** | [**str**](.md)| ID of the order to be decreased. | 

### Return type

[**DecreaseOrderResponse**](DecreaseOrderResponse.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balance**
> GetBalanceResponse get_balance()

GetBalance

Endpoint for getting the balance of the logged-in member.

### Example
```python
from __future__ import print_function
import time
import kalshi_python
from kalshi_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearer_token
configuration = kalshi_python.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kalshi_python.PortfolioApi(kalshi_python.ApiClient(configuration))

try:
    # GetBalance
    api_response = api_instance.get_balance()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioApi->get_balance: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetBalanceResponse**](GetBalanceResponse.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fills**
> GetFillsResponse get_fills(ticker=ticker, order_id=order_id, min_ts=min_ts, max_ts=max_ts, limit=limit, cursor=cursor)

GetFills

Endpoint for getting all fills for the logged-in member.

### Example
```python
from __future__ import print_function
import time
import kalshi_python
from kalshi_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearer_token
configuration = kalshi_python.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kalshi_python.PortfolioApi(kalshi_python.ApiClient(configuration))
ticker = 'ticker_example' # str | Restricts the response to trades in a specific market. (optional)
order_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Restricts the response to trades related to a specific order. (optional)
min_ts = 789 # int | Restricts the response to trades after a timestamp. (optional)
max_ts = 789 # int | Restricts the response to trades before a timestamp. (optional)
limit = 56 # int | Parameter to specify the number of results per page. Defaults to 100. (optional)
cursor = 'cursor_example' # str | The Cursor represents a pointer to the next page of records in the pagination. So this optional parameter, when filled, should be filled with the cursor string returned in a previous request to this end-point. Filling this would basically tell the api to get the next page containing the number of records passed on the limit parameter. On the other side not filling it tells the api you want to get the first page for another query. The cursor does not store any filters, so if any filter parameters like ticker, max_ts or min_ts were passed in the original query they must be passed again. (optional)

try:
    # GetFills
    api_response = api_instance.get_fills(ticker=ticker, order_id=order_id, min_ts=min_ts, max_ts=max_ts, limit=limit, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioApi->get_fills: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**| Restricts the response to trades in a specific market. | [optional] 
 **order_id** | [**str**](.md)| Restricts the response to trades related to a specific order. | [optional] 
 **min_ts** | **int**| Restricts the response to trades after a timestamp. | [optional] 
 **max_ts** | **int**| Restricts the response to trades before a timestamp. | [optional] 
 **limit** | **int**| Parameter to specify the number of results per page. Defaults to 100. | [optional] 
 **cursor** | **str**| The Cursor represents a pointer to the next page of records in the pagination. So this optional parameter, when filled, should be filled with the cursor string returned in a previous request to this end-point. Filling this would basically tell the api to get the next page containing the number of records passed on the limit parameter. On the other side not filling it tells the api you want to get the first page for another query. The cursor does not store any filters, so if any filter parameters like ticker, max_ts or min_ts were passed in the original query they must be passed again. | [optional] 

### Return type

[**GetFillsResponse**](GetFillsResponse.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order**
> GetOrderResponse get_order(order_id)

GetOrder

Endpoint for getting a single order.

### Example
```python
from __future__ import print_function
import time
import kalshi_python
from kalshi_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearer_token
configuration = kalshi_python.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kalshi_python.PortfolioApi(kalshi_python.ApiClient(configuration))
order_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Order_id input for the current order.

try:
    # GetOrder
    api_response = api_instance.get_order(order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioApi->get_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | [**str**](.md)| Order_id input for the current order. | 

### Return type

[**GetOrderResponse**](GetOrderResponse.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orders**
> GetOrdersResponse get_orders(ticker=ticker, event_ticker=event_ticker, min_ts=min_ts, max_ts=max_ts, status=status, cursor=cursor, limit=limit)

GetOrders

Endpoint for getting all orders for the logged-in member.

### Example
```python
from __future__ import print_function
import time
import kalshi_python
from kalshi_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearer_token
configuration = kalshi_python.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kalshi_python.PortfolioApi(kalshi_python.ApiClient(configuration))
ticker = 'ticker_example' # str | Restricts the response to orders in a single market. (optional)
event_ticker = 'event_ticker_example' # str | Restricts the response to orders in a single event. (optional)
min_ts = 789 # int | Restricts the response to orders after a timestamp, formatted as a Unix Timestamp. (optional)
max_ts = 789 # int | Restricts the response to orders before a timestamp, formatted as a Unix Timestamp. (optional)
status = 'status_example' # str | Restricts the response to orders that have a certain status: resting, canceled, or executed. (optional)
cursor = 'cursor_example' # str | The Cursor represents a pointer to the next page of records in the pagination. So this optional parameter, when filled, should be filled with the cursor string returned in a previous request to this end-point. Filling this would basically tell the api to get the next page containing the number of records passed on the limit parameter. On the other side not filling it tells the api you want to get the first page for another query. The cursor does not store any filters, so if any filter parameters like ticker, max_ts or min_ts were passed in the original query they must be passed again. (optional)
limit = 56 # int | Parameter to specify the number of results per page. Defaults to 100. (optional)

try:
    # GetOrders
    api_response = api_instance.get_orders(ticker=ticker, event_ticker=event_ticker, min_ts=min_ts, max_ts=max_ts, status=status, cursor=cursor, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioApi->get_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**| Restricts the response to orders in a single market. | [optional] 
 **event_ticker** | **str**| Restricts the response to orders in a single event. | [optional] 
 **min_ts** | **int**| Restricts the response to orders after a timestamp, formatted as a Unix Timestamp. | [optional] 
 **max_ts** | **int**| Restricts the response to orders before a timestamp, formatted as a Unix Timestamp. | [optional] 
 **status** | **str**| Restricts the response to orders that have a certain status: resting, canceled, or executed. | [optional] 
 **cursor** | **str**| The Cursor represents a pointer to the next page of records in the pagination. So this optional parameter, when filled, should be filled with the cursor string returned in a previous request to this end-point. Filling this would basically tell the api to get the next page containing the number of records passed on the limit parameter. On the other side not filling it tells the api you want to get the first page for another query. The cursor does not store any filters, so if any filter parameters like ticker, max_ts or min_ts were passed in the original query they must be passed again. | [optional] 
 **limit** | **int**| Parameter to specify the number of results per page. Defaults to 100. | [optional] 

### Return type

[**GetOrdersResponse**](GetOrdersResponse.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portfolio_settlements**
> GetPortfolioSettlementsResponse get_portfolio_settlements(limit=limit, cursor=cursor)

GetPortfolioSettlements

Endpoint for getting the logged-in member's settlements historical track.

### Example
```python
from __future__ import print_function
import time
import kalshi_python
from kalshi_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearer_token
configuration = kalshi_python.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kalshi_python.PortfolioApi(kalshi_python.ApiClient(configuration))
limit = 789 # int | Parameter to specify the number of results per page. Defaults to 100. (optional)
cursor = 'cursor_example' # str | The Cursor represents a pointer to the next page of records in the pagination. So this optional parameter, when filled, should be filled with the cursor string returned in a previous request to this end-point. Filling this would basically tell the api to get the next page containing the number of records passed on the limit parameter. On the other side not filling it tells the api you want to get the first page for another query. (optional)

try:
    # GetPortfolioSettlements
    api_response = api_instance.get_portfolio_settlements(limit=limit, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioApi->get_portfolio_settlements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Parameter to specify the number of results per page. Defaults to 100. | [optional] 
 **cursor** | **str**| The Cursor represents a pointer to the next page of records in the pagination. So this optional parameter, when filled, should be filled with the cursor string returned in a previous request to this end-point. Filling this would basically tell the api to get the next page containing the number of records passed on the limit parameter. On the other side not filling it tells the api you want to get the first page for another query. | [optional] 

### Return type

[**GetPortfolioSettlementsResponse**](GetPortfolioSettlementsResponse.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_positions**
> GetPositionsResponse get_positions(cursor=cursor, limit=limit, settlement_status=settlement_status, ticker=ticker, event_ticker=event_ticker)

GetPositions

Endpoint for getting all market positions for the logged-in member.

### Example
```python
from __future__ import print_function
import time
import kalshi_python
from kalshi_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearer_token
configuration = kalshi_python.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kalshi_python.PortfolioApi(kalshi_python.ApiClient(configuration))
cursor = 'cursor_example' # str | The Cursor represents a pointer to the next page of records in the pagination. So this optional parameter, when filled, should be filled with the cursor string returned in a previous request to this end-point. Filling this would basically tell the api to get the next page containing the number of records passed on the limit parameter. On the other side not filling it tells the api you want to get the first page for another query. The cursor does not store any filters, so if any filter parameters like settlement_status, ticker, or event_ticker were passed in the original query they must be passed again. (optional)
limit = 56 # int | Parameter to specify the number of results per page. Defaults to 100. (optional)
settlement_status = 'settlement_status_example' # str | Settlement status of the markets to return. Defaults to unsettled. (optional)
ticker = 'ticker_example' # str | Ticker of desired positions. (optional)
event_ticker = 'event_ticker_example' # str | Event ticker of desired positions. (optional)

try:
    # GetPositions
    api_response = api_instance.get_positions(cursor=cursor, limit=limit, settlement_status=settlement_status, ticker=ticker, event_ticker=event_ticker)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioApi->get_positions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| The Cursor represents a pointer to the next page of records in the pagination. So this optional parameter, when filled, should be filled with the cursor string returned in a previous request to this end-point. Filling this would basically tell the api to get the next page containing the number of records passed on the limit parameter. On the other side not filling it tells the api you want to get the first page for another query. The cursor does not store any filters, so if any filter parameters like settlement_status, ticker, or event_ticker were passed in the original query they must be passed again. | [optional] 
 **limit** | **int**| Parameter to specify the number of results per page. Defaults to 100. | [optional] 
 **settlement_status** | **str**| Settlement status of the markets to return. Defaults to unsettled. | [optional] 
 **ticker** | **str**| Ticker of desired positions. | [optional] 
 **event_ticker** | **str**| Event ticker of desired positions. | [optional] 

### Return type

[**GetPositionsResponse**](GetPositionsResponse.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

