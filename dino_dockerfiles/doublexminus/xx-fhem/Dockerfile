FROM alpine:latest

MAINTAINER doublexminus <samson@vgraevenitz.de>

RUN apk add --update perl-device-serialport \
                     perl-io-socket-ssl \
                     perl-libwww \
                     perl-xml-simple \
					 perl-utils \
					 yaml \
					 make \
					 gcc \
					 openssh-client \
					 sshpass \
					 musl-dev \
					 perl-dev \
					 perl-json \
    && rm -rf /var/cache/apk/*

RUN apk add --no-cache -X http://dl-4.alpinelinux.org/alpine/edge/testing perl-soap-lite	
	
RUN mkdir -p /opt/fhem

RUN cpan install Log::Log4perl \
					Net::MQTT:Simple \
					Net::MQTT:Constants \
					HTML::TableExtract \
					Soap::Lite \
					Date::Parse \
					Net::Telnet \
					INC \
					LWP::Protocol::https \
					Crypt::Cipher::AES \
					Mozilla::CA \
					Crypt::CBC
					
VOLUME /opt/fhem

EXPOSE 8083
EXPOSE 6767/udp

ADD startfhem.sh /usr/local/bin/startfhem.sh
RUN chmod a+x /usr/local/bin/startfhem.sh

WORKDIR /opt/fhem

ENTRYPOINT ["/usr/local/bin/startfhem.sh"]
