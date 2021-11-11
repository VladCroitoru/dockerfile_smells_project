FROM debian:9

RUN apt-get update \
    && apt-get install -y build-essential wget openjdk-8-jre avr-libc avrdude binutils-avr xz-utils

ENV ARDUINO_IDE_VERSION 1.8.10

RUN (wget -q -O- https://downloads.arduino.cc/arduino-${ARDUINO_IDE_VERSION}-linux64.tar.xz \
    | tar xJC /usr/local/share \
    && ln -s /usr/local/share/arduino-${ARDUINO_IDE_VERSION} /usr/local/share/arduino \
    && ln -s /usr/local/share/arduino-${ARDUINO_IDE_VERSION}/arduino /usr/local/bin/arduino)





