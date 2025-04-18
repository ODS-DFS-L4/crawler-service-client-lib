# -*- coding: utf-8 -*-
import sys
import time
from lib_subscribe import SubscribeUtil
# LibSub_ErrStatusの中身は paho.mqtt.enums.MQTTErrorCode  :利用者がpahoを直接使わなくてもいいようにラッピング 
from lib_subscribe import LibSub_ErrStatus


hostname = "localhost"
port = 1883

# sybscribe時のtopicは単語一つ、またはタプルのリストで渡す
#  タプルの構成 : ( topic, qos )
#       qos : Quality of Service   0: 送信後は成功/失敗を確認せず、再送もしない 
#                                  1: 送信後 相手からのAckを待つ 
#                                  2: メッセージが一度だけ到達することを保証する(再送処理、重複検知処理あり)  
#  トピックのワイルドカードに"#"を使うと下の階層まで含めてなんでもいけるっぽい 
#topic1 = "/airway1/#"
#topic2 = "/airway2/+"

#topic = topic1
#topic = topic2
#topic = [ ( topic1, 0 ),  ( topic2, 0 ) ] # トピックが複数の場合

def on_message( client, userdata, msg ):
    print( f"Received  topic:{msg.topic}   message:`{msg.payload.decode()}`" )


def run():


    topics = []
    for idx, topic in enumerate( sys.argv ):
        if idx > 0:
            topics.append( ( topic,  0 ) )

    subobj = SubscribeUtil( hostname, port )
    subobj.connect()
    ret = subobj.subscribe( topics,  on_message )
    if ret == LibSub_ErrStatus.MQTT_ERR_SUCCESS :
        for topic in topics:
            print( f"Subscribed  topic:{topic[0]}" )

    while True:
        try:
            subobj.loop_start()
            time.sleep(1)
            subobj.loop_stop()
        except KeyboardInterrupt:
            # Ctrl+C で unsubscribeする
            ret = subobj.unsubscribe( topics[0][0] )
            if ret == LibSub_ErrStatus.MQTT_ERR_SUCCESS :
                print( f"Unsubscribed  topic:{topics[0][0]}" )
            break

if __name__ == '__main__':
    run()
