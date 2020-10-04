import sqlite3

conn = sqlite3.connect('mydatabase.db')

print ("Opened database successfully");


#to be commented out once table is already made
conn.execute('''CREATE TABLE TEMP
         (tdate        DATE    NOT NULL,
         ttime         TIME    NOT NULL,
         zone          TEXT    NOT NULL,
         temperature         NUMERIC);''')
print ("Table 1 created successfully");

conn.execute("INSERT INTO TEMP (tdate, ttime, zone, temperature) \
      VALUES (date('now', '-1 day'),time('now'),'kitchen', 20.6)");

conn.execute("INSERT INTO TEMP (tdate, ttime, zone, temperature) \
      VALUES (date('now', '-1 day'),time('now'), 'greenhouse', 26.3)");

conn.execute("INSERT INTO TEMP (tdate, ttime, zone, temperature) \
      VALUES (date('now', '-1 day'),time('now'), 'garage', 18.6)");

conn.execute("INSERT INTO TEMP (tdate, ttime, zone, temperature) \
      VALUES (date('now'),time('now', '-12 hours'),'kitchen', 19.5)");

conn.execute("INSERT INTO TEMP (tdate, ttime, zone, temperature) \
      VALUES (date('now'),time('now', '-12 hours'), 'greenhouse', 15.1)");

conn.execute("INSERT INTO TEMP (tdate, ttime, zone, temperature) \
      VALUES (date('now'),time('now', '-12 hours'), 'garage', 18.1)");

conn.execute("INSERT INTO TEMP (tdate, ttime, zone, temperature) \
      VALUES (date('now'),time('now'),'kitchen', 21.2)");

conn.execute("INSERT INTO TEMP (tdate, ttime, zone, temperature) \
      VALUES (date('now'),time('now'), 'greenhouse', 27.1)");

conn.execute("INSERT INTO TEMP (tdate, ttime, zone, temperature) \
      VALUES (date('now'),time('now'), 'garage', 19.1)");

cursor = conn.execute("SELECT tdate, ttime, zone, temperature from TEMP")
for row in cursor:
   print ("tdate = ", row[0])
   print ("ttime = ", row[1])
   print ("zone = ", row[2])
   print ("temperature = ", row[3], "\n")
   




#to be commented out once table is already made
conn.execute('''CREATE TABLE SENSORS
         (sensorID INT PRIMARY KEY     NOT NULL,
         type           TEXT    NOT NULL,
         zone           TEXT    NOT NULL);''')
print ("Table 2 created successfully");

conn.execute("INSERT INTO SENSORS (sensorID, type, zone) \
      VALUES (1,'door','kitchen')");

conn.execute("INSERT INTO SENSORS (sensorID, type, zone) \
      VALUES (2,'temperature','kitchen')");

conn.execute("INSERT INTO SENSORS (sensorID, type, zone) \
      VALUES (3,'door','garage')");

conn.execute("INSERT INTO SENSORS (sensorID, type, zone) \
      VALUES (4,'motion','garage')");

conn.execute("INSERT INTO SENSORS (sensorID, type, zone) \
      VALUES (5,'temperature','garage')");

cursor = conn.execute("SELECT sensorID, type, zone from SENSORS")

for row in cursor:
   print ("sensorID = ", row[0])
   print ("type = ", row[1])
   print ("zone = ", row[2], "\n")
   
conn.commit()
print("Records created successfully");
conn.close()


