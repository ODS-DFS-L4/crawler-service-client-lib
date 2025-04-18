# AirwayInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**administrator_id** | **str** |  | 
**business_number** | **int** |  | 
**airways** | [**List[SingleAirwayInput]**](SingleAirwayInput.md) |  | 
**url** | **str** |  | 

## Example

```python
from drone_distcat.models.airway_input import AirwayInput

# TODO update the JSON string below
json = "{}"
# create an instance of AirwayInput from a JSON string
airway_input_instance = AirwayInput.from_json(json)
# print the JSON string representation of the object
print(AirwayInput.to_json())

# convert the object into a dict
airway_input_dict = airway_input_instance.to_dict()
# create an instance of AirwayInput from a dict
airway_input_from_dict = AirwayInput.from_dict(airway_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


