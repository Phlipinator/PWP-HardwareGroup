#source https://github.com/tayfunulu/WiFiManager

def start():

    import wifimgr

    """     from microDNSSrv import MicroDNSSrv
    domainsList = {
    "test.com"   : "1.1.1.1",
    "*test2.com" : "2.2.2.2",
    "*google*"   : "192.168.4.1",
    "*.toto.com" : "192.168.4.1",
    "www.site.*" : "192.168.4.1" }
    mds = MicroDNSSrv(domainsList)
    if mds.Start() :
        print("MicroDNSSrv started.")
    else :
        print("Error to starts MicroDNSSrv...") """

    wlan = wifimgr.get_connection()
    if wlan is None:
        print("Could not initialize the network connection.")
        while True:
            pass 

    # Main Code goes here, wlan is a working network.WLAN(STA_IF) instance.
    #print("ESP OK")

    #import server
    #server.start()

start()