import drone_distcat
from drone_distcat.models.create_or_update_drone_port_reference_response import CreateOrUpdateDronePortReferenceResponse
from drone_distcat.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = drone_distcat.Configuration(
    host = "http://10.0.7.127:8082"
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
