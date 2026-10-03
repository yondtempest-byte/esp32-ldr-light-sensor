# esp32-ldr-light-sensor
ESP32 project with Light-Sensor
A simple light detection project using ESP32, an LDR sensor module, and an LED.

## Components

- ESP32
- LDR light sensor module
- LED
- Resistor
- Breadboard
- Jumper wires

## Wiring

| Component | ESP32 |
|---|---|
| LDR VCC | 3V3 |
| LDR GND | GND |
| LDR DO | GPIO 15 |
| LED | GPIO 4 |

## How It Works

The LDR sensor detects the surrounding light level.

The sensor sends a digital signal through its DO pin to GPIO 15 of the ESP32.

The ESP32 reads the signal and controls the LED on GPIO 4.

## Code

```python
from machine import Pin

led = Pin(4, Pin.OUT)
sensor = Pin(15, Pin.IN)

while True:
    nilai = sensor.value()

    if nilai == 1:
        led.value(1)
    else:
        led.value(0)
