# DeleteDronePortReferenceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **int** |  | 
**message** | **str** |  | 

## Example

```python
from drone_distcat.models.delete_drone_port_reference_response import DeleteDronePortReferenceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteDronePortReferenceResponse from a JSON string
delete_drone_port_reference_response_instance = DeleteDronePortReferenceResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteDronePortReferenceResponse.to_json())

# convert the object into a dict
delete_drone_port_reference_response_dict = delete_drone_port_reference_response_instance.to_dict()
# create an instance of DeleteDronePortReferenceResponse from a dict
delete_drone_port_reference_response_from_dict = DeleteDronePortReferenceResponse.from_dict(delete_drone_port_reference_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


