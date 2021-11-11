#
# VERSION 0.0.1
#

FROM centos:centos6
MAINTAINER yukinagae "yuki.nagae1130@gmail.com"

# epel
RUN rpm -ivh http://ftp-srv2.kddilabs.jp/Linux/distributions/fedora/epel/6/x86_64/epel-release-6-8.noarch.rpm

# remi
RUN rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-6.rpm

# update
RUN yum -y update

# basic
RUN yum install -y wget
RUN yum install -y tar
RUN yum install -y gcc
RUN yum install -y make

# java
RUN yum -y install java-1.7.0-openjdk-devel

# avoid compile error
RUN yum install -y perl-ExtUtils-MakeMaker

# install git (Version 1.7.7.5 required)
RUN yum install -y gettext-devel expat-devel curl-devel zlib-devel openssl-devel
RUN wget -O /usr/local/src/git-1.8.5.tar.gz http://kernel.org/pub/software/scm/git/git-1.8.5.tar.gz
RUN tar xzvf /usr/local/src/git-1.8.5.tar.gz -C /usr/local/src
RUN cd /usr/local/src/git-1.8.5 && make prefix=/usr/local all && make prefix=/usr/local install

# install svn
RUN cd /usr/local/src
RUN curl -L -O http://pkgs.repoforge.org/rpmforge-release/rpmforge-release-0.5.3-1.el6.rf.x86_64.rpm
RUN rpm -ivh rpmforge-release-0.5.3-1.el6.rf.x86_64.rpm
RUN yum install -y --enablerepo=rpmforge-extras subversion

# install git-svn
RUN yum install -y --enablerepo=rpmforge-extras git-svn

# svn-tool
RUN wget -O /usr/local/src/svn-migration-scripts.jar https://bitbucket.org/atlassian/svn-migration-scripts/downloads/svn-migration-scripts.jar

# verify (optional)
RUN java -jar /usr/local/src/svn-migration-scripts.jar verify

# httpd
RUN yum install -y httpd
RUN chkconfig httpd on

EXPOSE 80

CMD service httpd start && tail -f /var/log/httpd/access_log
