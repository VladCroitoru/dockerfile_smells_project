FROM debian:testing

MAINTAINER Lars Boegild Thomsen <lbthomsen@gmail.com>

RUN     export DEBIAN_FRONTEND=noninteractive && \
        apt-get -y update && \
        apt-get install -yq curl 

RUN curl -SL http://www.mersenne.org/ftp_root/gimps/p95v294b8.linux64.tar.gz | tar -xz mprime && mv mprime /usr/sbin && chmod +x /usr/sbin/mprime

COPY runprime /
RUN chmod +x ./runprime

RUN mkdir prime

CMD ["/bin/bash", "-c", "./runprime"]

