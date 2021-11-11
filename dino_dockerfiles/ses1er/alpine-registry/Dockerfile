FROM gliderlabs/alpine:3.3

RUN apk update &&  apk add --update bash curl wget docker-registry
ADD ./config.yml /etc/docker-registry/config.yml

EXPOSE 80
ENTRYPOINT ["/usr/bin/docker-registry"]
CMD ["/etc/docker-registry/config.yml"]

