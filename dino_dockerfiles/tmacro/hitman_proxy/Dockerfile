FROM tmacro/lego:latest

ENV STATE_DIR /etc/haproxy/state

ADD https://github.com/jwilder/docker-gen/releases/download/0.7.3/docker-gen-alpine-linux-amd64-0.7.3.tar.gz /tmp/docker-gen.tar.gz
RUN tar xzf /tmp/docker-gen.tar.gz -C /usr/bin

RUN apk_add haproxy socat

ADD ./reload-haproxy /usr/bin/reload-haproxy
RUN chmod +x /usr/bin/reload-haproxy
ADD ./haproxy.cfg.tmpl /etc/haproxy/haproxy.cfg.tmpl
COPY ./s6 /etc
RUN mkdir -p $STATE_DIR
ENTRYPOINT /init