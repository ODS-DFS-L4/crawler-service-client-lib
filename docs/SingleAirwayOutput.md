# SingleAirwayOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**junctions** | [**List[AirwayJunctionOutput]**](AirwayJunctionOutput.md) |  | 
**sections** | [**List[AirwaySection]**](AirwaySection.md) |  | 

## Example

```python
from drone_distcat.models.single_airway_output import SingleAirwayOutput

# TODO update the JSON string below
json = "{}"
# create an instance of SingleAirwayOutput from a JSON string
single_airway_output_instance = SingleAirwayOutput.from_json(json)
# print the JSON string representation of the object
print(SingleAirwayOutput.to_json())

# convert the object into a dict
single_airway_output_dict = single_airway_output_instance.to_dict()
# create an instance of SingleAirwayOutput from a dict
single_airway_output_from_dict = SingleAirwayOutput.from_dict(single_airway_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


