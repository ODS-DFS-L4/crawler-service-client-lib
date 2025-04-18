# PutAirwayDefinitionParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**airway** | [**AirwayInput**](AirwayInput.md) |  | 

## Example

```python
from drone_distcat.models.put_airway_definition_parameters import PutAirwayDefinitionParameters

# TODO update the JSON string below
json = "{}"
# create an instance of PutAirwayDefinitionParameters from a JSON string
put_airway_definition_parameters_instance = PutAirwayDefinitionParameters.from_json(json)
# print the JSON string representation of the object
print(PutAirwayDefinitionParameters.to_json())

# convert the object into a dict
put_airway_definition_parameters_dict = put_airway_definition_parameters_instance.to_dict()
# create an instance of PutAirwayDefinitionParameters from a dict
put_airway_definition_parameters_from_dict = PutAirwayDefinitionParameters.from_dict(put_airway_definition_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


