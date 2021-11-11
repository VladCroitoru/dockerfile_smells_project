#FROM quay.io/wakaba/docker-perl-app-base

FROM debian:stretch
RUN apt-get update && \
    DEBIAN_FRONTEND="noninteractive" apt-get -y install sudo git wget curl make gcc build-essential libssl-dev && \
    rm -rf /var/lib/apt/lists/*
RUN wget https://cpan.metacpan.org/`curl -f -L https://raw.githubusercontent.com/wakaba/perl-setupenv/master/version/perl-cpan-path.txt` && \
    tar zvxf perl-*.tar.gz && \
    cd perl-* && \
    sh Configure -de -A ccflags=-fPIC -Duserelocatableinc -Dusethreads -Dman1dir=none -Dman3dir=none && \
    make -j 4 all install && \
    cd .. && \
    rm -fr perl-*

ADD .git/ /app/.git/
ADD .gitmodules /app/.gitmodules
ADD Makefile /app/
ADD bin/ /app/bin/
ADD lib/ /app/lib/
ADD config/ /app/config/
ADD modules/ /app/modules/
ADD templates/ /app/templates/
ADD css/ /app/css/
ADD js/ /app/js/
ADD html/ /app/html/
ADD local/data/ /app/local/data/

RUN cd /app && \
    make deps-docker PMBP_OPTIONS="--execute-system-package-installer --dump-info-file-before-die" && \
    echo '#!/bin/bash' > /server && \
    echo 'exec /app/bin/docker-server' >> /server && \
    chmod u+x /server && \
    rm -fr /app/.git /app/deps /app/t /app/t_deps && \
    rm -rf /var/lib/apt/lists/*

CMD ["/server"]
