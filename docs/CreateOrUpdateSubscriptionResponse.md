# CreateOrUpdateSubscriptionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**subscription_details** | [**SubscriptionBase**](SubscriptionBase.md) |  | 

## Example

```python
from drone_distcat.models.create_or_update_subscription_response import CreateOrUpdateSubscriptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrUpdateSubscriptionResponse from a JSON string
create_or_update_subscription_response_instance = CreateOrUpdateSubscriptionResponse.from_json(json)
# print the JSON string representation of the object
print(CreateOrUpdateSubscriptionResponse.to_json())

# convert the object into a dict
create_or_update_subscription_response_dict = create_or_update_subscription_response_instance.to_dict()
# create an instance of CreateOrUpdateSubscriptionResponse from a dict
create_or_update_subscription_response_from_dict = CreateOrUpdateSubscriptionResponse.from_dict(create_or_update_subscription_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


