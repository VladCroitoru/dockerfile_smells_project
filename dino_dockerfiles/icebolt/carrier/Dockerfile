FROM centos:centos6

ADD etc/yum.repos.d/epel.repo /etc/yum.repos.d/epel.repo
ADD etc/yum.repos.d/jimmy.repo /etc/yum.repos.d/jimmy.repo

RUN \
 rpm --import file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-6 && \
 rm -rf /var/lib/yum/history/*.sqlite && \
 yum -y update --disablerepo=epel\* && \
 yum -y groupinstall "Development Tools" && \
 yum -y install bison-devel cmake freetype-devel gd-devel glib2-devel gtk+-devel libaio-devel libcurl-devel libjpeg-turbo-devel libmcrypt-devel libpng-devel libxml2-devel ncurses-devel net-snmp-devel pcre-devel re2c nmap telnet vim wget tar 
 yum -y install zlib zlib-devel && \
 yum -y install openssl-devel && yum clean all

RUN \
 wget -O ruby-install-0.5.0.tar.gz https://github.com/postmodern/ruby-install/archive/v0.5.0.tar.gz && \
 tar -xzvf ruby-install-0.5.0.tar.gz && \
 rm -f ruby-install-0.5.0.tar.gz && \
 cd ruby-install-0.5.0/ && \
 make install && \
 ruby-install ruby 2.1.3 && \
 ln -s /opt/rubies/ruby-2.1.3/bin/ruby /usr/sbin/ruby && \
 make clean && \
 cd .. && rm -rf ruby-install-0.5.0 && \
 cd /usr/local/src && rm -rf ruby-2.1.3 ruby-2.1.3.tar.bz2

RUN \
 wget http://production.cf.rubygems.org/rubygems/rubygems-2.4.2.zip && \
 unzip rubygems-2.4.2.zip && \
 rm -f rubygems-2.4.2.zip && \
 cd rubygems-2.4.2 && \
 ruby setup.rb && \
 ln -s /opt/rubies/ruby-2.1.3/bin/gem /usr/bin/gem && \
 gem sources --remove https://rubygems.org/ && \
 gem sources -a http://ruby.taobao.org/ && \
 gem install gem-fast && \
 #gem update --system && \
 cd .. && rm -rf rubygems-2.4.2

RUN \
 wget http://prdownloads.sourceforge.net/tcl/tcl8.5.15-src.tar.gz && \
 gunzip < tcl8.5.15-src.tar.gz | tar xvf - && \
 rm -f tcl8.5.15-src.tar.gz && \
 cd tcl8.5.15 && cd unix && \
 ./configure --prefix=/usr --enable-threads --mandir=/usr/share/man && \
 make && sed -i -e "s@^\(TCL_SRC_DIR='\).*@\1/usr/include'@" -e "/TCL_B/s@='\(-L\)\?.*unix@='\1/usr/lib@"  tclConfig.sh && \
 make install && make install-private-headers && ln -v -sf tclsh8.5 /usr/bin/tclsh && chmod -v 755 /usr/lib/libtcl8.5.so && \
 make clean && \
 cd / && rm -rf tcl8.5.15

RUN \
 wget http://www.cmake.org/files/v2.8/cmake-2.8.12.1.tar.gz && \
 tar -zxvf cmake-2.8.12.1.tar.gz && \
 rm -f cmake-2.8.12.1.tar.gz && \
 cd cmake-2.8.12.1 && \
 ./configure && make && make install && \
 make clean && \
 cd .. && rm -rf cmake-2.8.12.1

RUN \
 yum -y install perl-CPAN  perl-Nagios-Plugin.noarch perl-YAML && yum clean all && ln -s /usr/lib64/perl5/CORE/libperl.so /usr/lib64/libperl.so

RUN \
 yum -y install docker-io e4fsprogs && yum clean all
