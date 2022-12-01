# Order

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Representing trade action; currently supports buy and sell. | 
**client_order_id** | **str** | Optional unique identifier for order placement. | 
**close_cancel_count** | **int** | The size of resting orders canceled because of market close (contract units). | [optional] 
**created_time** | [**OutputTime**](OutputTime.md) |  | [optional] 
**decrease_count** | **int** | The reduction in the size of resting for orders (contract units). | [optional] 
**expiration_time** | [**OutputTime**](OutputTime.md) |  | [optional] 
**fcc_cancel_count** | **int** | The size of resting contracts canceled because of exchange operations (contract units). | [optional] 
**last_update_time** | [**OutputTime**](OutputTime.md) |  | [optional] 
**maker_fill_count** | **int** | The size of filled maker orders (contract units). | [optional] 
**no_price** | [**Cent**](Cent.md) |  | 
**order_id** | **str** |  | [optional] 
**place_count** | **int** | the size of placed maker orders (contract units). | [optional] 
**queue_position** | **int** | Position in the priority queue at a given price level | [optional] 
**remaining_count** | **int** | The size of the remaining resting orders (contract units). | [optional] 
**side** | **str** | Representing direction of the order; currently supports yes and no. | 
**status** | [**OrderStatus**](OrderStatus.md) |  | 
**taker_fees** | [**Cent**](Cent.md) |  | [optional] 
**taker_fill_cost** | [**Cent**](Cent.md) |  | [optional] 
**taker_fill_count** | **int** | The size of filled taker orders (contract units) | [optional] 
**ticker** | **str** | Unique identifier for markets. | 
**type** | [**OrderType**](OrderType.md) |  | 
**user_id** | **str** |  | [optional] 
**yes_price** | [**Cent**](Cent.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

