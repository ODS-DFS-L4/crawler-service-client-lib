# drone_distcat.DronePortsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_drone_port_reference_v1_api_managed_corridors_ports_port_id_delete**](DronePortsApi.md#delete_drone_port_reference_v1_api_managed_corridors_ports_port_id_delete) | **DELETE** /v1/api/ports/{port_id} | Delete Drone Port Reference
[**get_drone_port_details_v1_api_managed_corridors_ports_port_id_get**](DronePortsApi.md#get_drone_port_details_v1_api_managed_corridors_ports_port_id_get) | **GET** /v1/api/ports/{port_id} | Get drone port reference details
[**search_drone_ports_v1_api_managed_corridors_ports_query_post**](DronePortsApi.md#search_drone_ports_v1_api_managed_corridors_ports_query_post) | **POST** /v1/api/ports/query | Query Drone ports
[**upsert_drone_port_reference_v1_api_managed_corridors_ports_port_id_put**](DronePortsApi.md#upsert_drone_port_reference_v1_api_managed_corridors_ports_port_id_put) | **PUT** /v1/api/ports/{port_id} | Upsert Drone Port Reference


# **delete_drone_port_reference_v1_api_managed_corridors_ports_port_id_delete**
> DeleteDronePortReferenceResponse delete_drone_port_reference_v1_api_managed_corridors_ports_port_id_delete(port_id)

Delete Drone Port Reference

Deletes a drone port reference by its port ID.

### Example


```python
import drone_distcat
from drone_distcat.models.delete_drone_port_reference_response import DeleteDronePortReferenceResponse
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
    api_instance = drone_distcat.DronePortsApi(api_client)
    port_id = 'port_id_example' # str | 

    try:
        # Delete Drone Port Reference
        api_response = api_instance.delete_drone_port_reference_v1_api_managed_corridors_ports_port_id_delete(port_id)
        print("The response of DronePortsApi->delete_drone_port_reference_v1_api_managed_corridors_ports_port_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DronePortsApi->delete_drone_port_reference_v1_api_managed_corridors_ports_port_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **port_id** | **str**|  | 

### Return type

[**DeleteDronePortReferenceResponse**](DeleteDronePortReferenceResponse.md)

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

# **get_drone_port_details_v1_api_managed_corridors_ports_port_id_get**
> CreateOrUpdateDronePortReferenceResponse get_drone_port_details_v1_api_managed_corridors_ports_port_id_get(port_id)

Get drone port reference details

Retrieve details of a specific drone port by its ID.

### Example


```python
import drone_distcat
from drone_distcat.models.create_or_update_drone_port_reference_response import CreateOrUpdateDronePortReferenceResponse
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
    api_instance = drone_distcat.DronePortsApi(api_client)
    port_id = 'port_id_example' # str | The ID of the drone port to retrieve.

    try:
        # Get drone port reference details
        api_response = api_instance.get_drone_port_details_v1_api_managed_corridors_ports_port_id_get(port_id)
        print("The response of DronePortsApi->get_drone_port_details_v1_api_managed_corridors_ports_port_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DronePortsApi->get_drone_port_details_v1_api_managed_corridors_ports_port_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **port_id** | **str**| The ID of the drone port to retrieve. | 

### Return type

[**CreateOrUpdateDronePortReferenceResponse**](CreateOrUpdateDronePortReferenceResponse.md)

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

# **search_drone_ports_v1_api_managed_corridors_ports_query_post**
> List[QueryDronePortReferenceResponse] search_drone_ports_v1_api_managed_corridors_ports_query_post(query_drone_port_reference_parameters, supports_drone_type=supports_drone_type, usage_type=usage_type, port_type=port_type, manufacturer=manufacturer)

Query Drone ports

Query all the drone ports in an area of interest.

### Example


```python
import drone_distcat
from drone_distcat.models.query_drone_port_reference_parameters import QueryDronePortReferenceParameters
from drone_distcat.models.query_drone_port_reference_response import QueryDronePortReferenceResponse
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
    api_instance = drone_distcat.DronePortsApi(api_client)
    query_drone_port_reference_parameters = drone_distcat.QueryDronePortReferenceParameters() # QueryDronePortReferenceParameters | 
    supports_drone_type = 'supports_drone_type_example' # str |  (optional)
    usage_type = 56 # int |  (optional)
    port_type = 56 # int |  (optional)
    manufacturer = 'manufacturer_example' # str |  (optional)

    try:
        # Query Drone ports
        api_response = api_instance.search_drone_ports_v1_api_managed_corridors_ports_query_post(query_drone_port_reference_parameters, supports_drone_type=supports_drone_type, usage_type=usage_type, port_type=port_type, manufacturer=manufacturer)
        print("The response of DronePortsApi->search_drone_ports_v1_api_managed_corridors_ports_query_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DronePortsApi->search_drone_ports_v1_api_managed_corridors_ports_query_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_drone_port_reference_parameters** | [**QueryDronePortReferenceParameters**](QueryDronePortReferenceParameters.md)|  | 
 **supports_drone_type** | **str**|  | [optional] 
 **usage_type** | **int**|  | [optional] 
 **port_type** | **int**|  | [optional] 
 **manufacturer** | **str**|  | [optional] 

### Return type

[**List[QueryDronePortReferenceResponse]**](QueryDronePortReferenceResponse.md)

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

# **upsert_drone_port_reference_v1_api_managed_corridors_ports_port_id_put**
> CreateOrUpdateDronePortReferenceResponse upsert_drone_port_reference_v1_api_managed_corridors_ports_port_id_put(port_id, put_drone_port_reference_parameters)

Upsert Drone Port Reference

Upsert (update or insert) a drone port reference. This function handles the creation or updating of a drone port reference based on the provided payload and port ID. If the drone port is created, the response status code is set to 201.

### Example


```python
import drone_distcat
from drone_distcat.models.create_or_update_drone_port_reference_response import CreateOrUpdateDronePortReferenceResponse
from drone_distcat.models.put_drone_port_reference_parameters import PutDronePortReferenceParameters
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
    api_instance = drone_distcat.DronePortsApi(api_client)
    port_id = 'port_id_example' # str | 
    put_drone_port_reference_parameters = drone_distcat.PutDronePortReferenceParameters() # PutDronePortReferenceParameters | 

    try:
        # Upsert Drone Port Reference
        api_response = api_instance.upsert_drone_port_reference_v1_api_managed_corridors_ports_port_id_put(port_id, put_drone_port_reference_parameters)
        print("The response of DronePortsApi->upsert_drone_port_reference_v1_api_managed_corridors_ports_port_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DronePortsApi->upsert_drone_port_reference_v1_api_managed_corridors_ports_port_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **port_id** | **str**|  | 
 **put_drone_port_reference_parameters** | [**PutDronePortReferenceParameters**](PutDronePortReferenceParameters.md)|  | 

### Return type

[**CreateOrUpdateDronePortReferenceResponse**](CreateOrUpdateDronePortReferenceResponse.md)

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

