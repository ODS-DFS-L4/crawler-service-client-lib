import json
import requests
import drone_distcat
from drone_distcat.models.discovery_service_list_read import DiscoveryServiceListRead
from drone_distcat.models.query_drone_port_reference_parameters import QueryDronePortReferenceParameters
from drone_distcat.models.query_drone_port_reference_response import QueryDronePortReferenceResponse
from drone_distcat.rest import ApiException
from pprint import pprint


# DISCOVERY_FINDER_URL = 'http://10.0.10.62:8080'
# DISTRIBUTE_CATALOG_URL = 'http://crawler-service.example.com/v1/api/sendEndpointList'
# DISTRIBUTE_CATALOG_SEND_QUERY_URL = 'http://crawler-service.example.com/v1/api/sendQuery'
# DISTRIBUTE_CATALOG_URL = 'http://10.0.11.176:8080/v1/api/sendEndpointList'
# DISTRIBUTE_CATALOG_SEND_QUERY_URL = 'http://10.0.11.176:8080/v1/api/sendQuery'


def _get_discovery_services(discovery_finder_host):
    configuration = drone_distcat.Configuration(
        host = discovery_finder_host  # u"http://localhost:8080"
    )

    # Enter a context with an instance of the API client
    with drone_distcat.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = drone_distcat.DiscoveryFinderApi(api_client)
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
    configuration = drone_distcat.Configuration(
        host = disovery_service_url  # "http://10.0.7.127:8082"
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
        # TODO: 本来は引数としてユーザが指定すべき内容
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
        finder_url: str,
        host_domain: str,
        min_latitude = -90,
        min_longitude = -180,
        max_latitude = 90,
        max_longitude = 180):
    
    # 分散カタログサービスのURLを取得する
    host_url = host_domain + '/v1/api/sendEndpointList'
    
    # ディスカバリーファインダーでディスカバリーサービスをURLを取得する
    dlist = _get_discovery_services(finder_url)['available_services']
    disovery_service_url = dlist[0]['url']
    print(f"{disovery_service_url=}")

    # ディスカバリーサービスからドローンポートURLを取得する
    dp_list = _query_droneport(
        disovery_service_url, min_latitude, min_longitude, max_latitude, max_longitude)
    droneport_list = [dp['url'] for dp in dp_list]
    print(f"{droneport_list=}")

    print(f"Call dist catalog {host_url}")
    # ドローンポートURLを分散カタログに送信する
    ret = requests.post(
        host_url,
        data=json.dumps({"endpoint_list": droneport_list}),
        headers={"Content-Type": "application/json"})
    # print(ret)
    if ret.status_code != 200:
        err = "分散カタログへの送信に失敗しました"
        raise ValueError(err)

    return droneport_list


def send_query(host_url: str, query: str):
    # アプリ連携: APIサーバの提供と設計支援システムとの連携
    # print(f"Call dist catalog {host_url}")
    d = json.dumps({"query": query})
    ret = requests.post(
        host_url,
        # data=json.dumps({"query": query}),
        params={"query": query},
        headers={"Content-Type": "application/json"})
    if ret.status_code != 200:
        err = "分散カタログへの送信に失敗しました"
        raise ValueError(err)
    return ret.text
