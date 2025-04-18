# QueryDronePortReferenceParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**area_of_interest** | [**AreaOfInterest**](AreaOfInterest.md) |  | 

## Example

```python
from drone_distcat.models.query_drone_port_reference_parameters import QueryDronePortReferenceParameters

# TODO update the JSON string below
json = "{}"
# create an instance of QueryDronePortReferenceParameters from a JSON string
query_drone_port_reference_parameters_instance = QueryDronePortReferenceParameters.from_json(json)
# print the JSON string representation of the object
print(QueryDronePortReferenceParameters.to_json())

# convert the object into a dict
query_drone_port_reference_parameters_dict = query_drone_port_reference_parameters_instance.to_dict()
# create an instance of QueryDronePortReferenceParameters from a dict
query_drone_port_reference_parameters_from_dict = QueryDronePortReferenceParameters.from_dict(query_drone_port_reference_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


