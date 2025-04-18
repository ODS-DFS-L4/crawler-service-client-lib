# Crawler Service Client Lib

このリポジトリは、ドローン航路のあり方に係る調査・研究として、ドローン航路システムに係るCrawler Serviceのクライアントライブラリのサンプルを公開しています。

## 目次

- [システム概要](#システム概要)
- [ビルド方法](#ビルド方法)
- [使用方法](#使用方法)
- [ライセンス](#ライセンス)
- [免責事項](#免責事項)

## システム概要

Crawler Service Client LibはCrawler Serviceに対するクライアント機能のライブラリです。  
ドローン航路システムと連携するシステムのアプリがCrawler Service機能を使用するためのライブラリのサンプルです。

## ビルド方法

### .whlファイル構築
以下を実行することで、 `dist/drone_distcat-1.0.0-py3-none-any.whl` が構築されます。
1. 必要なPython ライブラリをインストール
   ```sh
   $ pip install ./build-requirements.txt
   ```
2. .whlファイルを構築
   ```sh
   $ python setup.py build
   $ python setup.py bdist_wheel
   ```

## 使用方法

### ライブラリのインポート
仮想環境で本ライブラリをインストールする方法  
1. `./requirements.txt` と `drone_distcat-1.0.0-py3-none-any.whl` を、作業ディレクトリ（Your/work/directory）に配置
2. 以下を実行
    ```sh
    $ cd Your/work/directory
    $ python -m venv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt
    $ pip install drone_distcat-1.0.0-py3-none-any.whl 
    ```

### Getting Started

```python

import drone_distcat
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
    except ApiException as e:
        print("Exception when calling AirwaysApi->create_airway_v1_api_aerial_corridors_airways_airway_id_put: %s\n" % e)

```

### Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AirwaysApi* | [**create_airway_v1_api_aerial_corridors_airways_airway_id_put**](docs/AirwaysApi.md#create_airway_v1_api_aerial_corridors_airways_airway_id_put) | **PUT** /v1/api/airways/{airway_id} | Create or update an airway by ID
*AirwaysApi* | [**delete_airway_v1_api_aerial_corridors_airways_airway_id_delete**](docs/AirwaysApi.md#delete_airway_v1_api_aerial_corridors_airways_airway_id_delete) | **DELETE** /v1/api/airways/{airway_id} | Delete an airway by ID
*AirwaysApi* | [**get_single_airway_details_v1_api_aerial_corridors_airways_airway_id_get**](docs/AirwaysApi.md#get_single_airway_details_v1_api_aerial_corridors_airways_airway_id_get) | **GET** /v1/api/airways/{airway_id} | Get details of a single airway by ID
*AirwaysApi* | [**search_for_airways_v1_api_aerial_corridors_airways_query_post**](docs/AirwaysApi.md#search_for_airways_v1_api_aerial_corridors_airways_query_post) | **POST** /v1/api/airways/query | Query airways 
*CommonApi* | [**read_version_availability_v1_api_version_availability_get**](docs/CommonApi.md#read_version_availability_v1_api_version_availability_get) | **GET** /v1/api/version-availability | Read Version Availability
*DefaultApi* | [**root_get**](docs/DefaultApi.md#root_get) | **GET** / | Root
*DiscoveryFinderApi* | [**create_discovery_service_v1_api_discovery_finder_discovery_services_post**](docs/DiscoveryFinderApi.md#create_discovery_service_v1_api_discovery_finder_discovery_services_post) | **POST** /v1/api/discovery-finder/discovery-services | Create a new discovery service URL
*DiscoveryFinderApi* | [**delete_discovery_service_v1_api_discovery_finder_discovery_services_url_id_delete**](docs/DiscoveryFinderApi.md#delete_discovery_service_v1_api_discovery_finder_discovery_services_url_id_delete) | **DELETE** /v1/api/discovery-finder/discovery-services/{url_id} | Delete Discovery Service
*DiscoveryFinderApi* | [**get_discovery_services_v1_api_discovery_finder_discovery_services_get**](docs/DiscoveryFinderApi.md#get_discovery_services_v1_api_discovery_finder_discovery_services_get) | **GET** /v1/api/discovery-finder/discovery-services/{url_id} | Get Discovery Services
*DronePortsApi* | [**delete_drone_port_reference_v1_api_managed_corridors_ports_port_id_delete**](docs/DronePortsApi.md#delete_drone_port_reference_v1_api_managed_corridors_ports_port_id_delete) | **DELETE** /v1/api/ports/{port_id} | Delete Drone Port Reference
*DronePortsApi* | [**get_drone_port_details_v1_api_managed_corridors_ports_port_id_get**](docs/DronePortsApi.md#get_drone_port_details_v1_api_managed_corridors_ports_port_id_get) | **GET** /v1/api/ports/{port_id} | Get drone port reference details
*DronePortsApi* | [**search_drone_ports_v1_api_managed_corridors_ports_query_post**](docs/DronePortsApi.md#search_drone_ports_v1_api_managed_corridors_ports_query_post) | **POST** /v1/api/ports/query | Query Drone ports
*DronePortsApi* | [**upsert_drone_port_reference_v1_api_managed_corridors_ports_port_id_put**](docs/DronePortsApi.md#upsert_drone_port_reference_v1_api_managed_corridors_ports_port_id_put) | **PUT** /v1/api/ports/{port_id} | Upsert Drone Port Reference
*SubscriptionsApi* | [**delete_subscription_v1_api_managed_corridors_subscriptions_subscription_id_delete**](docs/SubscriptionsApi.md#delete_subscription_v1_api_managed_corridors_subscriptions_subscription_id_delete) | **DELETE** /v1/api/subscriptions/{subscription_id} | Delete Subscription
*SubscriptionsApi* | [**get_subscription_v1_api_managed_corridors_subscriptions_subscription_id_get**](docs/SubscriptionsApi.md#get_subscription_v1_api_managed_corridors_subscriptions_subscription_id_get) | **GET** /v1/api/subscriptions/{subscription_id} | Get Subscription details
*SubscriptionsApi* | [**search_subscriptions_v1_api_managed_corridors_subscriptions_query_post**](docs/SubscriptionsApi.md#search_subscriptions_v1_api_managed_corridors_subscriptions_query_post) | **POST** /v1/api/subscriptions/query | Query Subscriptions
*SubscriptionsApi* | [**upsert_subscription_v1_api_managed_corridors_subscriptions_subscription_id_put**](docs/SubscriptionsApi.md#upsert_subscription_v1_api_managed_corridors_subscriptions_subscription_id_put) | **PUT** /v1/api/subscriptions/{subscription_id} | Upsert Subscription

### Documentation for DistributedCatalog API

 - [get_route_operator](docs/get_route_operator.md)
 - [send_query](docs/send_query.md)
 - [SubscribeUtil](docs/SubscribleUtil.md)

### Documentation For Models

 - [AirwayGeometry](docs/AirwayGeometry.md)
 - [AirwayInput](docs/AirwayInput.md)
 - [AirwayJunctionDetailInput](docs/AirwayJunctionDetailInput.md)
 - [AirwayJunctionDetailOutput](docs/AirwayJunctionDetailOutput.md)
 - [AirwayJunctionInput](docs/AirwayJunctionInput.md)
 - [AirwayJunctionOutput](docs/AirwayJunctionOutput.md)
 - [AirwayOutput](docs/AirwayOutput.md)
 - [AirwaySection](docs/AirwaySection.md)
 - [AreaOfInterest](docs/AreaOfInterest.md)
 - [AvailabilityEnum](docs/AvailabilityEnum.md)
 - [BBoxDefinition](docs/BBoxDefinition.md)
 - [CreateOrUpdateDronePortReferenceResponse](docs/CreateOrUpdateDronePortReferenceResponse.md)
 - [CreateOrUpdateSubscriptionResponse](docs/CreateOrUpdateSubscriptionResponse.md)
 - [DeleteAirwayDefinitionResponse](docs/DeleteAirwayDefinitionResponse.md)
 - [DeleteDronePortReferenceResponse](docs/DeleteDronePortReferenceResponse.md)
 - [DeleteSubscriptionResponse](docs/DeleteSubscriptionResponse.md)
 - [Deviation](docs/Deviation.md)
 - [DiscoveryServiceListRead](docs/DiscoveryServiceListRead.md)
 - [DronePortDetails](docs/DronePortDetails.md)
 - [DronePortType](docs/DronePortType.md)
 - [DronePortUsageType](docs/DronePortUsageType.md)
 - [Geometry](docs/Geometry.md)
 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [LocationInner](docs/LocationInner.md)
 - [PutAirwayDefinitionParameters](docs/PutAirwayDefinitionParameters.md)
 - [PutDronePortReferenceParameters](docs/PutDronePortReferenceParameters.md)
 - [PutSubscriptionParameters](docs/PutSubscriptionParameters.md)
 - [QueryAirwayDefinitionParameters](docs/QueryAirwayDefinitionParameters.md)
 - [QueryDronePortReferenceParameters](docs/QueryDronePortReferenceParameters.md)
 - [QueryDronePortReferenceResponse](docs/QueryDronePortReferenceResponse.md)
 - [QuerySingleAirwayDefinitionResponse](docs/QuerySingleAirwayDefinitionResponse.md)
 - [QuerySubscriptionParameters](docs/QuerySubscriptionParameters.md)
 - [SingleAirwayDefinitionResponse](docs/SingleAirwayDefinitionResponse.md)
 - [SingleAirwayInput](docs/SingleAirwayInput.md)
 - [SingleAirwayOutput](docs/SingleAirwayOutput.md)
 - [SingleDiscoveryServiceDetail](docs/SingleDiscoveryServiceDetail.md)
 - [SubscriptionBase](docs/SubscriptionBase.md)
 - [UpsertAirwayDefinitionResponsePublic](docs/UpsertAirwayDefinitionResponsePublic.md)
 - [ValidationError](docs/ValidationError.md)
 - [VersionAvailabilityRead](docs/VersionAvailabilityRead.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.

## ライセンス

- 本リポジトリはMITライセンスで提供されています。
- ソースコードおよび関連ドキュメントの著作権はIntentExchange株式会社に帰属します。

## 免責事項
- 本リポジトリの内容は予告なく変更・削除する可能性があります。
- 本リポジトリの利用により生じた損失及び損害等について、いかなる責任も負わないものとします。
