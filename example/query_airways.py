import drone_distcat
from drone_distcat.models.query_airway_definition_parameters import QueryAirwayDefinitionParameters
from drone_distcat.models.query_single_airway_definition_response import QuerySingleAirwayDefinitionResponse
from drone_distcat.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = drone_distcat.Configuration(
    host = "http://localhost:8082"
)


# Enter a context with an instance of the API client
with drone_distcat.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = drone_distcat.AirwaysApi(api_client)
    query_airway_definition_parameters = drone_distcat.QueryAirwayDefinitionParameters(
        area_of_interest = drone_distcat.models.area_of_interest.AreaOfInterest(
            outline_polygon = drone_distcat.models.b_box_definition.BBoxDefinition(
                min_latitude = -90,
                min_longitude = -180,
                max_latitude = -90,
                max_longitude = -180, ), )
    )

    try:
        # Query airways 
        api_response = api_instance.search_for_airways_v1_api_aerial_corridors_airways_query_post(query_airway_definition_parameters)
        print("The response of AirwaysApi->search_for_airways_v1_api_aerial_corridors_airways_query_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AirwaysApi->search_for_airways_v1_api_aerial_corridors_airways_query_post: %s\n" % e)
