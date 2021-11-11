FROM zhujunsan/lnp:v1.8

MAINTAINER San <zhujunsan@gmail.com>

ENV THRIFTPHP_VERSION v0.1.0

# Install Redis/Node.js/alpine-conf
RUN apk add --update --no-cache redis nodejs alpine-conf

# Install ThriftPHP
RUN buildDeps=' \
    git \
    g++ \
    make \
    cmake \
    bison \
    flex \
    ' \
    && apk add --update $buildDeps \
    && git clone https://github.com/stdrickforce/PHP-CPP.git \
    && cd PHP-CPP \
    && sed -i 's/`\${PHP_CONFIG} \-\-ldflags`//g' Makefile \
    && make && make install \
    && cd .. && rm -r PHP-CPP \
    && git clone https://gitlab.baixing.cn/Terence/thriftphp.git \
    && cd thriftphp && git checkout $THRIFTPHP_VERSION && mkdir build && cd build \
    && cmake .. && make && make install \
    && cd ../.. && rm -r thriftphp \
    && echo "extension=thriftphp.so" >> /usr/local/etc/php/conf.d/thriftphp.ini \
    && apk del --purge $buildDeps \
    && echo "build finished~"

# Add Redis supervisor conf
ADD redis.conf /etc/supervisor/conf.d/redis.conf

# Change timezone to CST
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo "Asia/Shanghai" > /etc/timezone
