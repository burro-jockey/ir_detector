
import RPi.GPIO as GPIO
from time import time
from ob import IRDetector

def main(seconds = 30): 
    # do stuff
    
    detcor = IRDetector([11 , 15], [ 13])
    detcor.run_for_duration(seconds)
    detcor.cleanup()
    print("Thanks for running!")

import argparse


if __name__ == '__main__':
    # Set up argparse to parse command line arguments
    parser = argparse.ArgumentParser(description='Wait for a number of seconds.')
    parser.add_argument('seconds', metavar='N', type=int,
                        help='the number of seconds to wait')
    args = parser.parse_args()

    # Call the main function with the number of seconds
    main(args.seconds)
