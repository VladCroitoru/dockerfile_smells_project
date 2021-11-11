FROM alpine
RUN apk --update upgrade \
    && apk add --no-cache \
      email \
    && rm -rf /var/cache/apk/* \
    && mv /etc/email/email.conf /etc/email/email.conf.orig
