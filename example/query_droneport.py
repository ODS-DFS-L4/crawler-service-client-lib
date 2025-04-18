import drone_distcat
from drone_distcat.models.query_drone_port_reference_parameters import QueryDronePortReferenceParameters
from drone_distcat.models.query_drone_port_reference_response import QueryDronePortReferenceResponse
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
    query_drone_port_reference_parameters = drone_distcat.QueryDronePortReferenceParameters(
        area_of_interest = drone_distcat.models.area_of_interest.AreaOfInterest(
            outline_polygon = drone_distcat.models.b_box_definition.BBoxDefinition(
                min_latitude = -90,
                min_longitude = -180,
                max_latitude = -90,
                max_longitude = -180, ), )
    )
    supports_drone_type = 'supports_drone_type_example' # str |  (optional)
    usage_type = 56 # int |  (optional)
    port_type = 56 # int |  (optional)
    manufacturer = 'manufacturer_example' # str |  (optional)

    try:
        # Query Drone ports
        api_response = api_instance.search_drone_ports_v1_api_managed_corridors_ports_query_post(query_drone_port_reference_parameters, supports_drone_type=supports_drone_type, usage_type=usage_type, port_type=port_type, manufacturer=manufacturer)
        print("The response of DronePortsApi->search_drone_ports_v1_api_managed_corridors_ports_query_post:\n")
        pprint(api_response)
        pprint(api_response[0].to_dict())
    except Exception as e:
        print("Exception when calling DronePortsApi->search_drone_ports_v1_api_managed_corridors_ports_query_post: %s\n" % e)
