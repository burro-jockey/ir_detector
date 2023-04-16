import RPi.GPIO as GPIO
from time import time
from ob import IRDetector

detcor = IRDetector([11], [13, 15])
detcor.run_for_duration(3o)
detcor.cleanup()
print("Thanks for running!")
