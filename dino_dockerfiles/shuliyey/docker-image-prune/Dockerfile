FROM docker
MAINTAINER Zeyu Ye <shuliyey@gmail.com>

# install dev tools
RUN apk add --update tar gzip wget bash tzdata \
  && wget --no-check-certificate -O /tmp/go-cron.tar.gz https://github.com/michaloo/go-cron/releases/download/v0.0.2/go-cron.tar.gz \
  && tar xvf /tmp/go-cron.tar.gz -C /usr/bin \
  && apk del wget \
  && rm -rf /var/cache/apk/* \
  && rm -rf /tmp/*

# environment variable for this container
ENV CRONSCHEDULE=

COPY docker-entrypoint.sh /root/docker-entrypoint.sh
COPY docker-image-prune.sh /root/docker-image-prune.sh

ENTRYPOINT ["/root/docker-entrypoint.sh"]
CMD ["cron"]
