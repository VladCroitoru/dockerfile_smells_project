# Build container with all build deps and builds deb package
FROM debian:9 as builder

RUN sed -i 's/deb\.debian\.org/cloudfront\.debian\.net/g' /etc/apt/sources.list

RUN apt-get update && apt-get install -y git && apt-get clean

RUN git clone https://github.com/sipwise/rtpengine.git /rtpengine
WORKDIR /rtpengine

RUN apt-get update && apt-get install -y \
       build-essential \
       dpkg-dev \
       debhelper \
       iptables-dev \
       netcat \
       libcurl4-openssl-dev \
       libglib2.0-dev \
       libhiredis-dev \
       libpcre3-dev \
       libssl-dev \
       markdown \
       libxmlrpc-core-c3-dev \
       nfs-common \
       dkms \
       default-libmysqlclient-dev \
       libavcodec-dev \
       libavfilter-dev \
       libavformat-dev \
       libavresample-dev \
       libavutil-dev \
       libevent-dev \
       libjson-glib-dev \
       libpcap-dev \
       git \
    && ( ( apt-get install -y linux-headers-$(uname -r) linux-image-$(uname -r) && \
      module-assistant update && \
      module-assistant auto-install ngcp-rtpengine-kernel-source ) || true ) \
    && apt-get clean && rm -rf /var/lib/apt/lists

RUN dpkg-checkbuilddeps
RUN dpkg-buildpackage -b -us -uc

# Smaller container to just install the deb and run it
FROM debian:9

COPY --from=builder /*.deb /

#Install some tools
RUN apt-get update && apt-get install -y gpg wget curl && apt-get clean

#Get the kope.io repo and gpg key
RUN wget https://dist-kope-io.s3.amazonaws.com/apt/kopeio.gpg.key -O /kopeio.gpg.key
RUN apt-key add /kopeio.gpg.key
RUN echo "deb http://dist.kope.io/apt jessie main" >> /etc/apt/sources.list.d/kope.io.list

#Install the deps and debs
RUN apt-get update && apt-get install -y \
    libbencode-perl \
    libcrypt-rijndael-perl \
    libdigest-hmac-perl \
    libio-socket-inet6-perl \
    libsocket6-perl \
    iptables \
    /*.deb \
    && apt-get clean && rm -rf /var/lib/apt/*

# We need some environment variables to work please review and modify
ENV RUN_RTPENGINE=yes
ENV LISTEN_TCP=25060
ENV LISTEN_UDP=12222
ENV LISTEN_NG=22222
ENV LISTEN_CLI=9900
ENV TIMEOUT=60
ENV SILENT_TIMEOUT=3600
ENV PIDFILE=/var/run/ngcp-rtpengine-daemon.pid
ENV FORK=no
ENV TABLE=0
ENV PORT_MIN=16384
ENV PORT_MAX=16485
ENV LOG_LEVEL=7

# Get the startup script.  It's long and complicated
COPY run.sh /run.sh
RUN chmod 755 /run.sh

CMD /run.sh
