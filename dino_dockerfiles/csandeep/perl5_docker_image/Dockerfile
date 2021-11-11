FROM node:latest
MAINTAINER csandeep <csandeep@gmail.com>

RUN apt-get update && apt-get install -y mariadb-client  mariadb-common unzip && apt-get install -y mysql-client

RUN mkdir -p /usr/src/perl

WORKDIR /usr/src/perl

## from perl; `true make test_harness` because 3 tests fail
## some flags from http://git.alpinelinux.org/cgit/aports/tree/main/perl/APKBUILD?id=19b23f225d6e4f25330e13144c7bf6c01e624656
RUN curl -SLO http://www.cpan.org/src/5.0/perl-5.28.0.tar.gz \
    && tar --strip-components=1 -xzf perl-5.28.0.tar.gz -C /usr/src/perl \
    && rm perl-5.28.0.tar.gz \
    && ./Configure -des \
        -Duse64bitall \
        -Dcccdlflags='-fPIC' \
        -Dcccdlflags='-fPIC' \
        -Dccdlflags='-rdynamic' \
        -Dlocincpth=' ' \
        -Duselargefiles \
        -Dusethreads \
        -Duseshrplib \
        -Dd_semctl_semun \
        -Dusenm \
    && make libperl.so \
    && make -j$(nproc) \
    && TEST_JOBS=$(nproc) true make test_harness \
    && make install \
    && rm /usr/bin/perl \
    && rm /usr/local/bin/perl \
    && ln -s /usr/local/bin/perl5.28.0 /usr/bin/perl \
    && ln -s /usr/local/bin/perl5.28.0 /usr/local/bin/perl \
    && curl -LO https://raw.githubusercontent.com/miyagawa/cpanminus/master/cpanm \
    && chmod +x cpanm \
    && ./cpanm App::cpanminus \
	&& ./cpanm Carton \
    && rm -fr ./cpanm /root/.cpanm /usr/src/perl

## from tianon/perl
ENV PERL_CPANM_OPT --verbose --mirror https://cpan.metacpan.org --mirror-only
RUN cpanm Digest::SHA Module::Signature && rm -rf ~/.cpanm
ENV PERL_CPANM_OPT $PERL_CPANM_OPT --verify

WORKDIR /
