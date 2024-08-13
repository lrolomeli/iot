import time
import random
import json
import firebase_admin
from firebase_admin import credentials, db
from colorama import Fore

def db_connect():
    cred = credentials.Certificate("iotsimulateddata-firebase-adminsdk-guzd0-22da15fe23.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://iotsimulateddata-default-rtdb.firebaseio.com/'
    })
    return db.reference('/')

# Paso 1: Simular la recopilación de datos de sensores de temperatura
def get_firebase_data(ref):
    data = []
    
    # Now you can interact with the Firebase Realtime Database
    snapshot = ref.order_by_key().limit_to_last(3).get()

    return snapshot
    
# Paso 3: Procesar los datos recibidos y detectar anomalías
def process_data(data_json):
    anomalies = []
    # Iterate over the posts and print the author of each post
    for post_id, post_info in data_json.items():
        temp = post_info['temperatura']
        if temp < 0.0 or temp > 35.0:
            anomalies.append(temp)
    return anomalies

        
# Paso 4: Tomar acciones basadas en las anomalías detectadas
def take_action(anomalies):
    for anomaly in anomalies:
        print(f"{Fore.RED} Alerta: Temperatura anómala detectada con {anomaly} °C")
        
# Ejecutar la práctica completa
ref = db_connect()
while True:
    sensor_data = get_firebase_data(ref)
    #print(f"{Fore.WHITE} Datos de sensores:", sensor_data)
    anomalies = process_data(sensor_data)
    #print(f"{Fore.WHITE} Anomalías detectadas:", anomalies)
    take_action(anomalies)
    time.sleep(30) # Esperar 1 segundo
