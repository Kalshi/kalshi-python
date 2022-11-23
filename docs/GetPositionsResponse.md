# GetPositionsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cursor** | **str** | The Cursor represents a pointer to the next page of records in the pagination. Use the value returned here in the cursor query parameter for this end-point to get the next page containing limit records. An empty value of this field indicates there is no next page. | [optional] 
**event_positions** | [**list[EventPosition]**](EventPosition.md) | List of event positions. | 
**market_positions** | [**list[MarketPosition]**](MarketPosition.md) | List of market positions. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

