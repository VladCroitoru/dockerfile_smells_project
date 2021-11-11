FROM cloudposse/library:ubuntu-vps

RUN apt-get update && \
    apt-get -y install libtest-requires-perl libtest-exception-perl libcgi-session-perl libfcgi-perl libmath-random-perl  libdbd-mysql-perl libwww-mechanize-perl libjson-perl && \
    cpan install Algorithm::BinPack::2D
