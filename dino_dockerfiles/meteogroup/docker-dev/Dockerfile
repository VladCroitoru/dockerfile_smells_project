FROM docker:dind

RUN apk --no-cache -U upgrade \
 && apk --no-cache -U add curl bash jq iptables xz py-pip \
 && pip install docker-compose

VOLUME /var/lib/docker

COPY docker-dev.sh /usr/local/bin/docker-dev.sh
ENTRYPOINT [ "docker-dev.sh" ]
