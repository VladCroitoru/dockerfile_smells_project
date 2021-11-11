FROM alpine:latest
RUN apk add --update curl jq bash && \
    rm -rf /var/cache/apk/*
ADD ./increment_patch.sh  /increment_patch.sh
RUN sh -c 'touch /increment_patch.sh'
RUN ["chmod", "+x", "/increment_patch.sh"]
ENTRYPOINT ["/increment_patch.sh"]