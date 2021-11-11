FROM centos:6.7
MAINTAINER hidetarou2013 <hidetoshi_maekawa@e-it.co.jp>

RUN yum -y update && yum -y upgrade

# tag:Apache2.2.15
RUN yum install -y httpd
EXPOSE 80 

# tag:SSL
RUN yum install -y openssl mod_ssl
EXPOSE 443

# tag:PHP5.3.3
RUN yum install -y php php-mbstring php-mysq

# tag:PHP5.3.3.1
RUN yum install -y php php-mbstring php-mysql php-devel php-mcrypt 

# tag:SVN1.6.11
# tag:SVN_repo1
RUN yum install -y subversion mod_dav_svn mod_dontdothat
RUN mkdir /var/lib/svnrepos/
ADD "$PWD"/subversion.conf /etc/httpd/conf.d/subversion.conf
ADD "$PWD"/svnrepos_pass /etc/httpd/conf/svnrepos_pass
ADD "$PWD"/create_svn_repo.sh /tmp/create_svn_repo.sh
RUN chmod 755 /tmp/create_svn_repo.sh
ENV TARGET_REPO repo1
RUN exec sh /tmp/create_svn_repo.sh $TARGET_REPO
RUN sed -i -e 's/tmp1/repo1/g' /etc/httpd/conf.d/subversion.conf
RUN cat -n /etc/httpd/conf.d/subversion.conf | grep repo1

RUN ls -la /etc/httpd/conf/
RUN ls -la /etc/httpd/conf.d/
RUN ls -la /tmp/
RUN rpm -qa | grep mod_dav_svn

# tag:AJP
ADD "$PWD"/httpd-proxy.conf /etc/httpd/conf.d/httpd-proxy.conf

# tag:debian-tomcat8_jaxrs-sample
#RUN sed -i -e 's/app/jaxrs-sample/g' /etc/httpd/conf.d/httpd-proxy.conf
#RUN sed -i -e 's/tomcat/debian-tomcat8/g' /etc/httpd/conf.d/httpd-proxy.conf

# tag:ubuntu-tomcat8_jaxrs-sample
#RUN sed -i -e 's/app/jaxrs-sample/g' /etc/httpd/conf.d/httpd-proxy.conf
#RUN sed -i -e 's/tomcat/ubuntu-tomcat8/g' /etc/httpd/conf.d/httpd-proxy.conf

# tag:bc01_tomcat_1_jaxrs-sample
RUN sed -i -e 's/app/jaxrs-sample/g' /etc/httpd/conf.d/httpd-proxy.conf
RUN sed -i -e 's/tomcat/bc01_tomcat_1/g' /etc/httpd/conf.d/httpd-proxy.conf

#CMD /usr/sbin/httpd -DFOREGROUND
ENTRYPOINT /etc/init.d/httpd start && /etc/rc.d/init.d/svnserve restart && /bin/bash