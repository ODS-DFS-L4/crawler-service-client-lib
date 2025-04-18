import drone_distcat
import json
# from drone_distcat.models.airway_input import AirwayInput
# from drone_distcat.models.single_airway_input import SingleAirwayInput
from drone_distcat.models.put_airway_definition_parameters import PutAirwayDefinitionParameters
from drone_distcat.models.upsert_airway_definition_response_public import UpsertAirwayDefinitionResponsePublic
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
    airway_id = 'airway_id_example' # str | 
    put_airway_definition_parameters = drone_distcat.PutAirwayDefinitionParameters(
        airway = drone_distcat.models.airway_input.AirwayInput(
            administrator_id = '', 
            business_number = 56, 
            airways = [
                drone_distcat.models.single_airway_input.SingleAirwayInput(
                    id = '', 
                    name = '', 
                    junctions = [
                        drone_distcat.models.airway_junction_input.AirwayJunctionInput(
                            id = '', 
                            name = '', 
                            type = '', 
                            airways = [
                                drone_distcat.models.airway_junction_detail_input.AirwayJunctionDetailInput(
                                    airway = drone_distcat.models.airway_geometry.AirwayGeometry(
                                        geometry = drone_distcat.models.geometry.Geometry(
                                            type = '', 
                                            coordinates = [
                                                [
                                                    '38.1', '141.2', '123.4'
                                                    ]
                                                ], ), ), 
                                    deviation = drone_distcat.models.deviation.Deviation(
                                        geometry = drone_distcat.models.geometry.Geometry(
                                            type = '', 
                                            coordinates = [
                                                [
                                                    '38.1', '141.2', '123.4'
                                                    ]
                                                ], ), ), )
                                ], )
                        ], 
                    sections = [
                        drone_distcat.models.airway_section.AirwaySection(
                            id = '', 
                            name = '', 
                            airway_point_ids = [
                                ''
                                ], )
                        ], )
                ], 
            url = '', )
    )

    try:
        # Create or update an airway by ID
        api_response = api_instance.create_airway_v1_api_aerial_corridors_airways_airway_id_put(airway_id, put_airway_definition_parameters)
        print("The response of AirwaysApi->create_airway_v1_api_aerial_corridors_airways_airway_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AirwaysApi->create_airway_v1_api_aerial_corridors_airways_airway_id_put: %s\n" % e)
