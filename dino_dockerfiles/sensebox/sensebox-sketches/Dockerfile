FROM debian:9.4-slim as builder

ENV IDE_VERSION=1.8.13 \
  SENSEBOXCORE_VERSION=1.4.2 \
  ARDUINO_SAMD_VERSION=1.8.11 \
  ARDUINO_AVR_VERSION=1.8.3 \
  SENSEBOXCORE_URL=https://raw.githubusercontent.com/sensebox/senseBoxMCU-core/master/package_sensebox_index.json \
  SENSEBOX_LIBRARY_URL=https://github.com/sensebox/senseBox_library/archive/master.zip \
  TELEGRAM_LIBRARY_URL=https://github.com/witnessmenow/Universal-Arduino-Telegram-Bot/archive/v1.1.0.zip \
  ARDUINO_JSON_LIBRARY_URL=https://github.com/bblanchon/ArduinoJson/releases/download/v5.13.5/ArduinoJson-v5.13.5.zip \
  TTN_ARDUINO_LIBRARY_URL=https://github.com/TheThingsNetwork/arduino-device-lib/archive/v2.5.15.zip \
  BSEC_LIBRARY_URL=https://github.com/BoschSensortec/BSEC-Arduino-library/archive/v1.5.1474.zip \
  GPS_LIBRARY_URL=https://github.com/sparkfun/SparkFun_u-blox_GNSS_Arduino_Library/archive/v2.0.3.zip\
  MQTT_LIBRARY_URL=https://github.com/adafruit/Adafruit_MQTT_Library/archive/2.1.0.zip \
  NEWPING_LIBRARY_URL=https://bitbucket.org/teckel12/arduino-new-ping/downloads/NewPing_v1.9.1.zip \
  PHYPHOX_LIBRARY_URL=https://github.com/sensebox/phyphox-arduino/archive/refs/heads/master.zip \ 
  PATH=$PATH:/arduino-ide

RUN apt-get update && apt-get install -y xz-utils unzip wget \
  && wget http://downloads.arduino.cc/arduino-$IDE_VERSION-linux64.tar.xz \
  && tar xf arduino-$IDE_VERSION-linux64.tar.xz \
  && mv arduino-$IDE_VERSION /arduino-ide \
  && wget -O senseBox_Library.zip $SENSEBOX_LIBRARY_URL \
  && unzip senseBox_Library.zip -d /arduino-ide/libraries \
  && wget -O telegram_Library.zip $TELEGRAM_LIBRARY_URL \
  && unzip telegram_Library.zip -d /arduino-ide/libraries \
  && wget -O arduino_json_Library.zip $ARDUINO_JSON_LIBRARY_URL \
  && unzip arduino_json_Library.zip -d /arduino-ide/libraries \
  && wget -O ttn_arduino_Library.zip $TTN_ARDUINO_LIBRARY_URL \
  && unzip ttn_arduino_Library.zip -d /arduino-ide/libraries \
  && wget -O bsec_Library.zip $BSEC_LIBRARY_URL \
  && unzip bsec_Library.zip -d /arduino-ide/libraries \
  && wget -O gps_Library.zip $GPS_LIBRARY_URL \
  && unzip gps_Library.zip -d /arduino-ide/libraries \
  && wget -O mqtt_Library.zip $MQTT_LIBRARY_URL \
  && unzip mqtt_Library.zip -d /arduino-ide/libraries \
  && wget -O newping_Library.zip $NEWPING_LIBRARY_URL \
  && unzip newping_Library.zip -d /arduino-ide/libraries \
  && wget -O phyphox_Library.zip $PHYPHOX_LIBRARY_URL \
  && unzip phyphox_Library.zip -d /arduino-ide/libraries \
  && arduino --pref boardsmanager.additional.urls=$SENSEBOXCORE_URL --install-boards sensebox:samd:$SENSEBOXCORE_VERSION \
  && arduino --install-boards arduino:samd:$ARDUINO_SAMD_VERSION \
  && arduino --install-boards arduino:avr:$ARDUINO_AVR_VERSION \
  && mkdir -p /arduino-ide/build-cache \
  && mv /root/.arduino15/packages /arduino-ide/packages \
  && apt-get purge -y xz-utils unzip wget \
  && apt-get autoremove -y \
  && apt-get clean \
  && rm -rf arduino-$IDE_VERSION-linux64.tar.xz senseBox_Library.zip /var/lib/apt/lists/* /tmp/* /var/tmp/* \
  && bash -c 'rm -rf /arduino-ide/{java,lib,reference,examples,arduino,install.sh,revisions.txt,uninstall.sh}' \
  && find /arduino-ide -type d -name "examples" -exec rm -rf \;

FROM node:8-slim

WORKDIR /app

ENV NODE_ENV=production

COPY package.json /app
COPY yarn.lock /app

RUN yarn install --pure-lockfile --production

COPY src /app/src
COPY --from=builder /arduino-ide /app/src/arduino-ide

COPY platform.txt /app/src/arduino-ide/packages/arduino/hardware/samd/1.8.11

CMD ["yarn","start"]
