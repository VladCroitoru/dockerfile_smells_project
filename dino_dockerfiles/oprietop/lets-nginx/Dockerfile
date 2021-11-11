FROM nginx:alpine
MAINTAINER Oscar Prieto <oprietop@uoc.edu>

#We need to install bash to easily handle arrays
# in the entrypoint.sh script
RUN apk add --update bash \
  certbot \
  openssl openssl-dev ca-certificates fuse\
  && rm -rf /var/cache/apk/*

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log
RUN ln -sf /dev/stderr /var/log/nginx/error.log

# used for webroot reauth
RUN mkdir -p /etc/letsencrypt/webrootauth

COPY entrypoint.sh /opt/entrypoint.sh
ADD templates /templates

# Adding GCSFUSE
RUN apk add --no-cache --virtual .build-dependencies git build-base go \
    && go get -v -u github.com/googlecloudplatform/gcsfuse \
    && mv /root/go/bin/gcsfuse /usr/local/bin/ \
    && apk del .build-dependencies \
    &&rm -rf /var/cache/apk/* /root/go

# There is an expose in nginx:alpine image
# EXPOSE 80 443

ENTRYPOINT ["/opt/entrypoint.sh"]
