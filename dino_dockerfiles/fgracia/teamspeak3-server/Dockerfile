FROM debian:10.7

LABEL maintainer="Frederic GRACIA <gracia.frederic@gmail.com>"

ENV VERSION=3.13.3

RUN apt-get update && \
    apt-get install -y curl bzip2
RUN apt-get clean

COPY ./startup.sh /startup.sh
RUN chmod +x /startup.sh

WORKDIR /opt
RUN curl -o teamspeak3-server_linux_amd64.tar.bz2 https://files.teamspeak-services.com/releases/server/${VERSION}/teamspeak3-server_linux_amd64-${VERSION}.tar.bz2
RUN tar xfj teamspeak3-server_linux_amd64.tar.bz2 && mv teamspeak3-server_linux_amd64 teamspeak
RUN rm -f teamspeak3-server_linux_amd64.tar.bz2

EXPOSE 9987/udp
EXPOSE 10011
EXPOSE 30033

VOLUME ["/data"]

CMD ["/startup.sh"]
