FROM debian:wheezy
MAINTAINER Kevin Fletcher <ipvfletch@gmail.com>
ENV VERSION 0.5.0
ENV DOWNLOAD_URL https://github.com/jwilder/docker-gen/releases/download/$VERSION/docker-gen-linux-amd64-$VERSION.tar.gz
ENV DOCKER_HOST unix:///tmp/docker.sock

RUN deps=' \
        curl ca-certificates \
    '; \
    set -x; \
    apt-get update \
    && apt-get install -y --no-install-recommends $deps \
    && curl -L $DOWNLOAD_URL | tar -C /usr/local/bin -xvz \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false -o APT::AutoRemove::SuggestsImportant=false $deps \
    && apt-get install -y --no-install-recommends python-pip python-requests \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

RUN pip install -U boto

ADD bin/route53-autodns.py /bin/route53-autodns.py
ADD templates/route53.tmpl templates/route53.tmpl

CMD /usr/local/bin/docker-gen -notify "/bin/bash /tmp/route53.sh" -interval 10 templates/route53.tmpl /tmp/route53.sh

