import RPi.GPIO as GPIO

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
            results = []
            results.append(self.detect())
            [ output(1) for x in results if x != 0 ] 
    def detect(self):
        readings = [GPIO.input(pin) for pin in self.input_pins]
        return tuple(readings)

    def output(self, values):
        for i, pin in enumerate(self.output_pins):
            GPIO.output(pin, values[i])

    def cleanup(self):
        GPIO.cleanup()