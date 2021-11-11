FROM debian:jessie
MAINTAINER twoboxen <hawkins22gmail.com>

RUN mkdir -p /usr/local/bin \
  && apt-get update -q \
  && apt-get install -qy python handbrake-cli \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

VOLUME /volumes/source
VOLUME /volumes/destination

COPY src/mediacleaner /usr/local/bin/
COPY src/mediafiler /usr/local/bin/
RUN chmod +x /media*

ENV PATH /:$PATH

ENTRYPOINT ["mediacleaner"]
CMD ["-l", "-r", "-d", "/volumes/destination", "/volumes/source"]
