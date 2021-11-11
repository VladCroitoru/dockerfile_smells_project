FROM ubuntu:focal
LABEL maintaner="Krotov Artem <timmson666@mail.ru>"

ARG timezone="Europe/Moscow"
ARG packages="software-properties-common sudo vim cron tzdata wget dnsutils git net-tools netcat nmap"

ENV DEBIAN_FRONTEND=noninteractive

COPY sources.list /etc/apt/

# Change time zone
RUN rm -rf /etc/localtime && \
    ln -s /usr/share/zoneinfo/${timezone} /etc/localtime

# Install essentials
RUN apt update && \
    apt dist-upgrade -y && \
    apt install -y ${packages} && \
    apt autoremove && \
    apt clean