FROM ubuntu:18.04

ENTRYPOINT ["/usr/local/bin/start_ibeacon_scanning"]

RUN env DEBIAN_FRONTEND=noninteractive \
    apt-get update && \
    apt-get install -yy \
        bc \
        bluez \
        bluez-hcidump \
        moreutils \
        rfkill \
        socat && \
    apt-get clean

COPY bin/* /usr/local/bin/
