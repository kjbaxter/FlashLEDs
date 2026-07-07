

from machine import Pin
from utime import sleep

low = 0
high = 1
blue_pin = Pin(42, Pin.OUT)
red_pin = Pin(41, Pin.OUT)
ctr = 0

print("LED starts flashing...")

while True:
    try:
        # red off & blue on
        red_pin.value(low)
        blue_pin.value(high)
        sleep(1) # sleep 1 second

        # red on & blue off
        red_pin.value(high)
        blue_pin.value(low)
        sleep(1) # sleep 1 second
    except KeyboardInterrupt:
        break

    print("LED counter %d times." % ctr)
    ctr+= 1

#blue_pin.off()
#red_pin.off()

print("Finished.")