import RPi.GPIO as GPIO

from time import time, sleep
class IRDetector:
    def __init__(self, input_pins, output_pins):
        self.input_pins = input_pins
        self.output_pins = output_pins
        self.detections = 0 
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
                    self.detections += 1
                    self.output()
                
    def detect(self):
        readings = []
        for pin in self.input_pins:
            if(pin != 11):
                readings.append(GPIO.input(pin))
            else:
                readings.append(not GPIO.input(pin))
        print(readings)
        return tuple(readings)
    def output(self, values = None):
        if(values is None):
            values = [GPIO.HIGH for pin in self.output_pins]
        for i, pin in enumerate(self.output_pins):
            GPIO.output(pin, values[i])
        sleep(0.4)
        values = [GPIO.LOW for pin in self.output_pins]
        for i, pin in enumerate(self.output_pins):
            GPIO.output(pin, values[i])

    def cleanup(self):
        self.output()
        print( f'Detected {self.detections} times.\n Using {self.input_pins} as input and {self.output_pins} as output pins. \n Thanks for running!')
        GPIO.cleanup()
