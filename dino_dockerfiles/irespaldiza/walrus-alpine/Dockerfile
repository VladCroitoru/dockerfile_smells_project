FROM docker
LABEL maintainer: docker@irespaldiza.com

RUN apk update && apk add --update \
    curl \
    vim \
    git \
    bash \
    git-bash-completion \
    py-pip &&\
    rm -rf /var/cache/apk/*

RUN pip install docker-compose
ADD aliases.sh /etc/profile.d/aliases.sh

WORKDIR /root

CMD ["/bin/bash", "-l"]
