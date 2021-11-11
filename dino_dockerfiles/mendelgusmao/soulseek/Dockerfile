FROM debian:stretch-slim
MAINTAINER github.com/mendelgusmao

ENV DISPLAY :1
ENV SOULSEEK_DL "https://www.dropbox.com/s/7qh902qv2sxyp6p/SoulseekQt-2016-1-17-64bit.tgz?dl=1"

RUN apt-get -yy update \
    && apt-get -y install --no-install-recommends \
       ca-certificates libfontconfig1 libx11-6 libx11-xcb1 openbox supervisor \
       wget x11vnc xvfb

RUN addgroup soulseek \
    && useradd -m -s /bin/bash -g soulseek soulseek
WORKDIR /home/soulseek

ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf
ADD menu.xml /etc/xdg/openbox/menu.xml
ADD start /bin/start
RUN wget -qO- "$SOULSEEK_DL" | tar xzvf - -C /usr/bin --transform='s/.*/soulseek/'

RUN apt-get -y remove --purge wget ca-certificates; \
    apt-get -y autoremove --purge; \
    apt-get clean; \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/log/*

USER soulseek
EXPOSE 5900 2234 2235

CMD ["/bin/start"]
