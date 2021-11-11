FROM gliderlabs/alpine:3.3

RUN apk-install perl

COPY ./dyfi-update.pl /opt/

CMD ["perl", "/opt/dyfi-update.pl"]
