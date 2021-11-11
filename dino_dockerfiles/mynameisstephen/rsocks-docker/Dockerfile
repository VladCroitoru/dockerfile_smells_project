FROM phusion/baseimage:0.9.18

ENV HOME /root
ENV DEBIAN_FRONTEND noninteractive

# Use baseimage-docker's init system
CMD ["/sbin/my_init"]

RUN \
 usermod -u 99 nobody && \
 usermod -g 100 nobody && \
 usermod -d /home nobody && \
 chown -R nobody:users /home

RUN apt-get update
RUN apt-get install -y wget software-properties-common python-software-properties
RUN wget -q -O - https://bootstrap.pypa.io/get-pip.py | sudo python -
RUN pip install rsocks

#SET CONFIG directory
VOLUME /config

# Add rsocks to runit RUN mkdir /etc/service/rsocks
ADD rsocks-run.sh /etc/service/rsocks/run
RUN chmod +x /etc/service/rsocks/run
ADD rsocks-finish.sh /etc/service/rsocks/finish
RUN chmod +x /etc/service/rsocks/finish