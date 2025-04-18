# AirwayJunctionDetailInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**airway** | [**AirwayGeometry**](AirwayGeometry.md) |  | 
**deviation** | [**Deviation**](Deviation.md) |  | 

## Example

```python
from drone_distcat.models.airway_junction_detail_input import AirwayJunctionDetailInput

# TODO update the JSON string below
json = "{}"
# create an instance of AirwayJunctionDetailInput from a JSON string
airway_junction_detail_input_instance = AirwayJunctionDetailInput.from_json(json)
# print the JSON string representation of the object
print(AirwayJunctionDetailInput.to_json())

# convert the object into a dict
airway_junction_detail_input_dict = airway_junction_detail_input_instance.to_dict()
# create an instance of AirwayJunctionDetailInput from a dict
airway_junction_detail_input_from_dict = AirwayJunctionDetailInput.from_dict(airway_junction_detail_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


