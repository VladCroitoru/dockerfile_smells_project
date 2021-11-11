FROM rebootshen/selenium

ENV FIREFOX_MINOR 34.0.5

RUN apt-get update -qqy \
&& apt-get -qqy --no-install-recommends install \
firefox \
xvfb \
bzip2 \
&& rm -rf /var/lib/apt/lists/*

RUN [ -e /usr/bin/firefox ] && rm /usr/bin/firefox
ADD https://ftp.mozilla.org/pub/mozilla.org/firefox/releases/${FIREFOX_MINOR}/linux-x86_64/en-US/firefox-${FIREFOX_MINOR}.tar.bz2 /tmp/
RUN apt-get install -q -y libdbus-glib-1-2
RUN tar -xvjf /tmp/firefox-${FIREFOX_MINOR}.tar.bz2 -C /opt/
RUN chmod -R +x /opt/firefox/ \
&& ln -s /opt/firefox/firefox /usr/bin/firefox

ADD register-node.sh /var/register-node.sh
RUN chmod 755 /var/register-node.sh

CMD ["/bin/bash", "/var/register-node.sh"]
