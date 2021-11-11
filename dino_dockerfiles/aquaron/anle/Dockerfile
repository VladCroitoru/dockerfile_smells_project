FROM alpine

ARG BUILD_DATE

LABEL maintainer="docker@aquaron.com" \
 org.label-schema.build-date=$BUILD_DATE \
 org.label-schema.docker.cmd="docker run -v $PWD:/data -p 80:80 -p 443:443 -h anle -d aquaron/anle" \
 org.label-schema.description="Nginx build on Alpine with Certbot to use as a reverse proxy." \
 org.label-schema.name="nginx" \
 org.label-schema.url="https://nginx.org" \
 org.label-schema.vcs-url="https://github.com/aquaron/anle" \
 org.label-schema.vendor="aquaron" \
 org.label-schema.version="1.1"

ENV _image=aquaron/anle

COPY data /data-default

RUN apk add -q --no-cache nginx \
 && ln -s /data-default/bin/runme.sh /usr/bin \
 && ln -s /data-default/bin/bash-prompt /root/.profile

VOLUME /data
ENTRYPOINT [ "runme.sh" ]
CMD [ "daemon" ]
