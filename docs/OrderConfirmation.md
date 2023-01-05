# OrderConfirmation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Representing trade action; currently supports buy and sell. | 
**client_order_id** | **str** | Optional unique identifier for order placement. | 
**created_time** | [**OutputTime**](OutputTime.md) |  | [optional] 
**expiration_time** | [**OutputTime**](OutputTime.md) |  | [optional] 
**no_price** | [**Cent**](Cent.md) |  | 
**order_id** | **str** |  | [optional] 
**side** | **str** | Representing direction of the order; currently supports yes and no. | 
**status** | [**OrderStatus**](OrderStatus.md) |  | 
**ticker** | **str** | Unique identifier for markets. | 
**type** | [**OrderType**](OrderType.md) |  | 
**user_id** | **str** |  | [optional] 
**yes_price** | [**Cent**](Cent.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

