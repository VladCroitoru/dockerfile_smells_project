FROM ubuntu:16.04
MAINTAINER tobernguyen@gmail.com
ENV DEBIAN_FRONTEND noninteractive
EXPOSE 8891

ENV SLIMERJS_VERSION_F 0.10.3

RUN apt-get update && \
    apt-get -y install curl unzip wget && \
    curl -sL https://deb.nodesource.com/setup_8.x | /bin/bash - && \
    apt-get -y install nodejs build-essential xvfb libfontconfig1 libgtk-3-0 libdbus-glib-1-2 graphicsmagick && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN wget sourceforge.net/projects/ubuntuzilla/files/mozilla/apt/pool/main/f/firefox-mozilla-build/firefox-mozilla-build_52.0.2-0ubuntu1_amd64.deb && \
    dpkg -i firefox-mozilla-build_52.0.2-0ubuntu1_amd64.deb && \
    rm firefox-mozilla-build_52.0.2-0ubuntu1_amd64.deb

RUN mkdir -p /srv/var && \
    wget -O /tmp/slimerjs-$SLIMERJS_VERSION_F.zip http://download.slimerjs.org/releases/$SLIMERJS_VERSION_F/slimerjs-$SLIMERJS_VERSION_F.zip && \
    unzip /tmp/slimerjs-$SLIMERJS_VERSION_F.zip -d /tmp && \
    rm -f /tmp/slimerjs-$SLIMERJS_VERSION_F.zip && \
    mv /tmp/slimerjs-$SLIMERJS_VERSION_F/ /srv/var/slimerjs && \
    chmod 755 /srv/var/slimerjs/slimerjs && \
    ln -s /srv/var/slimerjs/slimerjs /usr/bin/slimerjs

ADD . /root
WORKDIR /root
RUN npm install

ENV DISPLAY=:99
ADD xvfb_init /etc/init.d/xvfb
ADD xvfb_daemon_run /usr/bin/xvfb-daemon-run
RUN chmod a+x /etc/init.d/xvfb && \
    chmod a+x /usr/bin/xvfb-daemon-run && \
    chmod a+x /root/entrypoint.sh

ENTRYPOINT ["/root/entrypoint.sh"]
