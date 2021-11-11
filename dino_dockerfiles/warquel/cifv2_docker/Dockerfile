FROM ubuntu:15.10

MAINTAINER Warren Raquel <warquel@gmail.com>

ENV CIF_ES_HOST localhost:9200
ENV CIF_USER root
ENV CIF_GROUP root

EXPOSE 53
EXPOSE 53/udp
EXPOSE 80
EXPOSE 443
EXPOSE 5000
EXPOSE 9200
EXPOSE 4961
EXPOSE 4963

RUN echo "Building CIFv2 Container" \
    && apt-get update \
    && apt-get -y upgrade \
    && echo 'Acquire::ForceIPv4 "true";' > /etc/apt/apt.conf.d/99force-ipv4 \
    && apt-get install -qq wget software-properties-common python-software-properties apt-utils \
    && add-apt-repository -y "deb http://ppa.launchpad.net/chris-lea/zeromq/ubuntu wily main" \
    && add-apt-repository -y "deb http://ppa.launchpad.net/maxmind/ppa/ubuntu wily main" \
    && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys DE1997DCDE742AFA \
    && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys B9316A7BC7917B12 \
    && echo "postfix postfix/mailname string localhost" | debconf-set-selections \
    && echo "postfix postfix/main_mailer_type string 'Internet Site'" | debconf-set-selections \
    && apt-get update \
    && apt-get install -y unbound supervisor elasticsearch geoipupdate curl build-essential libmodule-build-perl libssl-dev nginx curl mailutils build-essential git-core automake rng-tools openjdk-7-jre-headless libtool pkg-config vim htop libzmq3 libzmq3-dev libffi6 libmoose-perl libmouse-perl libanyevent-perl liblwp-protocol-https-perl libxml2-dev libexpat1-dev libgeoip-dev geoip-bin python-dev starman ntp cpanminus libtest-autoloader-perl

RUN /usr/share/elasticsearch/bin/elasticsearch -d \
    && /usr/bin/openssl req -subj '/CN=cif.local/O=ACME' -new -newkey rsa:2048 -days 365 -nodes -x509 -keyout /etc/ssl/private/cif.key -out /etc/ssl/certs/cif.crt \
    && cpanm Regexp::Common Moo@1.007000 Mouse@2.4.1 \
    && cpanm AutoLoader \
    && cpanm --force --notest ZMQ::FFI@0.17 \
    && cpanm --force --notest https://github.com/csirtgadgets/ZMQx-Class/archive/master.tar.gz \
    && cpanm Log::Log4perl@1.44 \
    && cpanm --force Test::Exception@0.32 \
    && cpanm MaxMind::DB::Reader@0.050005 GeoIP2@0.040005 Hijk@0.19

RUN cpanm --force --notest git://github.com/csirtgadgets/p5-cif-sdk.git@afae699500333cca1ae53b87b56e4ca639bbf4f3 \
    && cpanm --force --notest https://github.com/kraih/mojo/archive/v5.82.tar.gz \
    && cpanm Search::Elasticsearch@1.19 \
    && cpanm --force --notest http://search.cpan.org/CPAN/authors/id/H/HA/HAARG/local-lib-2.000015.tar.gz \
    && echo 'HRNGDEVICE=/dev/urandom' >> /etc/default/rng-tools \
    && cd /tmp \
    && git clone -b 2.00.00-rc.16 https://github.com/csirtgadgets/massive-octo-spice.git cifv2 \
    && cd /tmp/cifv2 \
    && ./autogen.sh \
    && ./configure --enable-geoip --sysconfdir=/opt/cif/etc --localstatedir=/opt/cif/var --prefix=/opt/cif \
    && mkdir -p /opt/cif/var/cache \
    && mkdir -p /opt/cif/www \
    && make \
    && make deps \
    && make install \
    && mkdir -p /opt/cif/elasticsearch \
    && cp /tmp/cifv2/elasticsearch/*.json /opt/cif/elasticsearch \
    && apt-get -y remove build-essential automake autoconf libtool libssl-dev libzmq3-dev libxml2-dev libexpat1-dev libgeoip-dev python-dev cpanminus \
    && apt-get -y autoremove \
    && rm -rf /tmp/cifv2 \
    && rm -rf /root/.cpanm \
    && rm -rf /tmp/* \
    && echo "Base install complete"

ADD ./configs/nginx.conf /etc/nginx/nginx.conf
ADD ./configs/nginx-cif.conf /etc/nginx/sites-available/default
ADD ./configs/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
ADD ./configs/geoipupdate.cron /etc/cron.montly/geoipupdate
ADD ./configs/unbound.conf /etc/unbound/unbound.conf.d/unbound.conf
ADD ./configs/GeoIP.conf /etc/GeoIP.conf
ADD ./scripts/cif.ops /opt/cif/bin/cif.ops
ADD ./files/index.html /opt/cif/www/index.html

CMD /usr/bin/supervisord -c /etc/supervisor/supervisord.conf
