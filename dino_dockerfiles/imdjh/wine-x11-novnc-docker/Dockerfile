FROM jedisct1/phusion-baseimage-latest
MAINTAINER archedraft

# Set correct environment variables
ENV HOME /root
ENV DEBIAN_FRONTEND noninteractive
ENV LC_ALL C.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8

RUN apt-get update &&  apt-get -y install xvfb \
                       x11vnc \
                       xdotool \
                       wget \
                       supervisor \
                       x11-apps \
                       net-tools && \
                       rm -rf /var/lib/apt/lists/*
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf

ENV DISPLAY :0.0

WORKDIR /root/
ADD novnc /root/novnc/

# Expose Port
EXPOSE 8080

CMD ["/usr/bin/supervisord"]
