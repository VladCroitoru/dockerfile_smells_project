FROM gliderlabs/alpine:3.4

RUN apk add --update --no-cache curl bash jq

COPY check /opt/resource/check
COPY in    /opt/resource/in
COPY out   /opt/resource/out
COPY functions.sh  /opt/resource/functions.sh

RUN chmod +x /opt/resource/out /opt/resource/in /opt/resource/check /opt/resource/functions.sh
