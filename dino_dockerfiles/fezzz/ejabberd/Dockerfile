# Set the base image
FROM centos
# Dockerfile author / maintainer
MAINTAINER Felix Stellmacher <docker@istsotoll.de>

EXPOSE 5222
EXPOSE 5269

RUN groupadd -r ejabberd && useradd -m -r -g ejabberd ejabberd

RUN yum update -y
RUN yum install epel-release -y
RUN yum install -y wget libwebp libwebp-devel gd gd-devel imagemagick-devel libjpeg-turbo-devel libpng-devel openssl openssl-devel zlib expat expat-devel libyaml-devel libyaml pam-devel pam
RUN yum groupinstall -y 'Development Tools'

RUN cd /tmp; wget -O es.rpm https://packages.erlang-solutions.com/erlang-solutions-1.0-1.noarch.rpm
RUN cd /tmp; rpm -Uvh es.rpm
RUN yum install -y esl-erlang

RUN cd /tmp; wget -O ejabberd.tgz https://www.process-one.net/downloads/downloads-action.php?file=/ejabberd/19.09/ejabberd-19.09.tgz
RUN cd /tmp; tar -xf ejabberd.tgz

RUN cd /tmp/ejabberd-19.09; ./configure  --disable-graphics --enable-user=ejabberd --enable-mysql --enable-pam --enable-zlib
RUN cd /tmp/ejabberd-19.09; make
RUN cd /tmp/ejabberd-19.09; make install

CMD ["/usr/local/sbin/ejabberdctl","foreground"]
