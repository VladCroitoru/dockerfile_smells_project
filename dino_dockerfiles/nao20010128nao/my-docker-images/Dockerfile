# Welcome to nao20010128nao/my-docker-images.
# "Latest" tag has no functions.
# In other words, it's dummy.
# See https://hub.docker.com/r/nao20010128nao/my-docker-images/ for tags,
#   https://github.com/nao20010128nao/my-docker-images/ for Dockerfiles.

FROM ubuntu
MAINTAINER nao20010128nao

RUN set -xe && \
        apt-get update && \
        apt-get install -y wget ca-certificates && \
        update-ca-certificates && \
        wget https://gist.github.com/nao20010128nao/397a71fb99d82b7219ad8cba80d70f41/raw/47fb96ae4e8f17d5d6b19122ce482bfbaf0e8b4c/message.sh -O /usr/local/bin/message.sh && \
        chmod +x /usr/local/bin/message.sh && \
        apt-get purge -y wget && \
        rm -rf /var/lib/apt/lists/*

CMD ["sh","/usr/local/bin/message.sh"]
