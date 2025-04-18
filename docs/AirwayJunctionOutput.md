# AirwayJunctionOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**type** | **str** |  | 
**airways** | [**List[AirwayJunctionDetailOutput]**](AirwayJunctionDetailOutput.md) |  | 

## Example

```python
from drone_distcat.models.airway_junction_output import AirwayJunctionOutput

# TODO update the JSON string below
json = "{}"
# create an instance of AirwayJunctionOutput from a JSON string
airway_junction_output_instance = AirwayJunctionOutput.from_json(json)
# print the JSON string representation of the object
print(AirwayJunctionOutput.to_json())

# convert the object into a dict
airway_junction_output_dict = airway_junction_output_instance.to_dict()
# create an instance of AirwayJunctionOutput from a dict
airway_junction_output_from_dict = AirwayJunctionOutput.from_dict(airway_junction_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


