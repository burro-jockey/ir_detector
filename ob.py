import RPi.GPIO as GPIO

from time import time, sleep
class IRDetector:
    def __init__(self, input_pins, output_pins):
        self.input_pins = input_pins
        self.output_pins = output_pins
        
        # Set up GPIO
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        for pin in self.input_pins:
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        for pin in self.output_pins:
            GPIO.setup(pin, GPIO.OUT)
    def run_for_duration(self, duration):
        t0 = time() # time is in seconds here
        results = []
        while (time() - t0) < duration:
            results = self.detect()
            for x in results:
                if x != 1:
                    print("Detected")
                    self.output()
                
    def detect(self):
        readings = [GPIO.input(pin) for pin in self.input_pins]
        return tuple(readings)
    def output(self, values = None):
        if(values is None):
            values = [GPIO.HIGH for pin in self.output_pins]
        for i, pin in enumerate(self.output_pins):
            GPIO.output(pin, values[i])
        sleep(0.1)
        values = [GPIO.LOW for pin in self.output_pins]
        for i, pin in enumerate(self.output_pins):
            GPIO.output(pin, values[i])

    def cleanup(self):
        self.output()
        GPIO.cleanup()
