import board
import digitalio
import time
print('hello!')

led = digitalio.DigitalInOut(board.LED)
led.switch_to_output()

while True:
        led.value = True
        time.sleep(0.1)
        led.value = False
        time.sleep(0.1)