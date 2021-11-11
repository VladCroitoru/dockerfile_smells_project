# Dockerfile to run the JKA demo bot
FROM ubuntu:16.04
MAINTAINER Dan Padgett <dumbledore3@gmail.com>

RUN apt-get update && \
      apt-get install -y locales libcurl3-gnutls

RUN cp /usr/share/i18n/charmaps/CP1252.gz /tmp && \
    cd /tmp && \
    gzip -d CP1252.gz && \
    localedef -f /tmp/CP1252 -i /usr/share/i18n/locales/en_US  /usr/lib/locale/en_US.CP1252

RUN cp /usr/share/i18n/charmaps/UTF-8.gz /tmp && \
    cd /tmp && \
    gzip -d UTF-8.gz && \
    localedef -f /tmp/UTF-8 -i /usr/share/i18n/locales/en_US  /usr/lib/locale/en_US.UTF-8

RUN useradd -ms /bin/bash demobot

# copy the nice dotfiles that dockerfile/ubuntu gives us:
RUN cd && cp -R .bashrc .profile /home/demobot

WORKDIR /home/demobot

RUN chown -R demobot:demobot /home/demobot

USER demobot
ENV HOME /home/demobot
ENV USER demobot

# copy over the demobot binaries
USER root
COPY demobot .
RUN chown demobot:demobot demobot
COPY serverscanner .
RUN chown demobot:demobot serverscanner
RUN mkdir -p /mnt/config
RUN chown demobot:demobot /mnt/config
VOLUME /mnt/config
USER demobot

CMD ./serverscanner /mnt/config/config.json
