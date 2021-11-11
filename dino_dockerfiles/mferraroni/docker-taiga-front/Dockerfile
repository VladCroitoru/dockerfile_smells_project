FROM nginx:1.7

MAINTAINER Maik Hummel <m@ikhummel.com>

WORKDIR /usr/local/taiga

ENV TAIGA_VERSION 3.1.0

COPY *.conf mime.types /etc/nginx/
COPY upstream.conf conf.json conf.env start ./

RUN buildDeps='curl'; \
    set -x && \
    apt-get -qq update && apt-get -qq install -y $buildDeps --no-install-recommends && \
    apt-get -qq install -y gettext-base --no-install-recommends && \

    # forward request and error logs to docker log collector
    ln -sf /dev/stdout /var/log/nginx/access.log && \
    ln -sf /dev/stderr /var/log/nginx/error.log && \
    mkdir taiga-front-dist && \
    curl -sL "https://github.com/taigaio/taiga-front-dist/archive/$TAIGA_VERSION-stable.tar.gz" | tar xz -C taiga-front-dist --strip-components=1 && \

    cd taiga-front-dist && \

    # clean up
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    apt-get purge -y --auto-remove $buildDeps && \
    apt-get autoremove -y && \
    apt-get clean

EXPOSE 80 443

CMD /bin/bash /usr/local/taiga/start
