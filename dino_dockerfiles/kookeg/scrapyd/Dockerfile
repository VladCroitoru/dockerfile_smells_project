FROM centos 
MAINTAINER kookeg<thinklang0917@gmail.com>

WORKDIR /data/python
ENV LANG en_US.UTF-8

RUN yum -y update  
RUN yum -y install epel-release
RUN yum -y install zsh curl wget git autoconf automake  g++ gcc make bzip2 zip  zlib zlib-devel openssl openssl-devel file libtool
RUN yum -y install patch gdbm-devel readline-devel bzip2-devel sqlite-devel openssh-server lszrz deltarpm kmod-devel
RUN yum clean all
RUN mkdir -p /usr/local/python2.7.12
RUN wget https://www.python.org/ftp/python/2.7.12/Python-2.7.12.tgz
RUN tar -zxvf Python-2.7.12.tgz
RUN cd /data/python/Python-2.7.12 && pwd && ./configure --prefix=/usr/local/python2.7.12 -enable-unicode=ucs4 && make \ 
	&& make install

RUN rm -rf Python-2.7.12
RUN rm -f Python-2.7.12.tgz
RUN rm -f /usr/bin/python
RUN ln -s /usr/local/python2.7.12/bin/python /usr/bin/python
RUN ln -s /usr/local/python2.7.12/bin/python-config /usr/bin/python-config
RUN sed -i "s/\/usr\/bin\/python/\/usr\/bin\/python2/" /usr/bin/yum
RUN sed -i "s/\/usr\/bin\/python/\/usr\/bin\/python2/" /usr/libexec/urlgrabber-ext-down
RUN ssh-keygen -t rsa -P "" -f /etc/ssh/ssh_host_rsa_key
RUN ssh-keygen -t ed25519 -P "" -f /etc/ssh/ssh_host_ed25519_key
RUN ssh-keygen -t ecdsa -P "" -f /etc/ssh/ssh_host_ecdsa_key
RUN wget -O get-pip.py 'https://bootstrap.pypa.io/get-pip.py'
RUN python get-pip.py
RUN ln -s /usr/local/python2.7.12/bin/pip /usr/bin/pip
RUN pip install virtualenv
RUN ln -s /usr/local/python2.7.12/bin/virtualenv /usr/bin/virtualenv
RUN echo "kookeg" | passwd --stdin root
RUN sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"


RUN yum -y install python-devel libffi-devel 
RUN wget ftp://sourceware.org/pub/libffi/libffi-3.2.1.tar.gz && tar -zxvf libffi-3.2.1.tar.gz
RUN cd /data/python/libffi-3.2.1  && ./configure  && make && make install 

RUN wget http://downloads.sourceforge.net/libxls/libxls-0.2.0.tar.gz && tar -zxvf libxls-0.2.0.tar.gz 
RUN cd /data/python/libxls-0.2.0  && ./configure  && make && make install 

RUN export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig:$PKG_CONFIG_PATH
RUN export LD_LIBRARY_PATH=/usr/local/lib
RUN pip install setuptools lxml wheel cryptography cffi 
RUN pip install scrapy scrapyd supervisor
RUN ln -s /usr/local/python2.7.12/bin/supervisord /usr/bin/supervisord
RUN ln -s /usr/local/python2.7.12/bin/scrapyd /usr/bin/scrapyd
ADD scrapyd.conf /etc/scrapyd/scrapyd.conf
ADD supervisord.conf /etc/supervisord.conf 
RUN mkdir -p /var/run/sshd /var/log/supervisor

VOLUME /data/python

VOLUME /data/scrapyd

EXPOSE 22 80 6800

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]
