FROM alpine:3.10.3
MAINTAINER Ivan Kuznetsov <kuzma.wm@gmail.com>

RUN apk add --no-cache --virtual build-deps g++ make perl-dev tzdata openssh git curl perl-dbd-pg
RUN cpan App::cpanminus
RUN cpanm App::Sqitch --no-wget --notest --quiet
RUN rm -rf /root/.cpan

FROM postgres:12.1-alpine

MAINTAINER Ivan Kuznetsov <kuzma.wm@gmail.com>

RUN apk add --no-cache perl perl-dbd-pg
RUN cp /usr/share/zoneinfo/UTC /etc/localtime
RUN echo UTC > /etc/timezone

COPY --from=0 /usr/lib/perl5/core_perl/perllocal.pod /usr/lib/perl5/core_perl/perllocal.pod

COPY --from=0 /usr/local/bin/config_data /usr/local/bin/config_data
COPY --from=0 /usr/local/bin/package-stash-conflicts /usr/local/bin/package-stash-conflicts
COPY --from=0 /usr/local/bin/shell-quote /usr/local/bin/shell-quote
COPY --from=0 /usr/local/bin/sqitch /usr/local/bin/sqitch

COPY --from=0 /usr/local/etc /usr/local/etc
COPY --from=0 /usr/local/lib/perl5 /usr/local/lib/perl5

COPY --from=0 /usr/local/share/perl5 /usr/local/share/perl5
#
