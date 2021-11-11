FROM nginx:1.11.3
MAINTAINER Olivier ORABONA olivier.orabona@gmail.com

# Install wget and install/updates certificates
RUN apt-get update \
 && apt-get install -y -q --no-install-recommends \
    ca-certificates \
    wget \
    curl \
    build-essential \
    nodejs \
    npm \
 && apt-get clean \
 && rm -r /var/lib/apt/lists/*

RUN npm i later deep-equal q winston promised-exec request-promise-any

ENV RANCHER_METADATA_HOST http://rancher:8080
ENV RANCHER_VERSION v1
ENV NGINX_CMD nginx
ENV IP_FIELD dockerIp

VOLUME ["/etc/nginx/certs", "/etc/nginx/conf.d", "/etc/nginx/vhosts.d"]

COPY app /app/
COPY nginx-default-vhost.conf /etc/nginx/vhosts.d/
COPY nginx.conf /etc/nginx/
WORKDIR /app/

RUN mkdir /etc/nginx/logs
RUN chmod u+x /app/docker-entrypoint.sh /app/app.js

ENTRYPOINT ["/app/docker-entrypoint.sh"]
CMD ["js", "app.js"]
