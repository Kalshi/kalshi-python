# OrderConfirmation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Representing trade action; currently supports buy and sell. | 
**client_order_id** | **str** | Optional unique identifier for order placement. | 
**created_time** | [**OutputTime**](OutputTime.md) |  | [optional] 
**expiration_time** | [**OutputTime**](OutputTime.md) |  | [optional] 
**no_price** | **int** | The no price for this order in cents. | 
**order_id** | **str** | Unique identifier for orders. | 
**side** | **str** | Representing direction of the order; currently supports yes and no. | 
**status** | **str** | The current status of a given order. | 
**ticker** | **str** | Unique identifier for markets. | 
**type** | **str** | Representing order type; currently supports \&quot;market\&quot; and \&quot;limit\&quot;. | 
**user_id** | **str** |  | [optional] 
**yes_price** | **int** | The yes price for this order in cents. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

