# SingleAirwayInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**junctions** | [**List[AirwayJunctionInput]**](AirwayJunctionInput.md) |  | 
**sections** | [**List[AirwaySection]**](AirwaySection.md) |  | 

## Example

```python
from drone_distcat.models.single_airway_input import SingleAirwayInput

# TODO update the JSON string below
json = "{}"
# create an instance of SingleAirwayInput from a JSON string
single_airway_input_instance = SingleAirwayInput.from_json(json)
# print the JSON string representation of the object
print(SingleAirwayInput.to_json())

# convert the object into a dict
single_airway_input_dict = single_airway_input_instance.to_dict()
# create an instance of SingleAirwayInput from a dict
single_airway_input_from_dict = SingleAirwayInput.from_dict(single_airway_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


