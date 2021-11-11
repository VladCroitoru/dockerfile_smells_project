FROM ubuntu:14.04.5
RUN mkdir -p /homebridge && \
  mkdir -p /var/run/dbus && \
	mkdir -p ~/.homebridge
WORKDIR /homebridge/
RUN BUILD_PACKAGES='curl git build-essential python' && \
  apt-get update && \
  apt-get install -y  $BUILD_PACKAGES avahi-daemon avahi-discover libnss-mdns libavahi-compat-libdnssd-dev && \
  curl -L https://deb.nodesource.com/setup_5.x | bash - && \
  apt-get install -y nodejs  && \
  npm install --unsafe-perm -g homebridge homebridge-wink && \
  npm cache clean && rm -rf && \
  apt-get remove --purge -y $BUILD_PACKAGES  && \
  rm -rf /var/lib/apt/lists/*
USER root
COPY config.json /root/.homebridge
RUN ls /root/.homebridge
EXPOSE 5353 51826
COPY run.sh /homebridge/run.sh
RUN chmod a=x /homebridge/run.sh
CMD ["/homebridge/run.sh"]
