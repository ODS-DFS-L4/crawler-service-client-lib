# drone_distcat.AirwaysApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_airway_v1_api_aerial_corridors_airways_airway_id_put**](AirwaysApi.md#create_airway_v1_api_aerial_corridors_airways_airway_id_put) | **PUT** /v1/api/airways/{airway_id} | Create or update an airway by ID
[**delete_airway_v1_api_aerial_corridors_airways_airway_id_delete**](AirwaysApi.md#delete_airway_v1_api_aerial_corridors_airways_airway_id_delete) | **DELETE** /v1/api/airways/{airway_id} | Delete an airway by ID
[**get_single_airway_details_v1_api_aerial_corridors_airways_airway_id_get**](AirwaysApi.md#get_single_airway_details_v1_api_aerial_corridors_airways_airway_id_get) | **GET** /v1/api/airways/{airway_id} | Get details of a single airway by ID
[**search_for_airways_v1_api_aerial_corridors_airways_query_post**](AirwaysApi.md#search_for_airways_v1_api_aerial_corridors_airways_query_post) | **POST** /v1/api/airways/query | Query airways 


# **create_airway_v1_api_aerial_corridors_airways_airway_id_put**
> UpsertAirwayDefinitionResponsePublic create_airway_v1_api_aerial_corridors_airways_airway_id_put(airway_id, put_airway_definition_parameters)

Create or update an airway by ID

A new airway is created or an existing one is updated by providing the airway ID and the new airway definition, which includes the airway name, junctions, and sections. The operation is idempotent.

### Example


```python
import drone_distcat
from drone_distcat.models.put_airway_definition_parameters import PutAirwayDefinitionParameters
from drone_distcat.models.upsert_airway_definition_response_public import UpsertAirwayDefinitionResponsePublic
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
    api_instance = drone_distcat.AirwaysApi(api_client)
    airway_id = 'airway_id_example' # str | 
    put_airway_definition_parameters = drone_distcat.PutAirwayDefinitionParameters() # PutAirwayDefinitionParameters | 

    try:
        # Create or update an airway by ID
        api_response = api_instance.create_airway_v1_api_aerial_corridors_airways_airway_id_put(airway_id, put_airway_definition_parameters)
        print("The response of AirwaysApi->create_airway_v1_api_aerial_corridors_airways_airway_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AirwaysApi->create_airway_v1_api_aerial_corridors_airways_airway_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **airway_id** | **str**|  | 
 **put_airway_definition_parameters** | [**PutAirwayDefinitionParameters**](PutAirwayDefinitionParameters.md)|  | 

### Return type

[**UpsertAirwayDefinitionResponsePublic**](UpsertAirwayDefinitionResponsePublic.md)

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

# **delete_airway_v1_api_aerial_corridors_airways_airway_id_delete**
> DeleteAirwayDefinitionResponse delete_airway_v1_api_aerial_corridors_airways_airway_id_delete(airway_id)

Delete an airway by ID

Delete an airway from the ICDS by providing the airway ID.

### Example


```python
import drone_distcat
from drone_distcat.models.delete_airway_definition_response import DeleteAirwayDefinitionResponse
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
    api_instance = drone_distcat.AirwaysApi(api_client)
    airway_id = 'airway_id_example' # str | 

    try:
        # Delete an airway by ID
        api_response = api_instance.delete_airway_v1_api_aerial_corridors_airways_airway_id_delete(airway_id)
        print("The response of AirwaysApi->delete_airway_v1_api_aerial_corridors_airways_airway_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AirwaysApi->delete_airway_v1_api_aerial_corridors_airways_airway_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **airway_id** | **str**|  | 

### Return type

[**DeleteAirwayDefinitionResponse**](DeleteAirwayDefinitionResponse.md)

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

# **get_single_airway_details_v1_api_aerial_corridors_airways_airway_id_get**
> SingleAirwayDefinitionResponse get_single_airway_details_v1_api_aerial_corridors_airways_airway_id_get(airway_id)

Get details of a single airway by ID

Retrieve details of a specific airway by its ID.

### Example


```python
import drone_distcat
from drone_distcat.models.single_airway_definition_response import SingleAirwayDefinitionResponse
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
    api_instance = drone_distcat.AirwaysApi(api_client)
    airway_id = 'airway_id_example' # str | The ID of the airway to retrieve.

    try:
        # Get details of a single airway by ID
        api_response = api_instance.get_single_airway_details_v1_api_aerial_corridors_airways_airway_id_get(airway_id)
        print("The response of AirwaysApi->get_single_airway_details_v1_api_aerial_corridors_airways_airway_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AirwaysApi->get_single_airway_details_v1_api_aerial_corridors_airways_airway_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **airway_id** | **str**| The ID of the airway to retrieve. | 

### Return type

[**SingleAirwayDefinitionResponse**](SingleAirwayDefinitionResponse.md)

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

# **search_for_airways_v1_api_aerial_corridors_airways_query_post**
> List[QuerySingleAirwayDefinitionResponse] search_for_airways_v1_api_aerial_corridors_airways_query_post(query_airway_definition_parameters)

Query airways 

This endpoint allows querying section of airways based on the area of interest. Although it uses request.POST, no changes are made to the database. The POST method is used instead of GET because GET does not support passing body parameters for querying.

### Example


```python
import drone_distcat
from drone_distcat.models.query_airway_definition_parameters import QueryAirwayDefinitionParameters
from drone_distcat.models.query_single_airway_definition_response import QuerySingleAirwayDefinitionResponse
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
    api_instance = drone_distcat.AirwaysApi(api_client)
    query_airway_definition_parameters = drone_distcat.QueryAirwayDefinitionParameters() # QueryAirwayDefinitionParameters | 

    try:
        # Query airways 
        api_response = api_instance.search_for_airways_v1_api_aerial_corridors_airways_query_post(query_airway_definition_parameters)
        print("The response of AirwaysApi->search_for_airways_v1_api_aerial_corridors_airways_query_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AirwaysApi->search_for_airways_v1_api_aerial_corridors_airways_query_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_airway_definition_parameters** | [**QueryAirwayDefinitionParameters**](QueryAirwayDefinitionParameters.md)|  | 

### Return type

[**List[QuerySingleAirwayDefinitionResponse]**](QuerySingleAirwayDefinitionResponse.md)

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

