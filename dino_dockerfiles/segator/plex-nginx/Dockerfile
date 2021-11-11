FROM linuxserver/plex
RUN apt-get update -y && apt-get install nginx -y
COPY default.conf /etc/nginx/conf.d/default.conf
COPY root/ /
ENV PLEX_BACKEND=127.0.0.1:32400