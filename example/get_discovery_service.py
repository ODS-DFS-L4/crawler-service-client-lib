import drone_distcat
from drone_distcat.models.discovery_service_list_read import DiscoveryServiceListRead
from drone_distcat.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = drone_distcat.Configuration(
    host = "http://10.0.10.62:8081"
)


# Enter a context with an instance of the API client
with drone_distcat.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = drone_distcat.DiscoveryFinderApi(api_client)
    url_id = 'discoveryservice' # str | 

    try:
        # Get Discovery Services
        api_response = api_instance.get_discovery_services_v1_api_discovery_finder_discovery_services_get(url_id)
        print("The response of DiscoveryFinderApi->get_discovery_services_v1_api_discovery_finder_discovery_services_get:\n")
        pprint(api_response)
        pprint(api_response.to_dict())
    except Exception as e:
        print("Exception when calling DiscoveryFinderApi->get_discovery_services_v1_api_discovery_finder_discovery_services_get: %s\n" % e)
