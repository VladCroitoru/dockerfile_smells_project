FROM gliderlabs/alpine
RUN apk-install bash

ADD log-generator.sh /

ENTRYPOINT ["/log-generator.sh"]
