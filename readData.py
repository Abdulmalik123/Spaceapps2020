import time
import serial
import sqlite3
import pandas as pd

#time of day on mars in seconds
#there are exactly 88,620 seconds in 1 mars day
marsTime = 0
dayLength = 88620
time.clock() #start a clock

status=0 #0 means there is no dust storm, 1 means there is a dust storm

#Column names are TimeStamp and Value
#Value is the reading fro                                                                  m the sensor
#range is roughtly 0-3000 right now
conn = sqlite3.connect('Data//marsSensor.db')
c = conn.cursor() # contians table light with columns time and value
c.execute("""DROP TABLE light""")
c.execute('''CREATE TABLE light
            (time int, value int)
        ''')
arduino = serial.Serial('COM9', 9600, timeout=.1)

#returns a pandas database of the data collected so far
def GetData():
    return lightData

while True:
    data = (arduino.readline()[:-2]) #the last bit gets rid of the new-line chars
    if data:
        data = int(data.decode("utf-8"))
        marsTime = round(time.clock()-3)
        nextRow = [marsTime, data]
        c.execute("INSERT INTO light VALUES (?,?)", nextRow)
        conn.commit()
        df = pd.read_sql_query("select * from light", conn)
        print(df.loc[len(df)-1])
conn.close()