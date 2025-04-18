# AirwayJunctionInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**type** | **str** |  | 
**airways** | [**List[AirwayJunctionDetailInput]**](AirwayJunctionDetailInput.md) |  | 

## Example

```python
from drone_distcat.models.airway_junction_input import AirwayJunctionInput

# TODO update the JSON string below
json = "{}"
# create an instance of AirwayJunctionInput from a JSON string
airway_junction_input_instance = AirwayJunctionInput.from_json(json)
# print the JSON string representation of the object
print(AirwayJunctionInput.to_json())

# convert the object into a dict
airway_junction_input_dict = airway_junction_input_instance.to_dict()
# create an instance of AirwayJunctionInput from a dict
airway_junction_input_from_dict = AirwayJunctionInput.from_dict(airway_junction_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


