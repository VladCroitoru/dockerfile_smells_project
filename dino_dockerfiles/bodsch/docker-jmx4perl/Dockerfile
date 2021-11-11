
FROM alpine:3.9

MAINTAINER Bodo Schulz <bodo@boone-schulz.de>

ENV \
  TERM=xterm \
  VERSION=1.12

# ---------------------------------------------------------------------------------------

RUN \
  apk --quiet --no-cache update && \
  apk --quiet --no-cache upgrade && \
  apk add --quiet --virtual .build-deps \
    build-base \
    perl-dev \
    readline-dev \
    ncurses-dev \
    libxml2-dev \
    expat-dev \
    gnupg1 \
    openssl-dev \
    wget && \
  apk --quiet --no-cache add \
    perl \
    readline \
    ncurses-libs && \
  cpan App::cpanminus < /dev/null && \
  cpanm --quiet --notest \
    IO::Socket::Multicast \
    Config::General \
    Crypt::Blowfish_PP \
    Module::Find  \
    Monitoring::Plugin \
    Sys::SigAction \
    File::SearchPath \
    ExtUtils::MakeMaker \
    PJB/Term-Clui-1.70.tar.gz \
    Term::ReadLine::Gnu \
    Term::ShellUI \
    Term::Size \
    Net::HTTP \
    ROLAND/jmx4perl-${VERSION}.tar.gz && \
    apk del --quiet --purge .build-deps && \
  rm -rf \
    /root/.cpanm \
    /tmp/* \
    /var/cache/apk/*

CMD [ "jmx4perl", "--version" ]

# ---------------------------------------------------------------------------------------
