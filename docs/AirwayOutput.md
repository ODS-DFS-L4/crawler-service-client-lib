# AirwayOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**administrator_id** | **str** |  | 
**business_number** | **int** |  | 
**airways** | [**List[SingleAirwayOutput]**](SingleAirwayOutput.md) |  | 
**url** | **str** |  | 

## Example

```python
from drone_distcat.models.airway_output import AirwayOutput

# TODO update the JSON string below
json = "{}"
# create an instance of AirwayOutput from a JSON string
airway_output_instance = AirwayOutput.from_json(json)
# print the JSON string representation of the object
print(AirwayOutput.to_json())

# convert the object into a dict
airway_output_dict = airway_output_instance.to_dict()
# create an instance of AirwayOutput from a dict
airway_output_from_dict = AirwayOutput.from_dict(airway_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


