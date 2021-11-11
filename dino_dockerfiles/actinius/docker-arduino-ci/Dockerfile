FROM ubuntu:16.04

LABEL maintainer="Alex Tsamakos <alex@actinius.com>"

RUN apt-get update -qq \
  && apt -qq -y install \
               wget \
               curl \
               git \
               xz-utils \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

ADD get-version.sh /usr/local/bin/get-version.sh
RUN chmod +x /usr/local/bin/get-version.sh

ENV ARDUINO_VERSION 1.8.5

RUN wget -nv http://downloads.arduino.cc/arduino-${ARDUINO_VERSION}-linux64.tar.xz \
  && tar xvf arduino-${ARDUINO_VERSION}-linux64.tar.xz -C /usr/local/share \
  && ln -s /usr/local/share/arduino-${ARDUINO_VERSION} /usr/local/share/arduino \
  && ln -s /usr/local/share/arduino-${ARDUINO_VERSION}/arduino /usr/local/bin/arduino

RUN arduino --install-boards "arduino:samd" \
  && arduino --install-boards "arduino:sam"

CMD ["/bin/bash"]
