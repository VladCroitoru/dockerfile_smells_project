FROM debian:stretch-slim

# install mongo-tools, curl  and jq
RUN apt-get update && apt-get install -y \
  mongo-tools=3.2.* \
  curl=7.51.* \
  jq=1.5* \
  xsltproc=1.1.29* \
  git=1:2.11.0* \
  && rm -rf /var/lib/apt/lists/*

# install go-cron
RUN curl -L https://github.com/odise/go-cron/releases/download/v0.0.7/go-cron-linux.gz \
  | zcat > /usr/local/bin/go-cron \
  && chmod u+x /usr/local/bin/go-cron

RUN mkdir /osem-archiver
WORKDIR /osem-archiver

COPY helpers.sh archive.sh cron-wrapper.sh build-index.sh *.xslt /osem-archiver/

# schedule for 02:30:00 UTC each day
CMD go-cron -p "0" -s "0 30 2 * * *" -- /osem-archiver/cron-wrapper.sh /osem-archiver/archive.sh
