FROM python:3.7-slim-buster

RUN apt update && apt install -y libgl1-mesa-dev libglib2.0-0

RUN pip3 install Flask flasgger && \
    pip3 install wheel --upgrade

ENV CONSUMER_PORT '6100'
ENV MQTT_BROKER_ADDRESS "xxx.xxx.xxx.xxx"
ENV MQTT_BROKER_PORT 31888
ENV MQTT_APP_BITRATE_INFO_TOPIC "appBitrateInfo"
ENV MQTT_APP_MODE_INFO_TOPIC "appModeInfo"
ENV MQTT_CONNECTIVITY_TOPIC "connectivityInfo"
ENV MQTT_USER "user"
ENV MQTT_PASS "pass"
ENV VIDEO_STREAM="http://xxx.xxx.xxx.xxx:xxxx"

COPY . /notifications_consumer
WORKDIR /notifications_consumer

RUN python3 setup.py install

CMD ["python3", "-u", "src/run.py"]
