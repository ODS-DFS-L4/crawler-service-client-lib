# DronePortDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manufacturer** | **str** |  | [optional] 
**port_type** | [**DronePortType**](DronePortType.md) |  | 
**latitude** | **float** | ドローンポート中心緯度 | 
**longitude** | **float** | ドローンポート中心経度 | 
**altitude** | **float** | ドローンポート着陸面の高さ(対地高度) | 
**supports_drone_type** | **str** | 対応機体。着陸可能な機体の種類等を設定 | 
**usage_type** | [**DronePortUsageType**](DronePortUsageType.md) |  | 
**url** | **str** | ドローンポートのURL | 

## Example

```python
from drone_distcat.models.drone_port_details import DronePortDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DronePortDetails from a JSON string
drone_port_details_instance = DronePortDetails.from_json(json)
# print the JSON string representation of the object
print(DronePortDetails.to_json())

# convert the object into a dict
drone_port_details_dict = drone_port_details_instance.to_dict()
# create an instance of DronePortDetails from a dict
drone_port_details_from_dict = DronePortDetails.from_dict(drone_port_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


