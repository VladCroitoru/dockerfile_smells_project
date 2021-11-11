FROM mrfroop/openjdk-alpine-gradle AS BUILD_IMAGE

#build knx2mqtt.jar
ENV APP_HOME=/app/
WORKDIR $APP_HOME
COPY src $APP_HOME/src
COPY build.gradle $APP_HOME/build.gradle
RUN gradle jar

#Build run image
FROM openjdk:jre-alpine
ENV APP_HOME=/app/
WORKDIR $APP_HOME
COPY --from=BUILD_IMAGE /app/build/libs/knx2mqtt.jar /app/
VOLUME ["/data"]
CMD java -Dknx2mqtt.knx.nat=NAT \
    -Dknx2mqtt.knx.ip=$knx2mqtt_knx_ip \
    -Dknx2mqtt.mqtt.server=$knx2mqtt_mqtt_server \
    -Dknx2mqtt.knx.ets5projectfile=/data/$knx2mqtt_knx_ets5projectfile \
    -jar knx2mqtt.jar 