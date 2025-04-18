# AreaOfInterest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**outline_polygon** | [**BBoxDefinition**](BBoxDefinition.md) |  | 

## Example

```python
from drone_distcat.models.area_of_interest import AreaOfInterest

# TODO update the JSON string below
json = "{}"
# create an instance of AreaOfInterest from a JSON string
area_of_interest_instance = AreaOfInterest.from_json(json)
# print the JSON string representation of the object
print(AreaOfInterest.to_json())

# convert the object into a dict
area_of_interest_dict = area_of_interest_instance.to_dict()
# create an instance of AreaOfInterest from a dict
area_of_interest_from_dict = AreaOfInterest.from_dict(area_of_interest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


