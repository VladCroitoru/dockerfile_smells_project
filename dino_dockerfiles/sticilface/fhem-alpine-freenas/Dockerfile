FROM lsiobase/alpine
LABEL maintainer sticilface <amelvin@gmail.com>
LABEL org.freenas.interactive="false" 		\
      org.freenas.version="3.8.008"		\
      org.freenas.upgradeable="true"		\
      org.freenas.expose-ports-at-host="true"	\
      org.freenas.autostart="true"		\
      org.freenas.capabilities-add="NET_BROADCAST" \
      org.freenas.web-ui-protocol="http"	\
      org.freenas.web-ui-port=8083		\
      org.freenas.web-ui-path="fhem"		\
      org.freenas.port-mappings="8083:8083/tcp,8084:8084/tcp,8085:8085/tcp"			\
      org.freenas.volumes="[							\
          {												\
              \"name\": \"/app/fhem\",					\
              \"descr\": \"Storage space\",				\
              \"optional\": true						\
          }												\
      ]"												\
      org.freenas.settings="[ 							\
          {												\
              \"env\": \"TZ\",							\
              \"descr\": \"Timezone eg Europe/London\",	\
              \"optional\": true						\
          },											\
          {												\
              \"env\": \"ADVERTISE_IP\",				\
              \"descr\": \"http://<hostIPAddress>:8083/fhem\",	\
              \"optional\": true						\
          },											\
          {												\
              \"env\": \"ALLOWED_NETWORKS\",			\
              \"descr\": \"IP/mask[,IP/mask]\",			\
              \"optional\": true						\
          },											\
          {												\
              \"env\": \"PUID\",						\
              \"descr\": \"Fhem User ID\",				\
              \"optional\": true						\
          },											\
          {												\
              \"env\": \"PGID\",						\
              \"descr\": \"Fhem Group ID\",				\
              \"optional\": true						\
          }  											\
       ]"

RUN apk add --no-cache --update \
	wget  						\
    nano 						\
    perl         \
    perl-socket  \
    perl-switch  \
    perl-sys-hostname-long   \
    perl-json \
    perl-io-socket-ssl \
    perl-crypt-openssl-rsa \
    perl-crypt-openssl-dsa \
    perl-xml-simple   \
    perl-socket 

RUN mkdir -p /usr/src/perl

ADD https://raw.githubusercontent.com/miyagawa/cpanminus/master/cpanm /usr/src/perl
ADD http://www.dhs-computertechnik.de/downloads/fhem-cvs.tgz /usr/local/fhem.tgz

RUN buildDeps='gcc build-base make' \
	&& cd /usr/src/perl \
    && apk add --no-cache --update $buildDeps \
    && chmod +x cpanm \
    && ./cpanm App::cpanminus \
    && rm -fr ./cpanm /root/.cpanm /usr/src/perl 

RUN cpanm Net::MQTT::Simple  \
	Net::MQTT::Constants \
	Net::Bonjour

COPY ./etc /etc
ENV TZ Europe/London

VOLUME /app/fhem

