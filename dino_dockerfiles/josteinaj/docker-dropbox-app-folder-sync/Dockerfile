FROM ubuntu:latest
MAINTAINER Jostein Austvik Jacobsen <josteinaj@gmail.com>

# Note: Based on mhimmer/dropbox

USER root
WORKDIR /root

# Set locale
RUN locale-gen en_GB en_GB.UTF-8
ENV LANG C.UTF-8
ENV LANGUAGE en_GB:en
ENV LC_ALL C.UTF-8

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get -o Dpkg::Options::="--force-confnew" --force-yes -fuy dist-upgrade
RUN apt-get update && apt-get install -y wget curl vim screen python-software-properties

RUN echo "Getting dropbox version: 8.4.19" && cd ~ && wget -O - "https://www.dropbox.com/download?plat=lnx.x86_64" | tar xzf -
RUN wget -O /usr/bin/dropbox.py "https://www.dropbox.com/download?dl=packages/dropbox.py"
RUN chmod +x /usr/bin/dropbox.py

RUN mkdir -p /root/Dropbox

COPY src/dropbox-whitelist /usr/bin/dropbox-whitelist
RUN mkdir -p /root/Dropbox/Apper/Blot && \
    mkdir -p /root/Dropbox/fagerheimen.no && \
    mkdir -p /root/Hjemmeside/filer && \
    mkdir -p /root/Hjemmeside/tekst && \
    ln --symbolic /root/Hjemmeside/filer /root/Dropbox/Apper/Blot/public && \
    ln --symbolic /root/Hjemmeside/tekst /root/Dropbox/Apper/Blot/text && \
    ln --symbolic /root/Hjemmeside/filer /root/Dropbox/fagerheimen.no/filer && \
    ln --symbolic /root/Hjemmeside/tekst /root/Dropbox/fagerheimen.no/tekst

RUN crontab -l | { cat; echo "* * * * * /usr/bin/dropbox-whitelist >>/var/log/dropbox-whitelist.log 2>&1\n*/5 * * * * /usr/bin/dropbox.py stop >>/var/log/dropbox.py.log 2>&1 && /usr/bin/
dropbox.py start >>/var/log/dropbox.py.log 2>&1"; } | crontab -
RUN touch /var/log/dropbox-whitelist.log

CMD service cron start ; /usr/bin/dropbox-whitelist ; tail -f /var/log/dropbox-whitelist.log
