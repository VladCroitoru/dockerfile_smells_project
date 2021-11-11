FROM alpine:3.4

MAINTAINER ngineered <support@ngineered.co.uk>

RUN echo http://nl.alpinelinux.org/alpine/edge/testing >> /etc/apk/repositories && apk update && \
    apk add --no-cache bash \
    openssh-client \
    wget \
    nginx \
    supervisor \
    curl \
    bc \
    python \
    python-dev \
    py-pip \
    augeas-dev \
    openssl-dev \
    ca-certificates \
    dialog \
    gcc \
    musl-dev \
    linux-headers \
    libffi-dev \
    git && \
    mkdir -p /etc/nginx && \
    mkdir -p /var/www/app && \
    mkdir -p /run/nginx && \
    mkdir -p /var/log/supervisor && \
    pip install -U certbot && \
    mkdir -p /etc/letsencrypt/webrootauth && \
    apk del gcc musl-dev linux-headers libffi-dev augeas-dev python-dev

#RUN git clone https://github.com/letsencrypt/letsencrypt /opt/letsencrypt

ADD conf/supervisord.conf /etc/supervisord.conf

# Copy our nginx config
RUN rm -Rf /etc/nginx/nginx.conf
ADD conf/nginx.conf /etc/nginx/nginx.conf

# nginx site conf
RUN mkdir -p /etc/nginx/sites-available/ && \
mkdir -p /etc/nginx/sites-enabled/ && \
mkdir -p /etc/nginx/ssl/ && \
rm -Rf /var/www/* && \
mkdir /var/www/html/
ADD conf/nginx-site.conf /etc/nginx/sites-available/default.conf
ADD conf/nginx-site-ssl.conf /etc/nginx/sites-available/default-ssl.conf
RUN ln -s /etc/nginx/sites-available/default.conf /etc/nginx/sites-enabled/default.conf

# Add Scripts
ADD scripts/start.sh /start.sh
ADD scripts/letsencrypt-setup /usr/bin/letsencrypt-setup
ADD scripts/pull /usr/bin/pull
ADD scripts/push /usr/bin/push
ADD scripts/letsencrypt-renew /usr/bin/letsencrypt-renew
RUN chmod 755 /usr/bin/pull && chmod 755 /usr/bin/push && chmod 755 /usr/bin/letsencrypt-renew && chmod 755 /usr/bin/letsencrypt-setup && chmod 755 /start.sh

# copy in code
ADD errors /var/www/errors/
ADD src/ /var/www/html/

VOLUME /var/www/html

EXPOSE 443 80

#CMD ["/usr/bin/supervisord", "-n", "-c",  "/etc/supervisord.conf"]
CMD ["/start.sh"]
