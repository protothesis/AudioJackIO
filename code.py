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
outjack01 = DigitalInOut(board.D3)
outjack01.direction = Direction.OUTPUT

# Output Jack 02
outjack02 = DigitalInOut(board.D4)
outjack02.direction = Direction.OUTPUT

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

# this is a solution for checking multiple jacks...
# but im not currently using it...
# def outJackIsOn(outjack):  # make sure to pass in which outjack you want
# 	#
# 	return not outjack.value

def inJackIsOn():
	#
	return not injack.value




### //// COMMAND FUNCTIONS  (use prefix "do" naming convention)




### //// NEW STATE VARIABLES (standard python underscore separator)
pause_duration_outjack01 = .5
previous_time_toggle_outjack01 = currentTime()

pause_duration_outjack02 = .1
previous_time_toggle_outjack02 = currentTime()

# CONNECTOR START
# connection_state = 

# _output = outjack.value
# _input = injack.value  


print("The Device has Initialized...")

# CONNECTOR START
input_stream_buffer = []
# there needs to be a buffer to check the output signals against
# need a sort of "clock" track (ie 1111...) before the signal itself 
# to know when to check the buffer for the signal itself...
# quite an involved problem afterall...


while True:

	if isItTime(previous_time_toggle_outjack01, pause_duration_outjack01):
		outjack01.value = not outjack01.value
		previous_time_toggle_outjack01 = currentTime()

	if isItTime(previous_time_toggle_outjack02, pause_duration_outjack02):
		outjack02.value = not outjack02.value
		previous_time_toggle_outjack02 = currentTime()


	# set led equal to injack
	led.value = inJackIsOn()

	# CONNECTOR START
	# print("connection +", connection_state)

	time.sleep(0.01)  # make bigger to slow down