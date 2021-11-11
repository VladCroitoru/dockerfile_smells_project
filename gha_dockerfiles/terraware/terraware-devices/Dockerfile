FROM python:3.8.5-buster AS build

RUN apt-get update \
    && apt-get install -y \
        cmake \
        curl \
        g++ \
        gcc \
        libbluetooth-dev \
        libglib2.0-0 \
        libusb-1.0-0-dev \
        make \
        pkg-config \
        wget \
        xz-utils

WORKDIR /tmp
RUN curl -Ls https://github.com/greatscottgadgets/libbtbb/archive/2020-12-R1.tar.gz | tar xfz -
WORKDIR /tmp/libbtbb-2020-12-R1/build
RUN cmake .. && make install && ldconfig

WORKDIR /tmp
RUN curl -Ls https://github.com/greatscottgadgets/ubertooth/releases/download/2020-12-R1/ubertooth-2020-12-R1.tar.xz | tar xfJ -
WORKDIR /tmp/ubertooth-2020-12-R1/host/build
RUN cmake .. && make install && ldconfig

WORKDIR /app

# Download the latest entrypoint script from Balena. This will set up the
# udev daemon and correctly mount devices into the container.
RUN wget -q https://raw.githubusercontent.com/balena-io-library/base-images/master/balena-base-images/aarch64/debian/buster/run/entry.sh

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

FROM python:3.8.5-slim-buster

WORKDIR /app

RUN apt-get update \
    && apt-get install -y \
        libbluetooth3 \
        libglib2.0-0 \
        libusb-1.0.0 \
        ssh \
        udev \
        nut \
    && apt-get clean \
    && rm -rf /var/cache/apt/lists

COPY --from=build /etc/udev/rules.d/40-ubertooth.rules /etc/udev/rules.d/40-ubertooth.rules
COPY --from=build /app/entry.sh /app/entry.sh

# /usr/local contains Python libraries as well as Ubertooth commands and libraries.
COPY --from=build /usr/local /usr/local
RUN ldconfig

COPY balena-config.yaml config.yaml main.py ble_scan.py /app/
COPY specs /app/specs
COPY terraware_devices /app/terraware_devices

COPY ups.conf nut.conf /etc/nut/

# Uncomment these two lines to push a local site JSON file to the Pi for testing in local dev mode.
#COPY sample_local.yaml /app/local.yaml
#COPY sample-site.json /app/sample-site.json

ENTRYPOINT ["/bin/bash", "/app/entry.sh"]
CMD ["/usr/local/bin/python3", "main.py"]
