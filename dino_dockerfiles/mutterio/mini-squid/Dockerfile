FROM mutterio/mini-base

RUN apk --update add squid && \
  rm -rf /tmp/src && \
  rm -rf /var/cache/apk/*

RUN curl -sSLo /usr/local/bin/dumb-init \
  https://github.com/Yelp/dumb-init/releases/download/v1.0.0/dumb-init_1.0.0_amd64
RUN chmod +x /usr/local/bin/dumb-init

ADD scripts/start.sh /start.sh
ADD scripts/start-cache.sh /start-cache.sh
ADD squid.conf /etc/squid/squid.conf
ADD squid-cache.conf /etc/squid/squid-cache.conf

RUN mkdir -p /var/log/squid

EXPOSE 3128
ENTRYPOINT ["dumb-init"]
CMD ["/start.sh"]
