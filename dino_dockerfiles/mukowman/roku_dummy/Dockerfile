FROM python:3
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
ENV HOST_IP=127.0.0.1
ENV HOST_PORT=8060
ENV MQTT_HOST=127.0.0.1
ENV MQTT_PORT=1883
ENV MQTT_USERNAME ""
ENV MQTT_PASSWORD ""

CMD [ "python", "./roku.py" ]

EXPOSE 8060/TCP
