from pyfirmata import Arduino, util
import time

# Define the serial port (check your Arduino IDE for the correct port)
port = 'COM3'  # Change 'COM3' to your Arduino's serial port

# Create a new Arduino board instance
board = Arduino(port)
# Define the LED pin (e.g., pin 13)
led_pin = board.get_pin('d:13:o')  # Digital output pin 13

while True:

	# Turn on the LED
	led_pin.write(1)

	# Run your program or perform tasks
	print("Running your program...")
	time.sleep(2)  # Simulate your program running for 5 seconds

	# Turn off the LED
	led_pin.write(0)

	time.sleep(2)  # Simulate your program running for 5 seconds


# Close the board connection
board.exit()