# drone_distcat.CommonApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**read_version_availability_v1_api_version_availability_get**](CommonApi.md#read_version_availability_v1_api_version_availability_get) | **GET** /v1/api/version-availability | Read Version Availability


# **read_version_availability_v1_api_version_availability_get**
> VersionAvailabilityRead read_version_availability_v1_api_version_availability_get()

Read Version Availability

Get the status of the discovery service and software version.

### Example


```python
import drone_distcat
from drone_distcat.models.version_availability_read import VersionAvailabilityRead
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
    api_instance = drone_distcat.CommonApi(api_client)

    try:
        # Read Version Availability
        api_response = api_instance.read_version_availability_v1_api_version_availability_get()
        print("The response of CommonApi->read_version_availability_v1_api_version_availability_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommonApi->read_version_availability_v1_api_version_availability_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**VersionAvailabilityRead**](VersionAvailabilityRead.md)

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

