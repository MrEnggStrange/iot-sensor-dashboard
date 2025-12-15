# code that mocks a sensor data and prints it

import json
import time
from datetime import datetime
LOG_FILE = "readings.json1"
# simulated sensor data
def get_sensor_reading():
    """Pretend we are reading from a real sensor"""
    return{
        "temperature": 25.5,
        "pressure" : 101.3,
        "timestamp" : datetime.now().isoformat()
    }

#main loop 
while True:
    reading = get_sensor_reading()
    #print to terminal
    print(json.dumps(reading, indent = 2))
    #append as one JSON object per line to a log file
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(reading)+ "\n")

    time.sleep(2) #read every 2 sec
