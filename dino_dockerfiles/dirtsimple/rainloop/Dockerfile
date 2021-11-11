FROM dirtsimple/php-server:latest

# Install dependencies
RUN EXTRA_APKS="imap-dev nodejs" EXTRA_EXTS=imap install-extras \
    && npm install -g yarn gulp

# Install/build Rainloop

ENV CODE_BASE /code
ARG RAINLOOP_VERSION=v1.11.1

RUN git clone --branch $RAINLOOP_VERSION --depth 1 https://github.com/RainLoop/rainloop-webmail $CODE_BASE \
    && cd $CODE_BASE \
    && yarn install \
    && gulp \
    && mv data /data \
    && ln -s /data data

ENV PHP_CONTROLLER true
ENV EXCLUDE_PHP /data
ENV NGINX_OWNED /data

VOLUME /data
WORKDIR $CODE_BASE

