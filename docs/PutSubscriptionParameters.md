# PutSubscriptionParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**area_of_interest** | [**AreaOfInterest**](AreaOfInterest.md) |  | 
**time_start** | **datetime** |  | 
**time_end** | **datetime** |  | 
**sp_base_url** | **str** |  | 

## Example

```python
from drone_distcat.models.put_subscription_parameters import PutSubscriptionParameters

# TODO update the JSON string below
json = "{}"
# create an instance of PutSubscriptionParameters from a JSON string
put_subscription_parameters_instance = PutSubscriptionParameters.from_json(json)
# print the JSON string representation of the object
print(PutSubscriptionParameters.to_json())

# convert the object into a dict
put_subscription_parameters_dict = put_subscription_parameters_instance.to_dict()
# create an instance of PutSubscriptionParameters from a dict
put_subscription_parameters_from_dict = PutSubscriptionParameters.from_dict(put_subscription_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


