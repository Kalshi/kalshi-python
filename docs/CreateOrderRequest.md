# CreateOrderRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Specifies if this is a buy or sell order. | 
**buy_max_cost** | **int** | If type &#x3D; market and action &#x3D; buy, buy_max_cost represents the maximum cents that can be spent to acquire a position. | [optional] 
**client_order_id** | **str** | Member-provided UUID to attach to the order. | 
**count** | **int** | Number of contracts to be bought or sold. | 
**expiration_ts** | **int** | Expiration time of the order, in unix seconds.  If this is not supplied, the order won&#x27;t expire until explicitly cancelled. This is also known as Good &#x27;Till Cancelled (GTC).  If the time is in the past, the order will attempt to partially or completely fill and the remaining unfilled quantity will be cancelled. This is also known as Immediate-or-Cancel (IOC).  If the time is in the future, the remaining unfilled quantity order will expire at the specified time. | [optional] 
**no_price** | **int** | Submitting price of the No side of the trade, in cents. Exactly one of yes_price and no_price must be passed. If both prices are passed, return 400. | [optional] 
**sell_position_floor** | **int** | SellPositionFloor will not let you flip position for a market order if set to 0. | [optional] 
**side** | **str** | Specifies if this is a &#x27;yes&#x27; or &#x27;no&#x27; order. | 
**ticker** | **str** | The ticker of the market the order will be placed in. | 
**type** | **str** | Specifies if this is a \&quot;market\&quot; or a \&quot;limit\&quot; order. Note that either the Yes Price or the No Price must be provided for limit orders. | 
**yes_price** | **int** | Submitting price of the Yes side of the trade, in cents. Exactly one of yes_price and no_price must be passed. If both prices are passed, return 400. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

