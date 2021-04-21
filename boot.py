import esp
import network
import webrepl
import time
esp.osdebug(None)
import uos, machine
import gc
gc.collect()
net = network.WLAN(network.STA_IF)
net.active(True)
net.active()
net.connect('Robins crib','88888888')
time.sleep(2)
webrepl.start()
#import webrepl_setup