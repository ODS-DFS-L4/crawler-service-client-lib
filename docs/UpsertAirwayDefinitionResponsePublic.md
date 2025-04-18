# UpsertAirwayDefinitionResponsePublic

A class to read data from the Airway table

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**airway** | [**AirwayOutput**](AirwayOutput.md) |  | 

## Example

```python
from drone_distcat.models.upsert_airway_definition_response_public import UpsertAirwayDefinitionResponsePublic

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertAirwayDefinitionResponsePublic from a JSON string
upsert_airway_definition_response_public_instance = UpsertAirwayDefinitionResponsePublic.from_json(json)
# print the JSON string representation of the object
print(UpsertAirwayDefinitionResponsePublic.to_json())

# convert the object into a dict
upsert_airway_definition_response_public_dict = upsert_airway_definition_response_public_instance.to_dict()
# create an instance of UpsertAirwayDefinitionResponsePublic from a dict
upsert_airway_definition_response_public_from_dict = UpsertAirwayDefinitionResponsePublic.from_dict(upsert_airway_definition_response_public_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


