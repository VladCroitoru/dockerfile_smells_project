# based on https://github.com/ZZROTDesign/alpine-caddy

FROM alpine:edge
MAINTAINER j842

RUN apk --no-cache add tini git openssh-client bash \
    && apk --no-cache add --virtual devs tar curl 
    
# Install Caddy Server version 0.9.5
RUN cd /root && curl -L "https://github.com/mholt/caddy/releases/download/v0.9.5/caddy_linux_386.tar.gz" > caddy.tgz && \
    tar zxvf caddy.tgz && cp caddy_linux_386 /usr/bin/caddy && chmod a+x /usr/bin/caddy && rm -rf /root/*
 
VOLUME ["/data"]
VOLUME ["/root/.caddy"]

# https://github.com/krallin/tini
# allows signals to be sent to process :-)
# SIGUSR1 gets caddy to reload config.
ENTRYPOINT ["/sbin/tini","--"]
ENV PATH /bin:/usr/bin:$PATH

#-- enabling http2 is incompatible with websocket connection upgrade.

CMD ["caddy", "-http2=false", "--conf", "/data/caddyfile"]

#CMD ["caddy", "-quic", "-http2=false", "--conf", "/data/caddyfile"]

# add on  -ca "https://acme-staging.api.letsencrypt.org/directory"  for staging