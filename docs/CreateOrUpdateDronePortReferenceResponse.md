# CreateOrUpdateDronePortReferenceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**drone_port_details** | [**DronePortDetails**](DronePortDetails.md) |  | 

## Example

```python
from drone_distcat.models.create_or_update_drone_port_reference_response import CreateOrUpdateDronePortReferenceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrUpdateDronePortReferenceResponse from a JSON string
create_or_update_drone_port_reference_response_instance = CreateOrUpdateDronePortReferenceResponse.from_json(json)
# print the JSON string representation of the object
print(CreateOrUpdateDronePortReferenceResponse.to_json())

# convert the object into a dict
create_or_update_drone_port_reference_response_dict = create_or_update_drone_port_reference_response_instance.to_dict()
# create an instance of CreateOrUpdateDronePortReferenceResponse from a dict
create_or_update_drone_port_reference_response_from_dict = CreateOrUpdateDronePortReferenceResponse.from_dict(create_or_update_drone_port_reference_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


