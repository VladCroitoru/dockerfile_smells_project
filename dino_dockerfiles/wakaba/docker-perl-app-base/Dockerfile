#FROM debian:sid
FROM debian

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

RUN mkdir /app && \
    cd app && \
    curl -f -L https://wakaba.github.io/packages/pmbp | sh && \
    perl local/bin/pmbp.pl \
        --perl-version latest --perl-relocatable --install-perl \
        --create-perl-command-shortcut @perl \
        --create-perl-command-shortcut @prove \
        --execute-system-package-installer \
        --dump-info-file-before-die && \
    ./perl local/bin/pmbp.pl \
        --install-module Encode \
        --install-module Net::SSLeay \
        --install-module JSON::XS \
        --install-module Unicode::Normalize \
        --install-module AnyEvent \
        --execute-system-package-installer \
        --dump-info-file-before-die && \
    rm -fr deps local/perlbrew/build && \
    PMBP_VERBOSE=10 perl local/bin/pmbp.pl
