FROM debian:8
# INSTALL SOGO
RUN apt-key adv --keyserver keys.gnupg.net --recv-key 0x810273C4 && \
    apt-get update && \
    apt-get install apt-transport-https -y && \
    echo "deb http://packages.inverse.ca/SOGo/nightly/3/debian/ jessie jessie" >> /etc/apt/sources.list && \
    apt-get update && \
    apt-get install sogo sope4.9-gdl1-postgresql -y
# Install CONFD
ADD https://github.com/kelseyhightower/confd/releases/download/v0.11.0/confd-0.11.0-linux-amd64 /usr/local/bin/confd
RUN chmod +x /usr/local/bin/confd
# Install configure CADDY
ADD https://github.com/mholt/caddy/releases/download/v0.9.5/caddy_linux_amd64.tar.gz /tmp/
RUN tar -xzvf /tmp/caddy_linux_amd64.tar.gz && \
    mv caddy_linux_amd64 /usr/local/bin/caddy
# LOAD CONFD TEMPLATES
ADD files/confd /etc/confd
ADD run.sh ./run.sh
ENTRYPOINT "./run.sh"
