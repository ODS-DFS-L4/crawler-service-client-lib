# BBoxDefinition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_latitude** | **float** |  | 
**min_longitude** | **float** |  | 
**max_latitude** | **float** |  | 
**max_longitude** | **float** |  | 

## Example

```python
from drone_distcat.models.b_box_definition import BBoxDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of BBoxDefinition from a JSON string
b_box_definition_instance = BBoxDefinition.from_json(json)
# print the JSON string representation of the object
print(BBoxDefinition.to_json())

# convert the object into a dict
b_box_definition_dict = b_box_definition_instance.to_dict()
# create an instance of BBoxDefinition from a dict
b_box_definition_from_dict = BBoxDefinition.from_dict(b_box_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


