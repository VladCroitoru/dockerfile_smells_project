FROM debian:stretch

MAINTAINER monkeydri <monkeydri@github.com>

RUN apt-get update && apt-get -y install \
cups=2.2.1* \
cups-filters \
cups-pdf \
whois \
usbutils \
lib32stdc++6 \
lib32gcc1 \
libc6-i386 \
wget \
&& rm -rf /var/lib/apt/lists/*

# Remove backends that don't make sense for container
RUN rm /usr/lib/cups/backend/parallel \
  && rm /usr/lib/cups/backend/serial

COPY etc-cups /etc/cups

VOLUME /etc/cups/ /var/log/cups /var/spool/cups /var/cache/cups

COPY etc-pam.d-cups /etc/pam.d/cups

# Copy brother driver installer and installer script
COPY linux-brprinter-installer-2.1.1-1 /root/linux-brprinter-installer-2.1.1-1
RUN chmod +x /root/linux-brprinter-installer-2.1.1-1
COPY install_brother_driver.sh /root/install_brother_driver.sh
RUN chmod +x /root/install_brother_driver.sh

COPY start_cups.sh /root/start_cups.sh
RUN chmod +x /root/start_cups.sh \
  && mkdir -p /etc/cups/ssl

CMD /root/install_brother_driver.sh & /root/start_cups.sh

EXPOSE 631
