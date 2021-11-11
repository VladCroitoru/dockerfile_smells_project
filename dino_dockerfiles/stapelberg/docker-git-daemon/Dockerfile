FROM debian:stable

RUN echo 'deb http://deb.debian.org/debian testing main' > /etc/apt/sources.list.d/testing.list \
    && echo 'APT::Default-Release "stable";' > /etc/apt/apt.conf.d/08default-release \
    && apt-get update \
    && apt-get install -y --no-install-recommends -t testing dumb-init \
    && apt-get install -y --no-install-recommends git \
    && rm /etc/apt/sources.list.d/testing.list \
    && rm -rf /var/lib/apt/lists/*
# TODO: switch back to the following once dumb-init is in stable:
#RUN apt-get update \
#    && apt-get install -y --no-install-recommends git \
#    && rm -rf /var/lib/apt/lists/*

EXPOSE 9418
ENTRYPOINT ["dumb-init", "/usr/bin/git", "daemon", "--reuseaddr", "--timeout=3600", "--verbose", "--base-path=/git", "/git"]
