FROM nginx
MAINTAINER AJ Bowen <aj@soulshake.net>

COPY ./src /data/www
COPY nginx.conf /etc/nginx/nginx.conf

COPY bin /src/bin
WORKDIR /src

RUN echo "alias ll='ls -lahF'" >> /root/.bashrc
