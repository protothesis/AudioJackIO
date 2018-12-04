# Audio Jack Data I/O prototype
# Metro M0 - Circuit Python 3.x

# //// IMPORTS
import board
import time
from digitalio import DigitalInOut, Direction, Pull

# Built in red LED
led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

# Output Jack
outjack = DigitalInOut(board.D3)
outjack.direction = Direction.OUTPUT

# Input Jack
injack = DigitalInOut(board.D8)
injack.direction = Direction.INPUT
injack.pull = Pull.UP





### //// PURE FUNCTIONS  (descriptive camel case)
def currentTime():  # returns the current time
	#
	return time.monotonic()
    
def isItTime(previous_time, pause_duration):  # returns if its time to do a thing
	#
	return currentTime() - previous_time > pause_duration

def outJackIsOn():
	#
	return not outjack.value

def inJackIsOn():
	#
	return not injack.value




### //// COMMAND FUNCTIONS  (use prefix "do" naming convention)




### //// NEW STATE VARIABLES (standard python underscore separator)
pause_duration_output = .5
previous_time_toggle_output = currentTime()

# _output = outjack.value
# _input = injack.value  


print("The Device has Initialized...")


while True:

	if isItTime(previous_time_toggle_output, pause_duration_output):
		# _output = not _output
		# using the _output and _input variables in this way didnt work...

		outjack.value = not outjack.value
		previous_time_toggle_output = currentTime()

		# print("")
		# print("isItTime checked...")
		# print("output jack = ", outJackIsOn())
		# print("input jack = ", inJackIsOn())

	# set led equal to injack
	led.value = inJackIsOn()

	time.sleep(0.01)  # make bigger to slow down
