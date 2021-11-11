FROM nginx
MAINTAINER luodaoyi <admin@52res.com>

RUN echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" >> /etc/apt/sources.list
RUN apt-get update && \
    apt-get install -y git && \
    rm -rf /var/lib/apt/lists/*