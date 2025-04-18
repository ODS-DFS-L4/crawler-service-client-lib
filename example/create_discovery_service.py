import drone_distcat
from drone_distcat.models.single_discovery_service_detail import SingleDiscoveryServiceDetail
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
    single_discovery_service_detail = drone_distcat.SingleDiscoveryServiceDetail(
		url="https://www.example.com", domain="example.com") # SingleDiscoveryServiceDetail | 

    try:
        # Create a new discovery service URL
        api_response = api_instance.create_discovery_service_v1_api_discovery_finder_discovery_services_post(single_discovery_service_detail)
        print("The response of DiscoveryFinderApi->create_discovery_service_v1_api_discovery_finder_discovery_services_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscoveryFinderApi->create_discovery_service_v1_api_discovery_finder_discovery_services_post: %s\n" % e)
