# ExchangeStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exchange_active** | **bool** | False if the core Kalshi exchange is no longer taking any state changes at all. This includes but is not limited to trading, new users, and transfers. True unless we are under maintenance. | 
**trading_active** | **bool** | True if we are currently permitting trading on the exchange. This is true during trading hours and false outside exchange hours. Kalshi reserves the right to pause at any time in case issues are detected. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

