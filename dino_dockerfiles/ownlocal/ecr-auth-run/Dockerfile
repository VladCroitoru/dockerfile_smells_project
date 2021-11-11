FROM alpine:3.4

WORKDIR /root

RUN apk update && apk upgrade && \
    apk add py-pip && \
    rm -f /var/cache/apk/* && \
    pip install awscli --no-cache-dir

ADD run.sh /root/

ENTRYPOINT ["./run.sh"] # Provide "docker run" arguments when running
