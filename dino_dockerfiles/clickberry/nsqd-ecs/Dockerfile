FROM nsqio/nsq

ADD ./docker-entrypoint.sh /
RUN chmod +x ./docker-entrypoint.sh
ENTRYPOINT ["/bin/sh", "./docker-entrypoint.sh"]
