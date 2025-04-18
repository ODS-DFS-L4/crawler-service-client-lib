# AirwayGeometry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geometry** | [**Geometry**](Geometry.md) |  | 

## Example

```python
from drone_distcat.models.airway_geometry import AirwayGeometry

# TODO update the JSON string below
json = "{}"
# create an instance of AirwayGeometry from a JSON string
airway_geometry_instance = AirwayGeometry.from_json(json)
# print the JSON string representation of the object
print(AirwayGeometry.to_json())

# convert the object into a dict
airway_geometry_dict = airway_geometry_instance.to_dict()
# create an instance of AirwayGeometry from a dict
airway_geometry_from_dict = AirwayGeometry.from_dict(airway_geometry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


