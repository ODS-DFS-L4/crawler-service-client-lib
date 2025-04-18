# AirwayJunctionDetailOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**airway** | [**AirwayGeometry**](AirwayGeometry.md) |  | 
**deviation** | [**Deviation**](Deviation.md) |  | 

## Example

```python
from drone_distcat.models.airway_junction_detail_output import AirwayJunctionDetailOutput

# TODO update the JSON string below
json = "{}"
# create an instance of AirwayJunctionDetailOutput from a JSON string
airway_junction_detail_output_instance = AirwayJunctionDetailOutput.from_json(json)
# print the JSON string representation of the object
print(AirwayJunctionDetailOutput.to_json())

# convert the object into a dict
airway_junction_detail_output_dict = airway_junction_detail_output_instance.to_dict()
# create an instance of AirwayJunctionDetailOutput from a dict
airway_junction_detail_output_from_dict = AirwayJunctionDetailOutput.from_dict(airway_junction_detail_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


