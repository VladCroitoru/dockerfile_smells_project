FROM gliderlabs/alpine
MAINTAINER Simon Dittlmann

RUN apk-install bash curl grep

ADD elasticsearch-optimize-index.sh /elasticsearch-optimize-index.sh
ADD elasticsearch-remove-old-indices.sh elasticsearch-remove-old-indices.sh

RUN chmod 755 /*.sh
