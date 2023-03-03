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
**no_price** | **int** | Submitting price of the No side of the trade, in cents. Exactly one of yes_price and no_price must be passed. If both prices are passed, return 400. | 
**order_id** | **str** | Unique identifier for orders. | 
**place_count** | **int** | the size of placed maker orders (contract units). | [optional] 
**queue_position** | **int** | Position in the priority queue at a given price level | [optional] 
**remaining_count** | **int** | The size of the remaining resting orders (contract units). | [optional] 
**side** | **str** | Representing direction of the order; currently supports yes and no. | 
**status** | **str** | The current status of this order. | 
**taker_fees** | **int** | Fees paid on filled orders, in cents. | [optional] 
**taker_fill_cost** | **int** | The cost of filled taker orders in cents. | [optional] 
**taker_fill_count** | **int** | The size of filled taker orders (contract units) | [optional] 
**ticker** | **str** | Unique identifier for markets. | 
**type** | **str** | Representing order type; currently supports \&quot;market\&quot; and \&quot;limit\&quot;. | 
**user_id** | **str** |  | [optional] 
**yes_price** | **int** | The yes price for this order in cents. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

