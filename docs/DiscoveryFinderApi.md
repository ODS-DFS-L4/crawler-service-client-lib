# drone_distcat.DiscoveryFinderApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_discovery_service_v1_api_discovery_finder_discovery_services_post**](DiscoveryFinderApi.md#create_discovery_service_v1_api_discovery_finder_discovery_services_post) | **POST** /v1/api/discovery-finder/discovery-services | Create a new discovery service URL
[**delete_discovery_service_v1_api_discovery_finder_discovery_services_url_id_delete**](DiscoveryFinderApi.md#delete_discovery_service_v1_api_discovery_finder_discovery_services_url_id_delete) | **DELETE** /v1/api/discovery-finder/discovery-services/{url_id} | Delete Discovery Service
[**get_discovery_services_v1_api_discovery_finder_discovery_services_get**](DiscoveryFinderApi.md#get_discovery_services_v1_api_discovery_finder_discovery_services_get) | **GET** /v1/api/discovery-finder/discovery-services/{url_id} | Get Discovery Services


# **create_discovery_service_v1_api_discovery_finder_discovery_services_post**
> SingleDiscoveryServiceDetail create_discovery_service_v1_api_discovery_finder_discovery_services_post(single_discovery_service_detail)

Create a new discovery service URL

Create a new discovery service url with details like region and application type.

### Example


```python
import drone_distcat
from drone_distcat.models.single_discovery_service_detail import SingleDiscoveryServiceDetail
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
    api_instance = drone_distcat.DiscoveryFinderApi(api_client)
    single_discovery_service_detail = drone_distcat.SingleDiscoveryServiceDetail() # SingleDiscoveryServiceDetail | 

    try:
        # Create a new discovery service URL
        api_response = api_instance.create_discovery_service_v1_api_discovery_finder_discovery_services_post(single_discovery_service_detail)
        print("The response of DiscoveryFinderApi->create_discovery_service_v1_api_discovery_finder_discovery_services_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscoveryFinderApi->create_discovery_service_v1_api_discovery_finder_discovery_services_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **single_discovery_service_detail** | [**SingleDiscoveryServiceDetail**](SingleDiscoveryServiceDetail.md)|  | 

### Return type

[**SingleDiscoveryServiceDetail**](SingleDiscoveryServiceDetail.md)

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

# **delete_discovery_service_v1_api_discovery_finder_discovery_services_url_id_delete**
> object delete_discovery_service_v1_api_discovery_finder_discovery_services_url_id_delete(url_id)

Delete Discovery Service

Deletes a discovery service URL from the database. This asynchronous function removes a discovery service URL from the database session provided.  Args:     db_session (DBSessionDep): The database session dependency.     url_id (int): The ID of the discovery service URL to be deleted.  Returns:     dict: A dictionary containing the status of the deletion operation.

### Example


```python
import drone_distcat
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
    api_instance = drone_distcat.DiscoveryFinderApi(api_client)
    url_id = 'url_id_example' # str | 

    try:
        # Delete Discovery Service
        api_response = api_instance.delete_discovery_service_v1_api_discovery_finder_discovery_services_url_id_delete(url_id)
        print("The response of DiscoveryFinderApi->delete_discovery_service_v1_api_discovery_finder_discovery_services_url_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscoveryFinderApi->delete_discovery_service_v1_api_discovery_finder_discovery_services_url_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url_id** | **str**|  | 

### Return type

**object**

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

# **get_discovery_services_v1_api_discovery_finder_discovery_services_get**
> DiscoveryServiceListRead get_discovery_services_v1_api_discovery_finder_discovery_services_get(url_id)

Get Discovery Services

Fetches discovery service URLs from the database. This asynchronous function retrieves a list of discovery service URLs from the database session provided.  Returns:     list: A list of discovery service URLs and their details.

### Example


```python
import drone_distcat
from drone_distcat.models.discovery_service_list_read import DiscoveryServiceListRead
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
    api_instance = drone_distcat.DiscoveryFinderApi(api_client)
    url_id = 'url_id_example' # str | 

    try:
        # Get Discovery Services
        api_response = api_instance.get_discovery_services_v1_api_discovery_finder_discovery_services_get(url_id)
        print("The response of DiscoveryFinderApi->get_discovery_services_v1_api_discovery_finder_discovery_services_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscoveryFinderApi->get_discovery_services_v1_api_discovery_finder_discovery_services_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url_id** | **str**|  | 

### Return type

[**DiscoveryServiceListRead**](DiscoveryServiceListRead.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

