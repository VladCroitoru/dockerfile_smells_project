FROM ubuntu:18.04
MAINTAINER giovanni.colapinto@gmail.com

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install -y --no-install-recommends --fix-missing\
    libgl-dev \
    qt5dxcb-plugin \
    libcurl3-gnutls \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/

ADD https://download.studio3t.com/robomongo/linux/robo3t-1.4.4-linux-x86_64-e6ac9ec.tar.gz /opt/robo3t.tar.gz
RUN cd /opt/ \
    && mkdir robo3t \
    && tar -C /opt/robo3t --strip-components 1 -xzf robo3t.tar.gz && rm robo3t.tar.gz \
    && ls /opt/robo3t

VOLUME /root/.3T
VOLUME /root/.config/3T

CMD /opt/robo3t/bin/robo3t

