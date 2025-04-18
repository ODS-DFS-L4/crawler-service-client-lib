import json
import requests
import discovery_client
from discovery_client.models.discovery_service_list_read import DiscoveryServiceListRead
from discovery_client.models.query_drone_port_reference_parameters import QueryDronePortReferenceParameters
from discovery_client.models.query_drone_port_reference_response import QueryDronePortReferenceResponse
from discovery_client.rest import ApiException
from pprint import pprint


DISCOVERY_FINDER_URL = 'http://10.0.10.62:8081'
DISTRIBUTE_CATALOG_URL = 'http://crawler-service.example.com/v1/api/sendEndpointList'
# DISTRIBUTE_CATALOG_URL = 'http://10.0.11.176:8081/v1/api/sendEndpointList'


def _get_discovery_services(discovery_finder_host):
    configuration = discovery_client.Configuration(
        host = discovery_finder_host  # u"http://localhost:8081"
    )

    # Enter a context with an instance of the API client
    with discovery_client.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = discovery_client.DiscoveryFinderApi(api_client)
        url_id = 'discoveryservice' # str | 

    try:
        # Get Discovery Services
        api_response = api_instance.get_discovery_services_v1_api_discovery_finder_discovery_services_get(url_id)
        return(api_response.to_dict())
    except Exception as e:
        print("Exception when calling DiscoveryFinderApi->get_discovery_services_v1_api_discovery_finder_discovery_services_get: %s\n" % e)


def _query_droneport(
        disovery_service_url,
        min_latitude = -90,
        min_longitude = -180,
        max_latitude = -90,
        max_longitude = -180):
    configuration = discovery_client.Configuration(
        host = disovery_service_url  # "http://10.0.7.127:8082"
    )

    # Enter a context with an instance of the API client
    with discovery_client.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = discovery_client.DronePortsApi(api_client)
        query_drone_port_reference_parameters = discovery_client.QueryDronePortReferenceParameters(
            area_of_interest = discovery_client.models.area_of_interest.AreaOfInterest(
                outline_polygon = discovery_client.models.b_box_definition.BBoxDefinition(
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
            return [ar.to_dict() for ar in api_response]
        except Exception as e:
            print("Exception when calling DronePortsApi->search_drone_ports_v1_api_managed_corridors_ports_query_post: %s\n" % e)


def get_route_operator(
        min_latitude = -90,
        min_longitude = -180,
        max_latitude = 90,
        max_longitude = 180):
    # ディスカバリーファインダーでディスカバリーサービスをURLを取得する
    dlist = _get_discovery_services(DISCOVERY_FINDER_URL)['available_services']
    disovery_service_url = dlist[0]['url']

    # ディスカバリーサービスからドローンポートURLを取得する
    dp_list = _query_droneport(
        disovery_service_url, min_latitude, min_longitude, max_latitude, max_longitude)
    droneport_list = [dp['url'] for dp in dp_list]
    print(droneport_list)

    # ドローンポートURLを分散カタログに送信する
    ret = requests.post(
        DISTRIBUTE_CATALOG_URL,
        data=json.dumps({"endpoint_list": droneport_list}),
        headers={"Content-Type": "application/json"})
    if ret.status_code != 200:
        err = "分散カタログへの送信に失敗しました"
        # logger.error(err)
        raise ValueError(err)
