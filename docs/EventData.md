# EventData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | Event category. | 
**event_ticker** | **str** | Unique identifier for events. | 
**mutually_exclusive** | **bool** | If true then the event is mutually exclusive. | 
**series_ticker** | **str** | Unique identifier for series. | 
**strike_date** | [**OutputTime**](OutputTime.md) |  | [optional] 
**strike_period** | **str** | The strike period for this event. This will be filled when the event strike is not a date. If it is a date then the &#x27;strike_date&#x27; field should be filled instead. | [optional] 
**sub_title** | **str** | Shortened title. | 
**title** | **str** | Event title. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

