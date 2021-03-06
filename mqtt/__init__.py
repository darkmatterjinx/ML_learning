import paho.mqtt.client as mqtt
import json


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    client.subscribe("chat")
    client.publish("chat", json.dumps({"user": user, "say": "Hello,anyone!"}))


def on_message(client, userdata, msg):
    payload = json.loads(msg.payload.decode())
    print(payload["user"]  + ":" + payload["say"])


if __name__ == '__main__':
    client = mqtt.Client()
    client.username_pw_set("admin", "password")  # 必须设置，否则会返回「Connected with result code 4」
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("106.14.165.164", 1883, 60)

    user = input("请输入名称:")
    client.user_data_set(user)

    client.loop_start()

    while True:
        str = input()
        if str:
            client.publish("chat", json.dumps({"user": user, "say": str}))
