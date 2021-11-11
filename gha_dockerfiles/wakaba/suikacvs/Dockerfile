#FROM quay.io/wakaba/docker-perl-app-base

#XXX
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
ADD local/cvsrepo/ /app/local/cvsrepo/
ADD config/ /app/config/

RUN cd /app && \
    apt-get update && apt-get install -y rcs python && \
    make deps-server PMBP_OPTIONS=--execute-system-package-installer && \
    echo '#!/bin/bash' > /server && \
    echo 'cd /app' >> /server && \
    echo 'exec ./plackup -s Twiggy -p 8080 bin/server.psgi' >> /server && \
    chmod u+x /server && \
    rm -fr /app/.git /app/deps /app/t /app/t_deps && \
    rm -rf /var/lib/apt/lists/*

CMD ["/server"]
