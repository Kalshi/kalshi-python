# Market

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_close_early** | **bool** | If true then this market can close earlier then the time provided on close_time. | 
**cap_strike** | [**Number**](Number.md) |  | [optional] 
**category** | **str** | Category for this market. | 
**close_time** | [**OutputTime**](OutputTime.md) |  | 
**custom_strike** | **dict(str, object)** | Expiration value for each target that leads to a YES settlement.  Filled only if \&quot;strike_type\&quot; is \&quot;custom\&quot;. | [optional] 
**event_ticker** | **str** | Unique identifier for events. | 
**expiration_time** | [**OutputTime**](OutputTime.md) |  | 
**expiration_value** | **str** | The value that was considered for the settlement. | 
**floor_strike** | [**Number**](Number.md) |  | [optional] 
**last_price** | [**Cent**](Cent.md) |  | 
**liquidity** | [**Cent**](Cent.md) |  | 
**no_ask** | [**Cent**](Cent.md) |  | 
**no_bid** | [**Cent**](Cent.md) |  | 
**open_interest** | **int** | Number of contracts bought on this market disconsidering netting. | 
**open_time** | [**OutputTime**](OutputTime.md) |  | 
**previous_price** | [**Cent**](Cent.md) |  | 
**previous_yes_ask** | [**Cent**](Cent.md) |  | 
**previous_yes_bid** | [**Cent**](Cent.md) |  | 
**result** | **str** | Settlement result for this market. | 
**risk_limit_cents** | [**Cent**](Cent.md) |  | 
**status** | **object** | Represents the current status of a market. | 
**strike_type** | **str** | Strike type defines how the market strike (expiration value) is defined and evaluated.  greater: It will be a single number. For YES outcome the expiration value should be greater than \&quot;floor_strike\&quot;.  greater_or_equal: It will be a single number. For YES outcome the expiration value should be greater than \&quot;floor_strike\&quot;.  less: It will be a single number. For YES outcome the expiration value should be less than \&quot;cap_strike\&quot;.  less_or_equal: It will be a single number. For YES outcome the expiration value should be less or equal than \&quot;cap_strike\&quot;.  between: It will be two numbers. For YES outcome the expiration value should be between inclusive \&quot;floor_strike\&quot; and \&quot;cap_strike\&quot;, that means expiration value needs to be greater or equal \&quot;floor_strike\&quot; and less or equal \&quot;cap_strike\&quot;.  custom: It will be one or more non-numerical values. For YES outcome the expiration values should be equal to the values in \&quot;custom_strike\&quot;. | [optional] 
**subtitle** | **str** | Shortened title for this market. | 
**ticker** | **str** | Unique identifier for markets. | 
**volume** | **int** | Number of contracts bought on this market. | 
**volume_24h** | **int** | Number of contracts bought on this market in the past day. | 
**yes_ask** | [**Cent**](Cent.md) |  | 
**yes_bid** | [**Cent**](Cent.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

