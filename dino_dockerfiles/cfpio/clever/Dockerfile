FROM ubuntu

# https://www.clever-cloud.com/doc/clever-tools/getting_started/

RUN apt-get update -y && apt-get install -y libcurl3-gnutls

ADD https://clever-tools.cellar.services.clever-cloud.com/releases/latest/clever-tools-latest_linux.tar.gz /clever-cloud/
RUN cd /clever-cloud && tar -xvf clever-tools-latest_linux.tar.gz
RUN mv /clever-cloud/* /usr/local/bin
COPY restart.sh /root/restart.sh
