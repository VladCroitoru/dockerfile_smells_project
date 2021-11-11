FROM docker:stable-git

ENV PATH=/usr/local/src/.ci/bin:/usr/local/src/bin:${PATH}

RUN set -exu \
 && apk add --update --no-cache bash ca-certificates curl git make py-pip tar jq \
 && pip install --upgrade pip \
 && pip install docker-compose \
 && mkdir -p /var/cache/docker/ /usr/local/src/

WORKDIR /usr/local/src
