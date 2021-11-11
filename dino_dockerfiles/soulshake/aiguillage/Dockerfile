FROM nginx
MAINTAINER AJ Bowen <aj@soulshake.net>
RUN apt-get update && apt-get install -y \
    curl
COPY nginx.conf /etc/nginx/nginx.conf
RUN echo "alias ll='ls -lahF'" >> /root/.profile

# docker build -t soulshake/aiguillage .
