import drone_distcat
from drone_distcat.models.create_or_update_drone_port_reference_response import CreateOrUpdateDronePortReferenceResponse
from drone_distcat.models.put_drone_port_reference_parameters import PutDronePortReferenceParameters
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
    port_id = 'port_id_example' # str | 
    put_drone_port_reference_parameters = drone_distcat.models.PutDronePortReferenceParameters(
        drone_port_details = drone_distcat.models.drone_port_details.DronePortDetails(
            manufacturer = '0',
            port_type = 1,
            latitude = 35.12345678,
            longitude = 140.12345678,
            altitude = 12,
            supports_drone_type = 'マルチコプター',
            usage_type = 1,
            url = 'https://example.com/droneport1', ))

    try:
        # Upsert Drone Port Reference
        api_response = api_instance.upsert_drone_port_reference_v1_api_managed_corridors_ports_port_id_put(port_id, put_drone_port_reference_parameters)
        print("The response of DronePortsApi->upsert_drone_port_reference_v1_api_managed_corridors_ports_port_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DronePortsApi->upsert_drone_port_reference_v1_api_managed_corridors_ports_port_id_put: %s\n" % e)
