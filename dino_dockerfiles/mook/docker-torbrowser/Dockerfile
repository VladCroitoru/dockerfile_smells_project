# vim: set et ts=4 :

FROM debian:jessie

ENV TOR_VERSION 4.0.3
ENV TOR_LANGUAGE en-US

RUN useradd --uid 1000 --create-home docker-user \
    && true

RUN export DEBIAN_FRONTEND=noninteractive \
    && TOR_URL=https://dist.torproject.org/torbrowser/${TOR_VERSION}/tor-browser-linux64-${TOR_VERSION}_${TOR_LANGUAGE}.tar.xz \
    && apt-get update -q \
    && apt-get install -qy iceweasel curl xauth xz-utils \
    && mkdir /tor-browser \
    && curl "${TOR_URL}" | tar --extract --directory=/tor-browser --xz --strip-components=1 \
    && apt-get remove -qy --auto-remove curl xz-utils \
    && apt-get remove -qy iceweasel \
    && apt-get clean \
    && rm -fr /var/lib/apt/lists/

# leave 9150 alone, otherwise the browser complains
RUN echo 'SocksPort 0.0.0.0:9153' >> /tor-browser/Browser/TorBrowser/Data/Tor/torrc-defaults

WORKDIR /tor-browser/
USER docker-user

CMD touch ${HOME}/.Xauthority ; echo "${XAUTHDATA}" | /usr/bin/xauth nmerge - && /tor-browser/start-tor-browser
