FROM centos:6.7

RUN yum clean all
RUN yum update -y
RUN yum install -y epel-release.noarch
RUN yum update -y
RUN yum install -y tar wget
COPY elgis-release-6-6_0.noarch.rpm /tmp/elgis-release-6-6_0.noarch.rpm
RUN rpm -Uvh /tmp/elgis-release-6-6_0.noarch.rpm
COPY armadillo-3.800.2-1.el6.x86_64.rpm /tmp/armadillo-3.800.2-1.el6.x86_64.rpm
RUN cd /tmp && yum install -y armadillo-3.800.2-1.el6.x86_64.rpm
RUN yum install -y hdf5
RUN yum install -y gcc-c++ zlib-devel libxml2-devel bison openssl python-devel subversion libxslt-devel libcurl-devel gdal-devel proj-devel libuuid-devel openssl-devel fcgi-devel yum install java-1.7.0-openjdk-devel autoconf flex bzip2
RUN cd /tmp && svn co http://www.zoo-project.org/svn/tags/rel-1.5.0 zoo-project && cd /tmp/zoo-project/thirds/cgic206 && make
RUN cd /tmp/zoo-project/zoo-project/zoo-kernel && autoconf && ./configure
RUN cd /tmp/zoo-project/zoo-project/zoo-kernel && make && make install
RUN cp /tmp/zoo-project/zoo-project/zoo-kernel/main.cfg /usr/lib/cgi-bin
ENV LD_LIBRARY_PATH=/usr/local/lib

COPY zoo-project.conf /etc/ld.so.conf.d/zoo-project.conf
RUN ldconfig
RUN yum clean all
RUN yum install -y mod_fcgid httpd

COPY httpd.conf /etc/httpd/conf/httpd.conf
EXPOSE 80

CMD ["apachectl","-D","FOREGROUND"]
