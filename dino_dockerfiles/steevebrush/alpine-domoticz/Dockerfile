FROM alpine:latest
LABEL maintainer="stéphane BROSSE <stevebrush@gmail.com>"

ENV TIMEZONE Europe/Paris

RUN set -x && \
	buildDeps='build-base cmake git libressl-dev libexecinfo-dev boost-dev zlib-dev curl-dev libusb-compat-dev eudev-dev coreutils linux-headers gmp-dev' && \
	apk add --no-cache $buildDeps && \
	apk add --no-cache libssl1.0 python3 python3-dev boost-thread boost-system boost-date_time zlib curl libcurl libusb libusb-compat udev gmp tzdata && \
    cp /usr/share/zoneinfo/${TIMEZONE} /etc/localtime && \
    echo "${TIMEZONE}" > /etc/TZ &&\
	git clone --depth 2 https://github.com/domoticz/domoticz.git /src/domoticz && \
	cd /src/domoticz && \
	git fetch --unshallow && \
	git clone --depth 2 https://github.com/OpenZWave/open-zwave.git /src/open-zwave && \
	git clone --depth 2 https://github.com/mjg59/python-broadlink /src/python-broadlink && \
	sed -i -e "s/sys\/poll.h/poll.h/g" /src/domoticz/httpclient/sock_port.h && \
    sed -i -e "s/sys\/errno.h/errno.h/g" /src/domoticz/hardware/csocket.cpp && \
    sed -i -e "s/sys\/signal.h/signal.h/g" /src/domoticz/hardware/serial/impl/unix.cpp && \
    sed -i -e "s/sys\/poll.h/poll.h/g" /usr/include/boost/asio/detail/socket_types.hpp && \
    sed -i -e "s/pycrypto==2.6.1/pycryptodome==3.4.7/g" /src/python-broadlink/setup.py && \
    cd /src/open-zwave && \
    make && \
    ln -s /src/open-zwave /src/open-zwave-read-only && \
    cd /src/python-broadlink && \
	python3 setup.py install && \
	cd /src/domoticz && \
    cmake -DCMAKE_BUILD_TYPE=Release -Wno-dev -DHAVE_EXECINFO_H=0 . && \
    make && \
    make install && \
    apk del $buildDeps && \
    cp -r /src/domoticz/dzVents /opt/domoticz/ && \
    rm -rf /src

VOLUME /config

EXPOSE 9080

ENTRYPOINT ["/opt/domoticz/domoticz", "-dbase", "/config/domoticz.db", "-log", "/config/domoticz.log", "-sslwww", "0"]
CMD ["-www", "9080"]
