# SingleDiscoveryServiceDetail

A class to hold a list of URLs and the type of service and regions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**domain** | **str** |  | 

## Example

```python
from drone_distcat.models.single_discovery_service_detail import SingleDiscoveryServiceDetail

# TODO update the JSON string below
json = "{}"
# create an instance of SingleDiscoveryServiceDetail from a JSON string
single_discovery_service_detail_instance = SingleDiscoveryServiceDetail.from_json(json)
# print the JSON string representation of the object
print(SingleDiscoveryServiceDetail.to_json())

# convert the object into a dict
single_discovery_service_detail_dict = single_discovery_service_detail_instance.to_dict()
# create an instance of SingleDiscoveryServiceDetail from a dict
single_discovery_service_detail_from_dict = SingleDiscoveryServiceDetail.from_dict(single_discovery_service_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


