#!/usr/bin/env python3
import time
NULL_CHAR = chr(0)

def write_report(report):
	with open('/dev/hidg0', 'rb+') as fd:
		fd.write(report.encode())

def press_key(key):
	write_report(NULL_CHAR*2+chr(key)+NULL_CHAR*5)
	write_report(NULL_CHAR*8)


# press a
#write_report(NULL_CHAR*2+chr(4)+NULL_CHAR*5)
# Release keys
#write_report(NULL_CHAR*8)

# press b
#press_key(5)

for i in range(100):
	# press f10
	#press_key(0x43)
	# press delete
	press_key(0x4c)
	time.sleep(0.1)

time.sleep(10)
#down
press_key(0x51)
#press enter
press_key(0x28)
#down
press_key(0x51)
time.sleep(1)
#down
press_key(0x51)
time.sleep(1)
#down
press_key(0x51)
time.sleep(1)
#enter
press_key(0x28)
time.sleep(1)
#up
press_key(0x52)
time.sleep(1)
#enter
press_key(0x28)
time.sleep(1)
#esc
press_key(0x29)
time.sleep(1)
# esc
press_key(0x29)
time.sleep(1)
# y
press_key(0x1c)
time.sleep(1)

# enter
press_key(0x28)
time.sleep(1)

# not in recepie:
# n
#press_key(0x11)
#time.sleep(0.1)
# enter
#press_key(0x28)
#time.sleep(0.1)
