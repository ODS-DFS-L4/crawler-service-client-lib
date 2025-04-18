# AirwaySection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**airway_point_ids** | **List[str]** |  | 

## Example

```python
from drone_distcat.models.airway_section import AirwaySection

# TODO update the JSON string below
json = "{}"
# create an instance of AirwaySection from a JSON string
airway_section_instance = AirwaySection.from_json(json)
# print the JSON string representation of the object
print(AirwaySection.to_json())

# convert the object into a dict
airway_section_dict = airway_section_instance.to_dict()
# create an instance of AirwaySection from a dict
airway_section_from_dict = AirwaySection.from_dict(airway_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


