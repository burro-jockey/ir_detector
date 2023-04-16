
import RPi.GPIO as GPIO
from time import time
from ob import IRDetector

def main(seconds = 30, input_pins = [11, 15], output_pins = [13]): 
    # do stuff
    
    detcor = IRDetector(input_pins , output_pins)
    detcor.run_for_duration(seconds)
    detcor.cleanup()
    print("Thanks for running!")

import argparse


if __name__ == '__main__':
    # Set up argparse to parse command line arguments
    parser = argparse.ArgumentParser(description='Wait for a number of seconds.')
    parser.add_argument('seconds', metavar='N', type=int,
                        help='the number of seconds to wait')
    parser.add_argument('input', metavar='i', type=str,
                        help='list of ints')
    parser.add_argument('output', metavar='o', type=str,
                        help='list of ints')
    args = parser.parse_args()

    # Call the main function with the number of seconds
    main(args.seconds, [int(x) for x in args.input.split(" ")] , [int(x) for x in args.output.split(" ")])
