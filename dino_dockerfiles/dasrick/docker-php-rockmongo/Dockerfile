FROM dasrick/docker-php-base-wbc:5.6.18

MAINTAINER Steve Reichenbach <steve.reichenbach@movingimage.com>

ENV ROCKMONGO_VERSION 1.1.7

RUN mkdir /var/rockmongo/ \
    && cd /var/rockmongo/ \
    && curl -O --insecure -L https://github.com/iwind/rockmongo/archive/${ROCKMONGO_VERSION}.tar.gz \
    && tar -zxvf ${ROCKMONGO_VERSION}.tar.gz -C $(pwd) --strip-components=1 \
    && rm -f ${ROCKMONGO_VERSION}.tar.gz

WORKDIR /var/rockmongo
RUN rm -f config.php && ln -fs /var/config.php config.php

VOLUME ["/var/rockmongo"]
