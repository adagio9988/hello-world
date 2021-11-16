import network
import utime as time

# Specify the SSID and password of your WiFi network
WIFI_CFG = { 'ssid': "hnnn", 'pwd': "99883322" }

def connect_wifi( wifi_cfg, max_retries=10 ):
    # use WiFi in station mode (not AP)
    wifi_sta = network.WLAN( network.STA_IF )
    # activate the WiFi interface (up)
    wifi_sta.active(True)
    # connect to the specified WiFi AP
    wifi_sta.connect( wifi_cfg['ssid'], wifi_cfg['pwd'] )
    retries = 0
    print("max_retries : ",max_retries)
    while not wifi_sta.isconnected():
        retries = retries + 1
        print("connecting count : ",retries)
        if retries >= max_retries:
            return None
        time.sleep_ms(500)
    return wifi_sta

# try to connect the network
wifi = connect_wifi( WIFI_CFG )

if wifi is None:
    print( 'WiFi connection failed' )
else:
    ipaddr, netmask, gateway, dns = wifi.ifconfig()
    print("-------------------------------")
    print("IP address  :", ipaddr)
    print("Net mask    :", netmask)
    print("Gateway     :", gateway)
    print("DNS server  :", dns)    
    print("-------------------------------")
    print("CONNECT SUCCESS")

import uping

uping.ping("168.126.63.1",count = 10)