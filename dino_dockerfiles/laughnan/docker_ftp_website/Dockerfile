FROM debian:stable-slim

ENV DEBIAN_FRONTEND noninteractive

RUN mkdir -p /root/work/
WORKDIR /root/work/

RUN apt-get -y update && apt-get -y install git

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/man/?? /usr/share/man/??_*

CMD git help