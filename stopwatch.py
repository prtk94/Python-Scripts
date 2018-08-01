#! python3
# stopwatch.py - A simple stopwatch program.
import time
# Display the program's instructions.
print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
input() # press Enter to begin
print('Started.')
startTime = time.time() # get the first lap's start time
lastTime = startTime
lapNum = 1

#Start tracking...
try:
	while True:
		input() #Enter
		lapTime = round(time.time()-lastTime,2)
		totalTime = round(time.time()-startTime,2)
		print('Lap #%s: %s (%s) seconds' % (lapNum, totalTime, lapTime), end='')
		lapNum += 1
		lastTime = time.time() # reset the last lap time
except KeyboardInterrupt:
	# Handle the Ctrl-C exception to keep its error message from displaying.
	print('\nDone.')	
	totalTime = str(round((lastTime)-(startTime),2))
	

print('Total time:' + totalTime+'seconds')