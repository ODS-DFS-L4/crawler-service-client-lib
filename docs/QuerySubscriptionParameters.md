# QuerySubscriptionParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**area_of_interest** | [**AreaOfInterest**](AreaOfInterest.md) |  | 

## Example

```python
from drone_distcat.models.query_subscription_parameters import QuerySubscriptionParameters

# TODO update the JSON string below
json = "{}"
# create an instance of QuerySubscriptionParameters from a JSON string
query_subscription_parameters_instance = QuerySubscriptionParameters.from_json(json)
# print the JSON string representation of the object
print(QuerySubscriptionParameters.to_json())

# convert the object into a dict
query_subscription_parameters_dict = query_subscription_parameters_instance.to_dict()
# create an instance of QuerySubscriptionParameters from a dict
query_subscription_parameters_from_dict = QuerySubscriptionParameters.from_dict(query_subscription_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


