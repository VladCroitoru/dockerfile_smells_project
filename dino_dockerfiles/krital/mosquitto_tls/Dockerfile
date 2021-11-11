FROM ubuntu:14.04

MAINTAINER Alex Kritikos <alex@kritikal.org>

ENV DEBIAN_FRONTEND="noninteractive"
ENV MOSQUITTO_PORT="8883" 
ENV MOSQUITTO_SOURCE_DIR="/usr/local/src" 
ENV MOSQUITTO_CONFIG_DIR="/etc/mosquitto" 
ENV MOSQUITTO_VERSION="1.4.8" 
ENV MOSQUITTO_USER="mosquitto" 
ENV CERTIFICATE_DURATION="365"
ENV CA_FILE_PREFIX="ca" 
ENV CA_KEY_PASSWORD="capasswd" 
ENV CA_COUNTRY="GR" 
ENV CA_STATE="Attica" 
ENV CA_LOCALITY="Athens" 
ENV CA_ORGANIZATION="SYRIZA" 
ENV CA_COMMON_NAME="SYRIZA CA"
ENV SERVER_FILE_PREFIX="server" 
ENV SERVER_KEY_SIZE="2048" 
ENV SERVER_KEY_PASSWORD="serverpasswd" 
ENV SERVER_COUNTRY="GR" 
ENV SERVER_STATE="Attica" 
ENV SERVER_LOCALITY="Athens" 
ENV SERVER_ORGANIZATION="kritikal.org" 
ENV SERVER_DOMAIN="mosquitto.kritikal.org" 
ENV SERVER_COMMON_NAME="test.$SERVER_DOMAIN"
ENV ROOT_PASSWORD="Mosquitto!"

RUN apt-get update && apt-get upgrade -y && apt-get install wget build-essential libwrap0-dev libssl-dev python-distutils-extra libc-ares-dev uuid-dev openssl -y

RUN mkdir -p $MOSQUITTO_SOURCE_DIR
WORKDIR $MOSQUITTO_SOURCE_DIR
RUN wget http://mosquitto.org/files/source/mosquitto-$MOSQUITTO_VERSION.tar.gz
RUN tar xvzf ./mosquitto-$MOSQUITTO_VERSION.tar.gz
WORKDIR $MOSQUITTO_SOURCE_DIR/mosquitto-$MOSQUITTO_VERSION
RUN make && make install

RUN adduser --system --disabled-password --disabled-login $MOSQUITTO_USER

RUN echo "root:$ROOT_PASSWORD" | chpasswd

RUN mkdir -p $MOSQUITTO_CONFIG_DIR
WORKDIR $MOSQUITTO_CONFIG_DIR
RUN chown -R $MOSQUITTO_USER $MOSQUITTO_CONFIG_DIR

USER $MOSQUITTO_USER

WORKDIR $MOSQUITTO_CONFIG_DIR
RUN cd $MOSQUITTO_CONFIG_DIR
RUN openssl req -new -x509 -days $CERTIFICATE_DURATION -extensions v3_ca -keyout $CA_FILE_PREFIX.key -out $CA_FILE_PREFIX.crt -nodes -subj "/C=$CA_COUNTRY/ST=$CA_STATE/L=$CA_LOCALITY/O=$CA_ORGANIZATION/CN=$CA_COMMON_NAME" -passout pass:$CA_KEY_PASSWORD
RUN openssl genrsa -out $SERVER_FILE_PREFIX.key $SERVER_KEY_SIZE -passout pass:$SERVER_KEY_PASSWORD

RUN openssl req -out $SERVER_FILE_PREFIX.csr -key $SERVER_FILE_PREFIX.key -new -nodes -passin pass:$SERVER_KEY_PASSWORD -subj "/C=$SERVER_COUNTRY/ST=$SERVER_STATE/L=$SERVER_LOCALITY/O=$SERVER_ORGANIZATION/CN=$SERVER_COMMON_NAME"
RUN openssl x509 -req -in $SERVER_FILE_PREFIX.csr -CA $CA_FILE_PREFIX.crt -CAkey $CA_FILE_PREFIX.key -CAcreateserial -out $SERVER_FILE_PREFIX.crt -days $CERTIFICATE_DURATION -passin pass:$CA_KEY_PASSWORD

RUN cp $MOSQUITTO_CONFIG_DIR/mosquitto.conf.example $MOSQUITTO_CONFIG_DIR/mosquitto.conf
RUN echo "port $MOSQUITTO_PORT" >> $MOSQUITTO_CONFIG_DIR/mosquitto.conf
RUN echo "cafile $MOSQUITTO_CONFIG_DIR/$CA_FILE_PREFIX.crt" >> $MOSQUITTO_CONFIG_DIR/mosquitto.conf
RUN echo "certfile $MOSQUITTO_CONFIG_DIR/$SERVER_FILE_PREFIX.crt" >> $MOSQUITTO_CONFIG_DIR/mosquitto.conf
RUN echo "keyfile $MOSQUITTO_CONFIG_DIR/$SERVER_FILE_PREFIX.key" >> $MOSQUITTO_CONFIG_DIR/mosquitto.conf

EXPOSE $MOSQUITTO_PORT

ENTRYPOINT ["/usr/local/sbin/mosquitto", "-c", "/etc/mosquitto/mosquitto.conf"]
