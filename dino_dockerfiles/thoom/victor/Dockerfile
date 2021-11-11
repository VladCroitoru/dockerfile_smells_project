FROM nginx:alpine
MAINTAINER Z. d. Peacock <zdp@thoomtech.com>

ENV HUGO_VERSION=0.23
RUN apk add --no-cache --update \
    ca-certificates \
    openssh-client \
    git \
    py-pygments \
    tini

ADD https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_Linux-64bit.tar.gz /tmp
RUN tar -xf /tmp/hugo_${HUGO_VERSION}_Linux-64bit.tar.gz -C /tmp \
    && mkdir -p /usr/local/sbin \
    && mv /tmp/hugo /usr/local/sbin/hugo \
    && rm -rf /tmp/hugo_${HUGO_VERSION}_linux_amd64

ADD conf/nginx-site.conf /etc/nginx/conf.d/default.conf

# Add Scripts
ADD scripts/start.sh /start.sh

# copy in code
ADD src/ /var/www/

EXPOSE 80
ENTRYPOINT ["/sbin/tini", "-g", "--"]
CMD ["sh", "/start.sh"]

