
import paho.mqtt.client as mqtt
import json, time, random
from datetime import datetime

BROKER = "localhost"
TOPIC_SENSOR = "iot/sensor"
TOPIC_KONTROL = "iot/kontrol"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Berhasil terhubung ke Mosquitto!")
    else:
        print(f"Koneksi gagal. Kode: {rc}")

client = mqtt.Client(
    callback_api_version=mqtt.CallbackAPIVersion.VERSION1,
    client_id="ESP32-Simulator"
)

client.on_connect = on_connect
client.connect(BROKER, 1883, 60)
client.loop_start()

print("ESP32 Simulator berjalan... Ctrl+C untuk stop")

try:
    while True:
        data = {
            "suhu": round(random.uniform(25, 32), 1),
            "kelembaban": round(random.uniform(55, 80), 1),
            "timestamp": datetime.now().isoformat()
        }

        client.publish(TOPIC_SENSOR, json.dumps(data))
        print(f"→ Publish: {data}")
        time.sleep(3)

except KeyboardInterrupt:
    print("\nESP32 Simulator dihentikan.")
    client.loop_stop()
    client.disconnect()
