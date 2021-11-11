# Writing Guidelines: https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/
# vim: set tabstop=4 shiftwidth=4 expandtab :

FROM nginx:1.11

MAINTAINER Jonah.Beckford@plainlychrist.org

# Similar to Apache v2 licensed https://github.com/coreos/docker-nginx-https-redirect, but without /.well-known/acme-challenge
# That /.well-known/acme-challenge is for "Let's Encrypt" to prove your site is yours (which is dangerous)

RUN rm -f /etc/nginx/conf.d/*.conf
ADD ./bounce.conf /etc/nginx/conf.d/

EXPOSE 80
