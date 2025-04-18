# SubscriptionBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | 
**notification_index** | **int** |  | 
**sp_base_url** | **str** |  | 
**time_start** | **datetime** |  | 
**time_end** | **datetime** |  | 

## Example

```python
from drone_distcat.models.subscription_base import SubscriptionBase

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionBase from a JSON string
subscription_base_instance = SubscriptionBase.from_json(json)
# print the JSON string representation of the object
print(SubscriptionBase.to_json())

# convert the object into a dict
subscription_base_dict = subscription_base_instance.to_dict()
# create an instance of SubscriptionBase from a dict
subscription_base_from_dict = SubscriptionBase.from_dict(subscription_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


