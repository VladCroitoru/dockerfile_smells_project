FROM busybox@sha256:16a2a52884c2a9481ed267c2d46483eac7693b813a63132368ab098a71303f8a
MAINTAINER Sune Keller <sune.keller@gmail.com>
ENV EVENTSTORE_VERSION=3.3.0
RUN mkdir /opt && wget -O- http://download.geteventstore.com/binaries/EventStore-OSS-Ubuntu-v$EVENTSTORE_VERSION.tar.gz | tar xz -C /opt
EXPOSE 2112/tcp
EXPOSE 1113/tcp
VOLUME [/data/db]
VOLUME [/data/logs]
WORKDIR /opt/EventStore-OSS-Ubuntu-v3.1.0
CMD ["sudo" "./run-node.sh" "--ext-tcp-port=1113" "--db" "/data/db" "--log" "/data/logs" "--ext-ip=0.0.0.0" "--ext-http-prefixes=http://*:2112/"]
