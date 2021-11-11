FROM ubuntu:16.04

MAINTAINER Quentin Peten

ENV USER domoticz
ENV UID 1000
ENV MAKE_CORES 2

RUN apt-get update -q && apt-get install -qy \
        build-essential nano cmake git libboost-dev libboost-thread-dev libboost-system-dev \
	libsqlite3-dev curl libcurl4-openssl-dev libssl-dev libusb-dev zlib1g-dev python3-dev

RUN useradd --no-create-home -g users -G dialout --uid $UID $USER

WORKDIR "/src/domoticz"
RUN chown $USER /src/domoticz

RUN apt-get autoremove -qy wget && \
    rm -rf /var/lib/apt/lists/*

USER $USER

RUN git clone https://github.com/domoticz/domoticz.git .
RUN cmake -DCMAKE_BUILD_TYPE=Release . && make -j $MAKE_CORES

VOLUME /config

CMD /src/domoticz/domoticz -userdata /config -dbase /config/domoticz.db -log /config/log/domoticz.log -www 8080 -sslwww 0
