FROM xogroup/mongodb-rclone:latest
LABEL maintainer="coreservices.group@xogrp.com"

USER root

ENV HOME_DIR /root
ADD mongodump.sh $HOME_DIR
ADD entrypoint.sh $HOME_DIR

RUN apk update \
 && apk add --no-cache \
    openssl \
    bash \
 && chmod +x $HOME_DIR/mongodump.sh \
 && chmod +x $HOME_DIR/entrypoint.sh \
 && rm -rf /var/cache/apk/*

ENTRYPOINT ["/root/entrypoint.sh"]
CMD ["/root/mongodump.sh"]
