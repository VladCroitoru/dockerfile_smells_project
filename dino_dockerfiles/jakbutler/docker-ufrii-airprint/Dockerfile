FROM golang:latest as builder

#########################################
##         DEPENDENCY INSTALL          ##
#########################################
RUN apt-get -o Acquire::Check-Valid-Until=false update && apt-get -y install \
    gcc libcups2-dev libavahi-client-dev && \
    rm -rf /var/lib/apt/lists/*

RUN go get github.com/google/cloud-print-connector/...

FROM debian:stretch-slim

MAINTAINER jakbutler

#########################################
##        ENVIRONMENTAL CONFIG         ##
#########################################
ENV CANON_DRIVER_URL='http://gdlp01.c-wss.com/gds/8/0100007658/08/linux-UFRII-drv-v370-uken-05.tar.gz'
ENV AIRPRINT_GENERATE_URL='https://raw.githubusercontent.com/tjfontaine/airprint-generate/fb98c1ded7625b1b15cbbc0f9ac004a799c7c1a6/airprint-generate.py'
ENV CUPS_USER_ADMIN=admin
ENV CUPS_USER_PASSWORD=secr3t
ENV TZ='America/Los_Angeles'
#ENV CUPS_CONFIG_DIR='/config'
#ENV AVAHI_SERVICE_DIR='/servces'

ENV DEBIAN_FRONTEND noninteractive

#########################################
##         DEPENDENCY INSTALL          ##
#########################################
RUN apt-get -o Acquire::Check-Valid-Until=false update && apt-get -y install \
    locales \
    cups \
    cups-client \
    cups-browsed \
    cups-bsd \
    cups-filters \
    cups-pdf \
    avahi-daemon \
    avahi-discover \
    avahi-utils \
    libnss-mdns \
    mdns-scan \
    whois \
    autoconf \
    automake \
    curl \
    inotify-tools \
    libglade2-0 \
    libpango1.0-0 \
    libpng16-16 \
    python \
	python-cups \
	wget && \
	apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Remove backends that don't make sense for container
RUN rm /usr/lib/cups/backend/parallel && \
    rm /usr/lib/cups/backend/serial && \
    rm /usr/lib/cups/backend/usb

#########################################
##             CUPS Config             ##
#########################################
RUN mkdir -p /usr/etc/cups && \
    mkdir -p /usr/etc/cups/interfaces && \
    mkdir -p /usr/etc/cups/ppd && \
    mkdir -p /usr/etc/cups/ssl && \
    chmod -R 777 /usr/etc/cups
COPY cups/* /usr/etc/cups/

## Add proper mimetypes for iOS
COPY mime/airprint.convs /share/cups/mime/airprint.convs
COPY mime/airprint.types /share/cups/mime/airprint.types

#########################################
##            Script Setup             ##
#########################################
COPY start-cups.sh /root/start-cups.sh
RUN chmod +x /root/start-cups.sh

#########################################
##          AirPrint Setup             ##
#########################################
RUN mkdir -p /opt/airprint && \
    chmod -R 777 /opt/airprint && \
    wget --no-check-certificate $AIRPRINT_GENERATE_URL -P /opt/airprint/
RUN chmod 755 /opt/airprint/airprint-generate.py
COPY printer-update.sh /opt/airprint/printer-update.sh
RUN chmod +x /opt/airprint/printer-update.sh

#########################################
##      Google Cloud Print Setup       ##
#########################################
RUN useradd -s /usr/sbin/nologin -r -M cloud-print-connector && \
    mkdir -p /etc/cloud-print-connector && \
    mkdir -p /opt/cloud-print-connector && \
    chmod -R 777 /etc/cloud-print-connector && \
    chmod -R 777 /opt/cloud-print-connector
COPY --from=builder /go/bin/gcp* /opt/cloud-print-connector/
COPY cloud-print-connector.sh /etc/init.d/cloud-print-connector
RUN chmod 755 /opt/cloud-print-connector/gcp* && \
    chmod 755 /etc/init.d/cloud-print-connector && \
    ln -s /etc/init.d/cloud-print-connector /etc/rc0.d/K01cloud-print-connector && \
    ln -s /etc/init.d/cloud-print-connector /etc/rc1.d/K01cloud-print-connector && \
    ln -s /etc/init.d/cloud-print-connector /etc/rc2.d/S01cloud-print-connector && \
    ln -s /etc/init.d/cloud-print-connector /etc/rc3.d/S01cloud-print-connector && \
    ln -s /etc/init.d/cloud-print-connector /etc/rc4.d/S01cloud-print-connector && \
    ln -s /etc/init.d/cloud-print-connector /etc/rc5.d/S01cloud-print-connector && \
    ln -s /etc/init.d/cloud-print-connector /etc/rc6.d/K01cloud-print-connector

#########################################
##     Canon UFRII Drivers Install     ##
#########################################
RUN curl $CANON_DRIVER_URL | tar xz && \
    dpkg -i *-UFRII-*/64-bit_Driver/Debian/*common*.deb && \
    dpkg -i *-UFRII-*/64-bit_Driver/Debian/*ufr2*.deb && \
    dpkg -i *-UFRII-*/64-bit_Driver/Debian/*utility*.deb && \
    rm -rf *-UFRII-*

#########################################
##         EXPORTS AND VOLUMES         ##
#########################################
VOLUME /etc/cups/ \
       /etc/avahi/services/ \
       /var/log/cups \
       /etc/cloud-print-connector

#########################################
##               PORTS                 ##
#########################################
# Expose SMB printer sharing
EXPOSE 137/udp 139/tcp 445/tcp

# Expose LPD printer sharing
EXPOSE 515/tcp

# Expose IPP printer sharing
EXPOSE 631/tcp

# Expose avahi advertisement
EXPOSE 5353/udp

#########################################
##           Startup Command           ##
#########################################
CMD ["/root/start-cups.sh"]