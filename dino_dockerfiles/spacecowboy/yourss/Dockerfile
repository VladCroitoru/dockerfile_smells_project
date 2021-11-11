FROM debian:stretch-slim

RUN apt-get update -qq && \
    apt-get install -qy curl bash libav-tools youtube-dl python3-feedparser && \
    rm -rf /var/lib/apt/lists/*

RUN curl --location --output /tmp/hugo.deb https://github.com/spf13/hugo/releases/download/v0.18.1/hugo_0.18.1-64bit.deb && \
    dpkg -i /tmp/hugo.deb
RUN curl --location --output /tmp/yourss.deb https://github.com/spacecowboy/yourss/releases/download/1.0.1/yourss_1.0.1_all.deb && \
    dpkg -i /tmp/yourss.deb

ENV SCRIPTDIR=/usr/share/yourss/scripts SITEDIR=/usr/share/yourss/site

ENTRYPOINT ["/usr/bin/yourss"]
