FROM java:8

LABEL maintainer "j.stephenson@ossila.com"

ENV ARDUINO_IDE_VERSION 1.8.2

RUN apt-get update && apt-get install -y Xvfb wget xz-utils build-essential ctags && \
    wget -q -O- https://downloads.arduino.cc/arduino-${ARDUINO_IDE_VERSION}-linux64.tar.xz | tar xJ -C /opt && \
    ln -s /opt/arduino-${ARDUINO_IDE_VERSION}/arduino /usr/local/bin/ && \
    ln -s /opt/arduino-${ARDUINO_IDE_VERSION}/arduino-builder /usr/local/bin/ && \
    ln -s /opt/arduino-${ARDUINO_IDE_VERSION} /opt/arduino && \
    /sbin/start-stop-daemon --start --quiet --pidfile /tmp/custom_xvfb_1.pid --make-pidfile --background --exec /usr/bin/Xvfb -- :1 -ac -screen 0 1280x1024x16 && \
    arduino --install-boards "arduino:sam:1.6.10" && \
    /sbin/start-stop-daemon --stop --quiet --pidfile /tmp/custom_xvfb_1.pid && \
    apt-get remove -y Xvfb && \
    apt-get autoremove -y && \
    apt-get autoclean -y

ENTRYPOINT [ ]
