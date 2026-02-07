#Import libraries
#serial is used to communicate with the Arduino serial data stream
import serial
import time
from datetime import datetime
from sys import argv

#User configurable variables - these will need to be configured
#Set hardware interface (COM port). Use 'python -m serial.tools.list_ports -v' to determine settings
interface = 'COM5'
#For collection mode set total run duration in seconds
duration = 10
#For collection mode 
interval = 0.5

#Obtain arguments from command to determine which mode the script should run
mode = argv[1]

#Filename for collection mode file
if mode == 'collect':
	#Gets current date/time in format yyyymmdd_hhmmss
	filename_datetime = datetime.now().strftime('%Y%m%d_%H%M%S')
	#Set prefix and suffix - including file extension
	filename_prefix = 'photometer_'
	filename_suffix = '.csv'
	filename = filename_prefix + filename_datetime + filename_suffix
	#Open file to write data into
	file = open(filename, "a")
	#Put header row into file
	file.write('time /s,10-bit\n')
	#Print filename to screen
	print('Filename: ' + filename)



#Set up serial port - uses 'interface' variable to configure the hardware setup
ser = serial.Serial(port=interface, baudrate=9600, timeout=100)

#Fixed variables
start = time.time()
reset = time.time()
skip_line = True

#Main loop
while True:
	ser.flush()
	#Obtains data from the serial data stream.
	#Data is obtained as a binary value and rstrip() removes line breaks and other formatting
	value = ser.readline().rstrip()
	#Loop which reads the line twice and takes the second value. As we could start reading the line at any point
	if skip_line:
		skip_line = False
		continue
	#Converts from binary to decimal
	data_10_bit = int(value,10)
	#Runs relevant function depending on mode from command line argument
	if mode == 'single':
		#For single reading prints value to screen and exits loop
		print(data_10_bit)
		break
	elif mode == 'stream':
		#
		print(data_10_bit)
	elif mode == 'collect':
		now = time.time()
		if (now-reset) > 1.5*interval:
			start = time.time()
			reset = now
			continue
		#print(round(now-reset-interval,2))
		if now-reset-interval > 0.0:
			print(f'{now-start:.4f},{data_10_bit}')
			#Writes measurements to the CSV file
			file.write(str(now-start) + ',' + str(data_10_bit) + '\n')
			reset = now
			#End data collection when duration of run is exceeded
			if time.time() - start > duration:
				file.close
				break
	#If an unknown mode is run print error statement and list possible modes
	else:
		print('Script argument not recognised: Valid options are single, stream, collect')
		break