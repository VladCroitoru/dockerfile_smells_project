FROM debian:jessie

RUN set -ex; \
    apt-get update -qq; \
    apt-get install -y \
        python-dev \
        zlib1g \
        zlib1g-dev \
        libssl-dev \
        git\
	ca-certificates \
        curl \
        libsqlite3-dev \
        libbz2-dev \
    ; 

RUN set -ex; \
    curl -fsSLO https://get.docker.com/builds/Linux/x86_64/docker-1.12.0.tgz && \
	tar --strip-components=1 -xvzf docker-1.12.0.tgz -C /usr/local/bin

RUN set -ex; \
    curl -L https://bootstrap.pypa.io/get-pip.py | python

RUN pip install https://github.com/whulshof/voodoo/archive/voodindock.zip


ADD entrypoint.sh /

ENTRYPOINT ["/entrypoint.sh"]
