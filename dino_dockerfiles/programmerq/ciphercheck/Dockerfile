FROM debian:jessie
MAINTAINER Jeff Anderson <jeff@docker.com>
RUN apt-get -y update
RUN apt-get -y install openssl
ADD ciphers.sh /ciphers.sh
ENTRYPOINT ["/ciphers.sh"]
