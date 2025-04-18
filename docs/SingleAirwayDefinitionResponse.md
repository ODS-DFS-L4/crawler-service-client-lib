# SingleAirwayDefinitionResponse

Put airways definition parameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**airway** | [**AirwayOutput**](AirwayOutput.md) |  | 

## Example

```python
from drone_distcat.models.single_airway_definition_response import SingleAirwayDefinitionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleAirwayDefinitionResponse from a JSON string
single_airway_definition_response_instance = SingleAirwayDefinitionResponse.from_json(json)
# print the JSON string representation of the object
print(SingleAirwayDefinitionResponse.to_json())

# convert the object into a dict
single_airway_definition_response_dict = single_airway_definition_response_instance.to_dict()
# create an instance of SingleAirwayDefinitionResponse from a dict
single_airway_definition_response_from_dict = SingleAirwayDefinitionResponse.from_dict(single_airway_definition_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


