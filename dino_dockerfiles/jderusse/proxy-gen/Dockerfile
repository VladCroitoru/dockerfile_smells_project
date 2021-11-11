FROM nginx:latest
MAINTAINER Jérémy Derussé "jeremy@derusse.com"

RUN apt-get update \
 && apt-get install --no-install-recommends -y \
    ca-certificates \
    supervisor \

 && apt-get clean \
 && rm -r /var/lib/apt/lists/*

ENV DOCKER_GEN_VERSION 0.4.0

RUN apt-get update \
 && apt-get install -y -q --no-install-recommends \
    wget \

 && wget --no-check-certificate -qO- https://github.com/jwilder/docker-gen/releases/download/$DOCKER_GEN_VERSION/docker-gen-linux-amd64-$DOCKER_GEN_VERSION.tar.gz | tar xvz -C /usr/local/bin \

 && apt-get purge -y wget \

 && apt-get clean \
 && rm -r /var/lib/apt/lists/*


ENV DOCKER_HOST unix:///var/run/docker.sock

ADD config/nginx.tmpl /etc/nginx.tmpl
ADD config/supervisord.conf /etc/supervisor/conf.d/docker-gen.conf

RUN echo "daemon off;" >> /etc/nginx/nginx.conf \
 && sed -i 's/^http {/&\n    server_names_hash_bucket_size 128;/g' /etc/nginx/nginx.conf

VOLUME /var/run

EXPOSE 80
EXPOSE 443

CMD ["/usr/bin/supervisord", "-n"]