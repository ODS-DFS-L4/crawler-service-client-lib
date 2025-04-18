# -*- coding: utf-8 -*-
from paho.mqtt import client as mqtt_client
from paho.mqtt.enums import MQTTErrorCode


class SubscribeUtil:
    broker_hostname = 'localhost'
    broker_port = 1883
    clientobj = None

    def on_connect( self, client, userdata, flags, reason_code, properties ):
        if reason_code.is_failure == False:
            print( "Succeeded to connect MQTT Broker." )
        else:
            print( "Failed to connect MQTT Broker: reason=%s", reason_code.getName() )

    def __init__( self, hostname="localhost", port=1883 ):
        self.broker_hostname = hostname
        self.broker_port = port
        self.clientobj = mqtt_client.Client( mqtt_client.CallbackAPIVersion.VERSION2 )
        self.clientobj.on_connect = self.on_connect

    def connect( self ) -> MQTTErrorCode :
        result = self.clientobj.connect( self.broker_hostname, self.broker_port )
        return result

    def disconnect( self ) -> MQTTErrorCode :
        result = self.clientobj.disconnect()
        return result

    def subscribe( self, topic, func ) -> MQTTErrorCode :
        self.clientobj.on_message = func 
        result, mid = self.clientobj.subscribe( topic )
        return result

    def unsubscribe( self, topic ) -> MQTTErrorCode  :
        result, mid = self.clientobj.unsubscribe( topic )
        return result

    #スレッドを占有してメッセージ処理
    def loop( self ):
        self.clientobj.loop_forever()

    #別スレッドを立ててメッセージ処理を開始
    def loop_start( self ):
        self.clientobj.loop_start()

    # loop_startで建てたメッセージ処理を終了して、スレッドを終了させる
    def loop_stop( self ):
        self.clientobj.loop_stop()
