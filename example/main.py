from time import sleep
from drone_distcat.lib_subscribe import SubscribeUtil
from drone_distcat.lib_distribute_catalog import get_route_operator


def on_message( client, userdata, msg ):
    print( f"Received  topic:{msg.topic}   message:`{msg.payload.decode()}`" )


def main():
    # s = SubscribeUtil('crawler-service.example.com', 1883)
    # s = SubscribeUtil('localhost', 1883)
    # s.connect()
    # s.subscribe(('10.0.11.246:8084', 0), on_message)
    # s.loop_start()

    print(get_route_operator(
        'http://10.0.10.62:8081',  # DiscoveryFinder
        'http://10.0.11.176:8081'))  # DistributedCatalog WebAPI

    # while True:
    #    sleep(5)
    #    print("loop()")

if __name__ == '__main__':
    main()
