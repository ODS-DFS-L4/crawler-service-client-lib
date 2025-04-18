# VersionAvailabilityRead

A class to hold version and availability of ICDS

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | 
**availability** | [**AvailabilityEnum**](AvailabilityEnum.md) |  | 

## Example

```python
from drone_distcat.models.version_availability_read import VersionAvailabilityRead

# TODO update the JSON string below
json = "{}"
# create an instance of VersionAvailabilityRead from a JSON string
version_availability_read_instance = VersionAvailabilityRead.from_json(json)
# print the JSON string representation of the object
print(VersionAvailabilityRead.to_json())

# convert the object into a dict
version_availability_read_dict = version_availability_read_instance.to_dict()
# create an instance of VersionAvailabilityRead from a dict
version_availability_read_from_dict = VersionAvailabilityRead.from_dict(version_availability_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


