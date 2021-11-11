FROM alpine:3.1

WORKDIR /etc/nginx
ENV NGINX_VERSION="1.9.12"
ENV NGINX_SHA="5945a0701f0ee0755fd20643f755507996a3f7f3"

RUN apk --update add \
    git \
    openssl-dev \
    pcre-dev \
    zlib-dev \
    wget \
    perl \
    perl-dev \
    imagemagick \
    imagemagick-dev \
    build-base

ENV \
    BUILD_DEPS="gettext"  \
    RUNTIME_DEPS="libintl"
RUN \
    apk add --update $RUNTIME_DEPS && \
    apk add --virtual build_deps $BUILD_DEPS &&  \
    cp /usr/bin/envsubst /usr/local/bin/envsubst && \
    apk del build_deps

ADD build.sh /tmp/build.sh
RUN sh /tmp/build.sh \
    rm /tmp/build.sh

RUN mkdir -p /var/nginx/cache
ADD files/default.conf /etc/nginx/conf.d/default.conf
ADD files/nginx.conf.template .
ADD run.sh ./run.sh
RUN chmod +x ./run.sh

EXPOSE 80 443

ENV OMP_NUM_THREADS=1

CMD ["ash", "./run.sh"]