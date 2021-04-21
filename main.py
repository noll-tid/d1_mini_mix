import network
import ssd1306
from machine import Pin, I2C, ADC
from writeoled import write
from time import sleep
import dht
import ujson
#import sms
net = network.WLAN(network.STA_IF)
d = dht.DHT22(Pin(0))
p1 = Pin(16, Pin.OUT)
state = {}

def savea(stat):
    with open('state.json', 'w') as f:
        f.write(ujson.dumps(stat))
        f.close()

status = ujson.loads(str(open('state.json', 'r').read()))

if '1' in status.keys():
    state['1'] = status['1']
    if state['1'] == 'off':
        p1.value(0)
    elif state['1'] == 'on':
        p1.value(1)
else:
    state['1'] = 'off'
    savea(state)

while True:
    d.measure()
    temp = str(d.temperature())
    hum = str(d.humidity())
    #lista = sms.check()
    write([net.ifconfig()[0],"Temp: {0}".format(temp),"Humidity: {0}".format(hum),"Outlet: {0}".format(state['1'])])
    sleep(2)

    """if len(lista) >= 1:
        for entry in lista:
            number = entry['number']
            msgid = entry['msgid']
            message = entry['message']
            write([number, message, msgid])
            message = message.replace('\r', '').replace('\n', '')
            if message.lower() == "on 1":
                state['1'] = 'on'
                savea(state)
                p1.value(1)
                sms.send(number, "Turned on outlet 1")
            elif message.lower() == "off 1":
                state['1'] = 'off'
                savea(state)
                p1.value(0)
                sms.send(number, "Turned off outlet 1")
            elif message.lower() == "status":
                sms.send(number, "Outlet 1: {0}".format(state['1']))
            elif message.lower() == "temp":
                sms.send(number, "Temp: {0}, Hum: {1}".format(temp, hum))
            else:
                sms.send(number, "Error: "+message)
            command = 'AT+CMGD='+msgid
            sms.cmd(command, 0.5)
            time.sleep(1)
    else:
        write(['No new messages'])"""
