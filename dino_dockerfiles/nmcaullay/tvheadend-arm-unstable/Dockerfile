#FROM resin/rpi-raspbian:jessie
#FROM hypriot/rpi-alpine-scratch
FROM resin/armv7hf-debian-qemu

RUN [ "cross-build-start" ]

#Create the HTS user (1000), and add to user group (100)
RUN useradd -u 1000 -g 100 hts

# Install dependencies, build and install tvheadend
RUN apt-get update -qq
RUN apt-get install -qy \
    build-essential pkg-config libssl-dev git bzip2 wget cmake \
    libavahi-client-dev zlib1g-dev libcurl4-gnutls-dev python \
    liburiparser1 liburiparser-dev gettext \
    libhdhomerun-dev dvb-apps
#    cd /tmp && \
#    git clone https://github.com/tvheadend/tvheadend.git && \
#    cd tvheadend && \
#    git reset --hard HEAD && \
#    git pull && \
#    ./configure --enable-hdhomerun_client --enable-hdhomerun_static --enable-libffmpeg_static --prefix=/usr && \
#    make && \
#    make install && \
#    rm -r /tmp/tvheadend && apt-get purge -qq build-essential pkg-config git && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


RUN [ "cross-build-end" ]  
