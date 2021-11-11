FROM ubuntu:17.10

RUN set -xe && apt update && apt install -y curl libusb-1.0-0 libhidapi-hidraw0 udev usbutils && \
    mkdir -p /opt/flirc && curl -sSL http://apt.flirc.tv/arch/x64/binary/flirc.latest.x86_64.tar.gz | tar xz -C /opt/flirc --strip-components=1 && \
    cp /opt/flirc/99-flirc.rules /etc/udev/rules.d/ && \
    cp /opt/flirc/flirc_util /usr/local/bin && \ 
    apt purge -y curl && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

CMD bash
