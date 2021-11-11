FROM nginx:alpine
MAINTAINER Z. d. Peacock <zdp@thoomtech.com>

RUN apk add --no-cache --update --virtual .build-deps \
    gcc \
    musl-dev \
    linux-headers \
    make \
    ruby-dev \
    libffi-dev \
    && apk add --no-cache --update \
    openssh-client \
    git \
    ruby \
    tini \
    && gem install -N \
    jekyll \
    io-console \
    json \
    bundler \
    && apk del .build-deps

ADD conf/nginx-site.conf /etc/nginx/conf.d/default.conf

# Add Scripts
ADD scripts/start.sh /start.sh

# copy in code
ADD src/ /var/www/

EXPOSE 80
ENTRYPOINT ["/sbin/tini", "-g", "--"]
CMD ["sh", "/start.sh"]
