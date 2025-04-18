# DeleteAirwayDefinitionResponse

Delete Airway Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **int** |  | 
**message** | **str** |  | 

## Example

```python
from drone_distcat.models.delete_airway_definition_response import DeleteAirwayDefinitionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteAirwayDefinitionResponse from a JSON string
delete_airway_definition_response_instance = DeleteAirwayDefinitionResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteAirwayDefinitionResponse.to_json())

# convert the object into a dict
delete_airway_definition_response_dict = delete_airway_definition_response_instance.to_dict()
# create an instance of DeleteAirwayDefinitionResponse from a dict
delete_airway_definition_response_from_dict = DeleteAirwayDefinitionResponse.from_dict(delete_airway_definition_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


