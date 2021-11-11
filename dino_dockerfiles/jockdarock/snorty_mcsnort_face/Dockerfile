FROM alpine:3.5

#Change these values dependant on your environment
ENV MQTT="test.mosquitto.org" MQTTPORT=1883 NETINT="eth0"

RUN    echo "http://dl-cdn.alpinelinux.org/alpine/edge/main" > /etc/apk/repositories \
    && apk add -Uuv --no-cache snort daq supervisor python2 python3 \
    && apk upgrade -v --available --no-cache

COPY requirements.txt .
RUN    pip3 install --no-cache-dir --upgrade pip setuptools wheel \
    && pip3 install --no-cache-dir -r requirements.txt

#Copy applications
COPY snort_socket.py .
COPY snort_parser.py .
COPY snort_api.py .
COPY super_snort.conf .
COPY simple_snort.conf /etc/snort/simple_snort.conf
COPY rules /etc/snort/rules

RUN sed -i '/import alert/c\import snortunsock.alert as alert' /usr/lib/python3.6/site-packages/snortunsock/snort_listener.py

EXPOSE 5000

#run processes from Supervisor
ENTRYPOINT ["/usr/bin/supervisord","-c","/super_snort.conf"]
