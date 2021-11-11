FROM debian

LABEL maintainer Kyokuheki <kyokuheki@gmail.com>

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    clamav \
    clamav-freshclam \
 && apt-get clean && rm -rf /var/lib/apt/lists/*
RUN freshclam
RUN mkdir /suspects

WORKDIR /suspects

ENTRYPOINT ["/usr/bin/clamd"]

CMD ["--verbose", "./"]
