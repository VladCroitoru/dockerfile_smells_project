FROM anapsix/alpine-java
RUN apk add --no-cache curl \
                       tar \
                       ruby \
                       ruby-dev \
                       zlib \
                       zlib-dev \
                       openssl \
                       openssl-dev \
                       libssl1.0 \
                       bash \
                       procps \
                       musl-dev \
                       make \
                       linux-headers \
                       build-base \
                       libxml2-dev \
                       libxslt-dev \
                       libffi-dev \
                       nodejs
RUN gem install bundler therubyracer --no-ri --no-rdoc
