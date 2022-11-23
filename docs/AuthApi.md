# kalshi_python.AuthApi

All URIs are relative to *https://trading-api.kalshi.com/trade-api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login**](AuthApi.md#login) | **POST** /login | Login
[**logout**](AuthApi.md#logout) | **POST** /logout | Logout

# **login**
> LoginResponse login(body)

Login

Endpoint to start a REST session with the Kalshi API.

### Example

```python
from __future__ import print_function
import time
import kalshi_python
from kalshi_python.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kalshi_python.AuthApi()
body = kalshi_python.LoginRequest() # LoginRequest | Login input data

try:
    # Login
    api_response = api_instance.login(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoginRequest**](LoginRequest.md)| Login input data | 

### Return type

[**LoginResponse**](LoginResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout**
> logout()

Logout

Terminate your session with Kalshi. After this endpoint is called, the session token previously returned by the `/log_in` endpoint will no longer be valid.

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
# Configure API key authorization: session_cookie
configuration = kalshi_python.Configuration()
configuration.api_key['Cookie'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Cookie'] = 'Bearer'

# create an instance of the API class
api_instance = kalshi_python.AuthApi(kalshi_python.ApiClient(configuration))

try:
    # Logout
    api_instance.logout()
except ApiException as e:
    print("Exception when calling AuthApi->logout: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[bearer_token](../README.md#bearer_token), [session_cookie](../README.md#session_cookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

