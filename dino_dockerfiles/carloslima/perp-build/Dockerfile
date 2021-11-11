FROM centos:centos6

MAINTAINER Carlos Lima <carlos@cpan.org>

RUN yum install -y tar gcc bzip2

WORKDIR /root
RUN curl -O http://www.fefe.de/dietlibc/dietlibc-0.33.tar.bz2 \
        && sha256sum dietlibc-0.33.tar.bz2 | grep '68838893790ddd7a42bc1a06e5435054e1dc1914e4b53d2d6c92f603d3b315f5' \
        && tar -jxf dietlibc-0.33.tar.bz2 \
        && rm dietlibc-0.33.tar.bz2
RUN cd dietlibc-0.33 && make && install bin-*/diet /usr/local/bin

RUN curl -O http://b0llix.net/perp/distfiles/perp-2.07.tar.gz \
        && sha256sum perp-2.07.tar.gz | grep '1222fe31c16014d8b2a78416f93ba9f8c31eddbc381adc9021fa5d9764475815' \
        && tar -zxf perp-2.07.tar.gz \
        && rm perp-2.07.tar.gz
ADD conf.mk /root/perp-2.07/conf.mk
RUN cd perp-2.07 && make && make strip

RUN yum install -y which rpm-build rpmdevtools; \
        wget http://ftp5.gwdg.de/pub/opensuse/repositories/home:/andnagy/RedHat_RHEL-6/x86_64/checkinstall-1.6.2-20.4.x86_64.rpm \
        && sha256sum checkinstall-*.rpm | grep '23c84c9d25d632f5843e591dfed687639860b8bd289855a3cef94c307ab559a9' \
        && rpm -i checkinstall-*.rpm \
        && rpmdev-setuptree
RUN cd /root/perp-2.07 && checkinstall -R -y --install=no --showinstall --pkgrelease=2
ADD installer /installer
CMD /installer
