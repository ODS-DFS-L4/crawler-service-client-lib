# DiscoveryServiceListRead

A class to hold a list of URLs and the type of service

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_services** | [**List[SingleDiscoveryServiceDetail]**](SingleDiscoveryServiceDetail.md) |  | 

## Example

```python
from drone_distcat.models.discovery_service_list_read import DiscoveryServiceListRead

# TODO update the JSON string below
json = "{}"
# create an instance of DiscoveryServiceListRead from a JSON string
discovery_service_list_read_instance = DiscoveryServiceListRead.from_json(json)
# print the JSON string representation of the object
print(DiscoveryServiceListRead.to_json())

# convert the object into a dict
discovery_service_list_read_dict = discovery_service_list_read_instance.to_dict()
# create an instance of DiscoveryServiceListRead from a dict
discovery_service_list_read_from_dict = DiscoveryServiceListRead.from_dict(discovery_service_list_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


