import random 
import time
import firebase_admin
from firebase_admin import credentials, db


# Function to simulate sensor data 
def simulate_sensor_data(): 
    temperature = round(random.uniform(-10.0, 40.0), 2) # Simulate temperature between 20.0 and 30.0 degrees Celsius 
    humidity = round(random.uniform(30.0, 70.0), 2) # Simulate humidity between 30.0% and 70.0% 
    return temperature, humidity 


cred = credentials.Certificate("iotsimulateddata-firebase-adminsdk-guzd0-22da15fe23.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://iotsimulateddata-default-rtdb.firebaseio.com/'
})

# Now you can interact with the Firebase Realtime Database
ref = db.reference('/')
print(ref)
#temp = db.reference("/temperatura")
#hum = db.reference("/humedad")

# Send data to FireBase
#ref.set({
#'humedad': 25,
#'temperatura': 30
#})



# obtener datos
#data = ref.get()

#print(data)

while True: 
    # Get simulated sensor data 
    temperature, humidity = simulate_sensor_data() 
 
    # Print simulated data 
    print(f'Simulated Temp={temperature}*C Humidity={humidity}%')
    
    # Send data to FireBase
    ref.push({
    'humedad': humidity,
    'temperatura': temperature
    })
    # temp.set(temperature)
    # hum.set(humidity)

    #response = requests.post(THINGSPEAK_URL, data=payload) 
 
    #if response.status_code == 200: 
        #print('Data sent to ThingSpeak successfully!') 
    #else: 
        #print('Failed to send data to ThingSpeak.') 
    # Wait 10 seconds before next read 
    time.sleep(10)
