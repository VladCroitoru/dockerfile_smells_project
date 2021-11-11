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

ADD Makefile /app/
ADD config/ /app/config/
ADD lib/ /app/lib/
ADD modules/ /app/modules/

RUN cd /app && \
    make deps-docker PMBP_OPTIONS="--execute-system-package-installer --dump-info-file-before-die" && \
    rm -rf /var/lib/apt/lists/* /app/local/pmbp/tmp /app/deps

#CMD ["/server"]

## License: Public Domain.
