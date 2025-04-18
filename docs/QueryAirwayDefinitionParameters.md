# QueryAirwayDefinitionParameters

Query all Airway Definitions for an area of interest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**area_of_interest** | [**AreaOfInterest**](AreaOfInterest.md) |  | 

## Example

```python
from drone_distcat.models.query_airway_definition_parameters import QueryAirwayDefinitionParameters

# TODO update the JSON string below
json = "{}"
# create an instance of QueryAirwayDefinitionParameters from a JSON string
query_airway_definition_parameters_instance = QueryAirwayDefinitionParameters.from_json(json)
# print the JSON string representation of the object
print(QueryAirwayDefinitionParameters.to_json())

# convert the object into a dict
query_airway_definition_parameters_dict = query_airway_definition_parameters_instance.to_dict()
# create an instance of QueryAirwayDefinitionParameters from a dict
query_airway_definition_parameters_from_dict = QueryAirwayDefinitionParameters.from_dict(query_airway_definition_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


