FROM alpine

MAINTAINER Yannik Ehlert <kontakt@yanniks.de>

RUN apk add --no-cache perl perl-device-serialport perl-xml-libxml-simple \
perl-libwww perl-xml-parser perl-json perl-module-pluggable perl-dev tzdata && \
adduser -S -D -h /opt/fhem -G dialout fhem
RUN apk add --no-cache --repository http://dl-3.alpinelinux.org/alpine/edge/testing/ \
--allow-untrusted perl-soap-lite
RUN mkdir -p /opt/fhem && chown -R fhem:dialout /opt/fhem && \
cd /opt/fhem && \
wget http://fhem.de/fhem-5.8.tar.gz && \
tar -xzf fhem-5.8.tar.gz -C /tmp/ && \
rm fhem-5.8.tar.gz && \
cp -R /tmp/fhem-5.8/* ./ && \
rm -r /tmp/fhem-5.8/ && \
chown -R fhem:dialout /opt/fhem && \
/usr/bin/cpan App::cpanminus && rm -rf /root/.cpan

# Set the timezone
RUN cp /usr/share/zoneinfo/Europe/Berlin /etc/localtime && \
echo "Europe/Berlin" > /etc/timezone

# Install cpan modules
RUN cpan install Net::MQTT:Simple Net::MQTT:Constants

COPY fhem-foreground /usr/bin/fhem-foreground
RUN chmod +x /usr/bin/fhem-foreground

WORKDIR /opt/fhem/
VOLUME ["/opt/fhem"]
EXPOSE 8083

USER fhem:dialout
CMD ["/usr/bin/fhem-foreground"]
