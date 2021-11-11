FROM debian:jessie 
MAINTAINER Dcylabs <dcylabs@gmail.com>

RUN apt-get update 
RUN apt-get install -y git autoconf libtool libpcsclite-dev libusb-1.0-0 libusb-1.0-0-dev libusb-dev make automake pkg-config

RUN mkdir -p /var/nfc

# Install libnfc
WORKDIR /var/nfc 
RUN git clone https://github.com/nfc-tools/libnfc.git
WORKDIR /var/nfc/libnfc 
RUN autoreconf -vis
RUN ./configure --with-drivers=all --sysconfdir=/etc --prefix=/usr
RUN make clean 
RUN make install all
RUN mkdir /etc/nfc
RUN mkdir /etc/nfc/devices.d
RUN cp contrib/libnfc/pn532_via_uart2usb.conf.sample /etc/nfc/devices.d/pn532_via_uart2usb.conf

# Install MFCUK 
WORKDIR /var/nfc
RUN git clone https://github.com/nfc-tools/mfcuk.git
WORKDIR /var/nfc/mfcuk 
RUN autoreconf -vis
RUN ./configure
RUN make install all 

# Install MFOC 
WORKDIR /var/nfc
RUN git clone https://github.com/nfc-tools/mfoc.git
WORKDIR /var/nfc/mfoc
RUN autoreconf -vis
RUN ./configure
RUN make install all

# Create workspace 
RUN mkdir /workspace
WORKDIR /workspace
