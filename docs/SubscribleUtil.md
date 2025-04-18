# SubscribleUtil

This util class that provides a client class that allows applications to connect to an MQTT broker, publish messages, and subscribe to topics to receive published messages.
Will notify you if there is a change to the route operating company.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**broker_hostname** | **str** | broker hostname  | 
**broker_port** | **int** |  broker port number| default 1883

## Example

```python
from drone_distract.lib_subscribe import SubscribeUtil

def on_message( client, userdata, msg ):
    print( f"Received  topic:{msg.topic}   message:`{msg.payload.decode()}`" )

def main():
    s = SubscribeUtil('localhost', 1883)  # Broker and port of destination
    s.connect()
    s.subscribe(('example.com', 0), on_message)  # notifications route operator
    s.loop_start()
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


