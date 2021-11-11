FROM alpine:edge

RUN apk add --update bash jq
RUN wget https://github.com/pivotal-cf/om/releases/download/0.26.0/om-linux -O /usr/local/bin/om && chmod +x /usr/local/bin/om

COPY check /opt/resource/check
COPY in /opt/resource/in
COPY out /opt/resource/out
