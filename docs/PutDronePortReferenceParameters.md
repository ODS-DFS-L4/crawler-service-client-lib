# PutDronePortReferenceParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**drone_port_details** | [**DronePortDetails**](DronePortDetails.md) |  | 

## Example

```python
from drone_distcat.models.put_drone_port_reference_parameters import PutDronePortReferenceParameters

# TODO update the JSON string below
json = "{}"
# create an instance of PutDronePortReferenceParameters from a JSON string
put_drone_port_reference_parameters_instance = PutDronePortReferenceParameters.from_json(json)
# print the JSON string representation of the object
print(PutDronePortReferenceParameters.to_json())

# convert the object into a dict
put_drone_port_reference_parameters_dict = put_drone_port_reference_parameters_instance.to_dict()
# create an instance of PutDronePortReferenceParameters from a dict
put_drone_port_reference_parameters_from_dict = PutDronePortReferenceParameters.from_dict(put_drone_port_reference_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


