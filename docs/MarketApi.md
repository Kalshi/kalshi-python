# swagger_client.MarketApi

All URIs are relative to *https://trading-api.kalshi.com/trade-api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_event**](MarketApi.md#get_event) | **GET** /events/{event_ticker} | GetEvent
[**get_market**](MarketApi.md#get_market) | **GET** /markets/{ticker} | GetMarket
[**get_market_history**](MarketApi.md#get_market_history) | **GET** /markets/{ticker}/history | GetMarketHistory
[**get_market_orderbook**](MarketApi.md#get_market_orderbook) | **GET** /markets/{ticker}/orderbook | GetMarketOrderbook
[**get_markets**](MarketApi.md#get_markets) | **GET** /markets | GetMarkets
[**get_series**](MarketApi.md#get_series) | **GET** /series/{series_ticker} | GetSeries
[**get_trades**](MarketApi.md#get_trades) | **GET** /markets/trades | GetTrades

# **get_event**
> GetEventResponse get_event(event_ticker)

GetEvent

Endpoint for getting data about an event by its ticker.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MarketApi()
event_ticker = 'event_ticker_example' # str | Should be filled with the ticker of the event.

try:
    # GetEvent
    api_response = api_instance.get_event(event_ticker)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->get_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_ticker** | **str**| Should be filled with the ticker of the event. | 

### Return type

[**GetEventResponse**](GetEventResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_market**
> GetMarketResponse get_market(ticker)

GetMarket

Endpoint for getting data about a specific market.  The value for the ticker path parameter should match the ticker of the target market.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MarketApi()
ticker = 'ticker_example' # str | Market ticker for the market being retrieved.

try:
    # GetMarket
    api_response = api_instance.get_market(ticker)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->get_market: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**| Market ticker for the market being retrieved. | 

### Return type

[**GetMarketResponse**](GetMarketResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_market_history**
> GetMarketHistoryResponse get_market_history(ticker, limit=limit, cursor=cursor, min_ts=min_ts, max_ts=max_ts)

GetMarketHistory

Endpoint for getting the statistics history for a market.  The value for the ticker path parameter should match the ticker of the target market. The min_ts parameter is optional, and will restrict statistics to those after provided timestamp. The min_ts is inclusive, which means a market history point at min_ts will be returned.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MarketApi()
ticker = 'ticker_example' # str | Market ticker
limit = 56 # int | Parameter to specify the number of results per page. Defaults to 20. (optional)
cursor = 'cursor_example' # str | The Cursor represents a pointer to the next page of records in the pagination. So this optional parameter, when filled, should be filled with the cursor string returned in a previous request to this end-point. Filling this would basically tell the api to get the next page containing the number of records passed on the limit parameter. On the other side not filling it tells the api you want to get the first page for another query. The cursor does not store any filters, so if any filter parameters like max_ts or min_ts were passed in the original query they must be passed again. (optional)
min_ts = 789 # int | If provided, MinTs restricts history to trades starting from MinTs.  Default value: 1 hour ago. (optional)
max_ts = 789 # int | If provided, MaxTs restricts history to trades up until MaxTs (optional)

try:
    # GetMarketHistory
    api_response = api_instance.get_market_history(ticker, limit=limit, cursor=cursor, min_ts=min_ts, max_ts=max_ts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->get_market_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**| Market ticker | 
 **limit** | **int**| Parameter to specify the number of results per page. Defaults to 20. | [optional] 
 **cursor** | **str**| The Cursor represents a pointer to the next page of records in the pagination. So this optional parameter, when filled, should be filled with the cursor string returned in a previous request to this end-point. Filling this would basically tell the api to get the next page containing the number of records passed on the limit parameter. On the other side not filling it tells the api you want to get the first page for another query. The cursor does not store any filters, so if any filter parameters like max_ts or min_ts were passed in the original query they must be passed again. | [optional] 
 **min_ts** | **int**| If provided, MinTs restricts history to trades starting from MinTs.  Default value: 1 hour ago. | [optional] 
 **max_ts** | **int**| If provided, MaxTs restricts history to trades up until MaxTs | [optional] 

### Return type

[**GetMarketHistoryResponse**](GetMarketHistoryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_market_orderbook**
> GetMarketOrderbookResponse get_market_orderbook(ticker, depth=depth)

GetMarketOrderbook

Endpoint for getting the orderbook for a market.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MarketApi()
ticker = 'ticker_example' # str | Market ticker.
depth = 56 # int | Depth specifies the maximum number of orderbook price levels on either side. (optional)

try:
    # GetMarketOrderbook
    api_response = api_instance.get_market_orderbook(ticker, depth=depth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->get_market_orderbook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**| Market ticker. | 
 **depth** | **int**| Depth specifies the maximum number of orderbook price levels on either side. | [optional] 

### Return type

[**GetMarketOrderbookResponse**](GetMarketOrderbookResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_markets**
> GetMarketsResponse get_markets(limit=limit, cursor=cursor, event_ticker=event_ticker, series_ticker=series_ticker, max_close_ts=max_close_ts, min_close_ts=min_close_ts, status=status, tickers=tickers)

GetMarkets

Endpoint for listing and discovering markets on Kalshi.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MarketApi()
limit = 789 # int | Parameter to specify the number of results per page. Defaults to 20. (optional)
cursor = 'cursor_example' # str | The Cursor represents a pointer to the next page of records in the pagination. So this optional parameter, when filled, should be filled with the cursor string returned in a previous request to this end-point. Filling this would basically tell the api to get the next page containing the number of records passed on the limit parameter. On the other side not filling it tells the api you want to get the first page for another query. The cursor does not store any filters, so if any filter parameters like tickers, max_ts or min_ts were passed in the original query they must be passed again. (optional)
event_ticker = 'event_ticker_example' # str | Event ticker to retrieve markets for. (optional)
series_ticker = 'series_ticker_example' # str | Series ticker to retrieve contracts for. (optional)
max_close_ts = 789 # int | Restricts the markets to those that are closing in or before this timestamp. (optional)
min_close_ts = 789 # int | Restricts the markets to those that are closing in or after this timestamp. (optional)
status = 'status_example' # str | Restricts the markets to those with certain statuses, as a comma separated list. The following values are accepted: open, closed, settled. (optional)
tickers = 'tickers_example' # str | Restricts the markets to those with certain tickers, as a comma separated list. (optional)

try:
    # GetMarkets
    api_response = api_instance.get_markets(limit=limit, cursor=cursor, event_ticker=event_ticker, series_ticker=series_ticker, max_close_ts=max_close_ts, min_close_ts=min_close_ts, status=status, tickers=tickers)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->get_markets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Parameter to specify the number of results per page. Defaults to 20. | [optional] 
 **cursor** | **str**| The Cursor represents a pointer to the next page of records in the pagination. So this optional parameter, when filled, should be filled with the cursor string returned in a previous request to this end-point. Filling this would basically tell the api to get the next page containing the number of records passed on the limit parameter. On the other side not filling it tells the api you want to get the first page for another query. The cursor does not store any filters, so if any filter parameters like tickers, max_ts or min_ts were passed in the original query they must be passed again. | [optional] 
 **event_ticker** | **str**| Event ticker to retrieve markets for. | [optional] 
 **series_ticker** | **str**| Series ticker to retrieve contracts for. | [optional] 
 **max_close_ts** | **int**| Restricts the markets to those that are closing in or before this timestamp. | [optional] 
 **min_close_ts** | **int**| Restricts the markets to those that are closing in or after this timestamp. | [optional] 
 **status** | **str**| Restricts the markets to those with certain statuses, as a comma separated list. The following values are accepted: open, closed, settled. | [optional] 
 **tickers** | **str**| Restricts the markets to those with certain tickers, as a comma separated list. | [optional] 

### Return type

[**GetMarketsResponse**](GetMarketsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_series**
> GetSeriesResponse get_series(series_ticker)

GetSeries

Endpoint for getting data about a series by its ticker.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MarketApi()
series_ticker = 'series_ticker_example' # str | Should be filled with the ticker of the series.

try:
    # GetSeries
    api_response = api_instance.get_series(series_ticker)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->get_series: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_ticker** | **str**| Should be filled with the ticker of the series. | 

### Return type

[**GetSeriesResponse**](GetSeriesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trades**
> PublicTradesGetResponse get_trades(cursor=cursor, limit=limit, ticker=ticker, min_ts=min_ts, max_ts=max_ts)

GetTrades

Endpoint for getting all trades for all markets.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MarketApi()
cursor = 'cursor_example' # str | The Cursor represents a pointer to the next page of records in the pagination. So this optional parameter, when filled, should be filled with the cursor string returned in a previous request to this end-point. Filling this would basically tell the api to get the next page containing the number of records passed on the limit parameter. On the other side not filling it tells the api you want to get the first page for another query. The cursor does not store any filters, so if any filter parameters like ticker, max_ts or min_ts were passed in the original query they must be passed again. (optional)
limit = 56 # int | Parameter to specify the number of results per page. Defaults to 20. (optional)
ticker = 'ticker_example' # str | Parameter to specify a specific market to get trades from. (optional)
min_ts = 789 # int | Restricts the response to trades after a timestamp. (optional)
max_ts = 789 # int | Restricts the response to trades before a timestamp. (optional)

try:
    # GetTrades
    api_response = api_instance.get_trades(cursor=cursor, limit=limit, ticker=ticker, min_ts=min_ts, max_ts=max_ts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MarketApi->get_trades: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| The Cursor represents a pointer to the next page of records in the pagination. So this optional parameter, when filled, should be filled with the cursor string returned in a previous request to this end-point. Filling this would basically tell the api to get the next page containing the number of records passed on the limit parameter. On the other side not filling it tells the api you want to get the first page for another query. The cursor does not store any filters, so if any filter parameters like ticker, max_ts or min_ts were passed in the original query they must be passed again. | [optional] 
 **limit** | **int**| Parameter to specify the number of results per page. Defaults to 20. | [optional] 
 **ticker** | **str**| Parameter to specify a specific market to get trades from. | [optional] 
 **min_ts** | **int**| Restricts the response to trades after a timestamp. | [optional] 
 **max_ts** | **int**| Restricts the response to trades before a timestamp. | [optional] 

### Return type

[**PublicTradesGetResponse**](PublicTradesGetResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

