from machine import Pin
led= Pin(4, Pin.OUT)
sensor = Pin(15, Pin.IN)

while True:
    x=sensor.value()
    if x==1:
        led.value(1)
    else:
        led.value(0)



