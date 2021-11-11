FROM futoase/docker-centos-base:utc

MAINTAINER Keiji Matsuzaki <futoase@gmail.com>
 
# setup network
# reference from https://github.com/dotcloud/docker/issues/1240#issuecomment-21807183
RUN echo "NETWORKING=yes" > /etc/sysconfig/network
 
# setup remi repository
RUN wget http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
RUN wget http://rpms.famillecollet.com/enterprise/remi-release-6.rpm
RUN curl -O http://rpms.famillecollet.com/RPM-GPG-KEY-remi; rpm --import RPM-GPG-KEY-remi
RUN rpm -Uvh remi-release-6*.rpm epel-release-6*.rpm

RUN yum -y install --enablerepo=epel,remi pkgconfig glib2-devel gettext libxml2-devel pango-devel cairo-devel ipa-gothic-fonts

# setup nginx repository
ADD ./template/nginx.repo /etc/yum.repos.d/nginx.repo

RUN yum -y update
RUN yum -y groupinstall --enablerepo=epel,remi "Development Tools"
RUN yum -y install --enablerepo=epel,remi openssl-devel git sqlite sqlite-devel libyaml-devel libxslt-devel nginx

# mkdir
RUN mkdir -p /tmp/download

# reference of https://gist.github.com/sonots/8661761
RUN yum -y install --enablerepo=epel,remi cairo-devel libxml2-devel pango-devel pango libpng-devel freetype perl-ExtUtils-MakeMaker
#RUN yum -y install rrdtool rrdtool-devel
RUN wget -O /tmp/download/rrdtool-1.4.8.tar.gz http://oss.oetiker.ch/rrdtool/pub/rrdtool-1.4.8.tar.gz 
RUN cd /tmp/download && tar -xvzf rrdtool-1.4.8.tar.gz
RUN cd /tmp/download/rrdtool-1.4.8 && ./configure --prefix=/usr --libdir=/usr/lib64
RUN cd /tmp/download/rrdtool-1.4.8 && make && make install

# setup ruby-install
RUN wget -O /tmp/download/ruby-install-0.3.4.tar.gz https://github.com/postmodern/ruby-install/archive/v0.3.4.tar.gz
RUN cd /tmp/download && tar -xvzf ruby-install-0.3.4.tar.gz
RUN cd /tmp/download/ruby-install-0.3.4 && make install

# cleanup
RUN rm -rf /tmp/download

RUN ruby-install ruby 2.0.0-p353

ENV PATH /opt/rubies/ruby-2.0.0-p353/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

RUN gem install bundle --no-ri --no-rdoc 

# setup focuslight
RUN git clone https://github.com/tagomoris/focuslight.git /root/focuslight
RUN cd /root/focuslight && bundle ins
RUN cd /root/focuslight && bundle ex rake init

# setup nginx
RUN rm /etc/nginx/conf.d/default.conf
RUN rm /etc/nginx/conf.d/example_ssl.conf
ADD ./template/nginx.conf /etc/nginx/conf.d/focuslight.conf
RUN service nginx restart

ADD ./startup.sh /root/startup.sh
RUN chmod +x /root/startup.sh

EXPOSE 80
CMD ["/root/startup.sh"]
