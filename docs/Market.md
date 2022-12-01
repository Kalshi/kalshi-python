# Market

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_close_early** | **bool** | If true then this market can close earlier then the time provided on close_time. | 
**category** | **str** | Category for this market. | 
**close_time** | [**OutputTime**](OutputTime.md) |  | 
**event_ticker** | **str** | Unique identifier for events. | 
**expiration_time** | [**OutputTime**](OutputTime.md) |  | 
**expiration_value** | **str** | The value that was considered for the settlement. | 
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
**subtitle** | **str** | Shortened title for this market. | 
**ticker** | **str** | Unique identifier for markets. | 
**volume** | **int** | Number of contracts bought on this market. | 
**volume_24h** | **int** | Number of contracts bought on this market in the past day. | 
**yes_ask** | [**Cent**](Cent.md) |  | 
**yes_bid** | [**Cent**](Cent.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

