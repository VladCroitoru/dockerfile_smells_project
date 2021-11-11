FROM ubuntu:trusty

ENV LANG en_US.UTF-8
RUN locale-gen $LANG

RUN apt-get update -q && \
    apt-get install -qy openjdk-7-jre-headless && \
    apt-get install -qy unzip
    
ADD http://downloads.sourceforge.net/project/subsonic/subsonic/6.0/subsonic-6.0.deb /tmp/subsonic.deb
ADD http://dilerium.se/musiccabinet/subsonic-installer-standalone.zip /tmp/subsonic-installer-standalone.zip

RUN dpkg -i /tmp/subsonic.deb && \
    rm -rf /tmp/subsonic.deb && \
    mv /var/subsonic /var/subsonic.default && \
    ln -s /data /var/subsonic && \
    unzip -d /usr/share/subsonic -o /tmp/subsonic-installer-standalone.zip && \
    mv -f /usr/share/subsonic/subsonic-installer-standalone/* /usr/share/subsonic/. && \
    rm -rf /usr/share/subsonic/subsonic-installer-standalone && \
    rm -rf /tmp/subsonic-installer-standalone.zip

# Don't fork to the background
RUN sed -i "s/ > \${LOG} 2>&1 &//" /usr/share/subsonic/subsonic.sh

ADD start.sh /start.sh
RUN chmod +x /start.sh && \
    chmod +x /usr/share/subsonic/subsonic.sh

VOLUME ["/data"]
EXPOSE 4040

CMD ["/start.sh"]
