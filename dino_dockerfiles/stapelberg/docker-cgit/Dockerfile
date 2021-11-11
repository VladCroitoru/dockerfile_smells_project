# This Dockerfile uses lighttpd instead of nginx because lighttpd has mod_cgi,
# whereas nginx requires a lot of effort (fcgiwrap, spawn-fcgi) to use cgi.
FROM debian:stable

RUN echo 'deb http://deb.debian.org/debian testing main' > /etc/apt/sources.list.d/testing.list \
    && echo 'APT::Default-Release "stable";' > /etc/apt/apt.conf.d/08default-release \
    && apt-get update \
    && apt-get install -y --no-install-recommends -t testing dumb-init \
    && apt-get install -y --no-install-recommends lighttpd cgit bzip2 gzip \
    && rm /etc/apt/sources.list.d/testing.list \
    && rm -rf /var/lib/apt/lists/*
# TODO: switch back to the following once dumb-init is in stable:
#RUN apt-get update \
#    && apt-get install -y --no-install-recommends lighttpd cgit bzip2 gzip \
#    && rm -rf /var/lib/apt/lists/*

RUN mkdir /etc/cgit \
    && ln -sf cgit/cgitrc /etc/cgitrc

ADD lighttpd-cgit.conf /etc/lighttpd/lighttpd-cgit.conf

VOLUME /etc/cgit

EXPOSE 80
ENTRYPOINT ["dumb-init", "/usr/sbin/lighttpd", "-f", "/etc/lighttpd/lighttpd-cgit.conf", "-D"]
