FROM alpine:latest
MAINTAINER Darkload <debuggerboy@gmail.com>
ENV GIT_REPO_URL="https://github.com/trydock/nginx-lb-config.git"
RUN apk add --update nginx supervisor bash curl git && rm -rf /var/cache/apk/* && cd /root/ && mkdir setup && cd setup && git clone ${GIT_REPO_URL} config && cd config && git pull && sh sync.sh
RUN mkdir -p /tmp/nginx/client-body
EXPOSE 80 443
CMD ["/usr/bin/supervisord"]
