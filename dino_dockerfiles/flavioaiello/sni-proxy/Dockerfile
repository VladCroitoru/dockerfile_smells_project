FROM alpine:3.7

# Add local files to image
COPY files /
    
RUN set -ex;\
    apk update;\
    apk upgrade;\
    apk add --no-cache su-exec tini sniproxy;\
    rm -rf /var/cache/apk/*

ENTRYPOINT ["/sbin/tini", "--", "entrypoint.sh"]
CMD ["sniproxy", "-f"]
