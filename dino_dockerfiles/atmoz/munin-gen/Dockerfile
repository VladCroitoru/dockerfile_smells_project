FROM nginx
MAINTAINER Adrian Dvergsdal [atmoz.net]

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y wget supervisor cron munin && \
    rm -rf /var/lib/apt/lists/*

ENV DOCKER_GEN_VERSION 0.4.1
RUN wget https://github.com/jwilder/docker-gen/releases/download/$DOCKER_GEN_VERSION/docker-gen-linux-amd64-$DOCKER_GEN_VERSION.tar.gz && \
    tar -C /usr/local/bin -xvzf docker-gen-linux-amd64-$DOCKER_GEN_VERSION.tar.gz && \
    rm /docker-gen-linux-amd64-$DOCKER_GEN_VERSION.tar.gz

RUN mkdir -p /var/run/munin /var/cache/munin/www && \
    chown -R munin /var/run/munin/ /var/cache/munin/www

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY supervisord.conf /etc/supervisor/conf.d/
COPY docker-nodes.tmpl /etc/munin/

VOLUME /var/lib/munin
VOLUME /var/cache/munin/www

COPY entrypoint.sh /
CMD ["/entrypoint.sh"]
