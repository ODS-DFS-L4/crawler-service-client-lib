# drone_distcat.SubscriptionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_subscription_v1_api_managed_corridors_subscriptions_subscription_id_delete**](SubscriptionsApi.md#delete_subscription_v1_api_managed_corridors_subscriptions_subscription_id_delete) | **DELETE** /v1/api/subscriptions/{subscription_id} | Delete Subscription
[**get_subscription_v1_api_managed_corridors_subscriptions_subscription_id_get**](SubscriptionsApi.md#get_subscription_v1_api_managed_corridors_subscriptions_subscription_id_get) | **GET** /v1/api/subscriptions/{subscription_id} | Get Subscription details
[**search_subscriptions_v1_api_managed_corridors_subscriptions_query_post**](SubscriptionsApi.md#search_subscriptions_v1_api_managed_corridors_subscriptions_query_post) | **POST** /v1/api/subscriptions/query | Query Subscriptions
[**upsert_subscription_v1_api_managed_corridors_subscriptions_subscription_id_put**](SubscriptionsApi.md#upsert_subscription_v1_api_managed_corridors_subscriptions_subscription_id_put) | **PUT** /v1/api/subscriptions/{subscription_id} | Upsert Subscription


# **delete_subscription_v1_api_managed_corridors_subscriptions_subscription_id_delete**
> DeleteSubscriptionResponse delete_subscription_v1_api_managed_corridors_subscriptions_subscription_id_delete(subscription_id)

Delete Subscription

Delete a subscription by its ID.

### Example


```python
import drone_distcat
from drone_distcat.models.delete_subscription_response import DeleteSubscriptionResponse
from drone_distcat.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = drone_distcat.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with drone_distcat.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = drone_distcat.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 

    try:
        # Delete Subscription
        api_response = api_instance.delete_subscription_v1_api_managed_corridors_subscriptions_subscription_id_delete(subscription_id)
        print("The response of SubscriptionsApi->delete_subscription_v1_api_managed_corridors_subscriptions_subscription_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->delete_subscription_v1_api_managed_corridors_subscriptions_subscription_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

[**DeleteSubscriptionResponse**](DeleteSubscriptionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Operation not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription_v1_api_managed_corridors_subscriptions_subscription_id_get**
> CreateOrUpdateSubscriptionResponse get_subscription_v1_api_managed_corridors_subscriptions_subscription_id_get(subscription_id)

Get Subscription details

Retrieve details of a specific subscription by its ID.

### Example


```python
import drone_distcat
from drone_distcat.models.create_or_update_subscription_response import CreateOrUpdateSubscriptionResponse
from drone_distcat.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = drone_distcat.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with drone_distcat.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = drone_distcat.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | The ID of the subscription to retrieve.

    try:
        # Get Subscription details
        api_response = api_instance.get_subscription_v1_api_managed_corridors_subscriptions_subscription_id_get(subscription_id)
        print("The response of SubscriptionsApi->get_subscription_v1_api_managed_corridors_subscriptions_subscription_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->get_subscription_v1_api_managed_corridors_subscriptions_subscription_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| The ID of the subscription to retrieve. | 

### Return type

[**CreateOrUpdateSubscriptionResponse**](CreateOrUpdateSubscriptionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Operation not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_subscriptions_v1_api_managed_corridors_subscriptions_query_post**
> List[CreateOrUpdateSubscriptionResponse] search_subscriptions_v1_api_managed_corridors_subscriptions_query_post(query_subscription_parameters)

Query Subscriptions

Query subscriptions in an area of interest.

### Example


```python
import drone_distcat
from drone_distcat.models.create_or_update_subscription_response import CreateOrUpdateSubscriptionResponse
from drone_distcat.models.query_subscription_parameters import QuerySubscriptionParameters
from drone_distcat.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = drone_distcat.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with drone_distcat.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = drone_distcat.SubscriptionsApi(api_client)
    query_subscription_parameters = drone_distcat.QuerySubscriptionParameters() # QuerySubscriptionParameters | 

    try:
        # Query Subscriptions
        api_response = api_instance.search_subscriptions_v1_api_managed_corridors_subscriptions_query_post(query_subscription_parameters)
        print("The response of SubscriptionsApi->search_subscriptions_v1_api_managed_corridors_subscriptions_query_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->search_subscriptions_v1_api_managed_corridors_subscriptions_query_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_subscription_parameters** | [**QuerySubscriptionParameters**](QuerySubscriptionParameters.md)|  | 

### Return type

[**List[CreateOrUpdateSubscriptionResponse]**](CreateOrUpdateSubscriptionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**404** | Operation not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_subscription_v1_api_managed_corridors_subscriptions_subscription_id_put**
> CreateOrUpdateSubscriptionResponse upsert_subscription_v1_api_managed_corridors_subscriptions_subscription_id_put(subscription_id, put_subscription_parameters)

Upsert Subscription

Upsert a subscription. This endpoint creates a new subscription or updates an existing one based on the provided subscription ID.

### Example


```python
import drone_distcat
from drone_distcat.models.create_or_update_subscription_response import CreateOrUpdateSubscriptionResponse
from drone_distcat.models.put_subscription_parameters import PutSubscriptionParameters
from drone_distcat.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = drone_distcat.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with drone_distcat.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = drone_distcat.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 
    put_subscription_parameters = drone_distcat.PutSubscriptionParameters() # PutSubscriptionParameters | 

    try:
        # Upsert Subscription
        api_response = api_instance.upsert_subscription_v1_api_managed_corridors_subscriptions_subscription_id_put(subscription_id, put_subscription_parameters)
        print("The response of SubscriptionsApi->upsert_subscription_v1_api_managed_corridors_subscriptions_subscription_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->upsert_subscription_v1_api_managed_corridors_subscriptions_subscription_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **put_subscription_parameters** | [**PutSubscriptionParameters**](PutSubscriptionParameters.md)|  | 

### Return type

[**CreateOrUpdateSubscriptionResponse**](CreateOrUpdateSubscriptionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Operation not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

