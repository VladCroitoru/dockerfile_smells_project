FROM talkincode/pypy
MAINTAINER jamiesun <jamiesun.net@gmail.com>


RUN add-apt-repository -y ppa:nginx/stable && \
    apt-get update -y && \
    apt-get install -y  mysql-client libmysqlclient-dev beanstalkd memcached nginx htop openssh-server libzmq-dev && \
    rm -rf /var/lib/apt/lists/*


# RUN cd /usr/local/src && \
#     wget http://pkgconfig.freedesktop.org/releases/pkg-config-0.29.tar.gz && \
#     tar xzvf pkg-config-0.29.tar.gz && \
#     cd pkg-config-0.29 && \
#     ./configure --with-internal-glib && \
#     make && \
#     make install && \
#     rm -fr /usr/local/src/pkg-config-0.29 && \
#     ldconfig

# RUN cd /usr/local/src && \
#     wget http://download.zeromq.org/zeromq-4.1.4.tar.gz && \
#     tar xzvf zeromq-4.1.4.tar.gz && \
#     cd zeromq-4.1.4 && \
#     ./configure --without-libsodium && \
#     make && \
#     make install && \
#     rm -fr /usr/local/src/zeromq-4.1.4 && \
#     ldconfig

RUN mkdir /var/run/sshd && \
    echo "root:toughstruct" | chpasswd && \
    sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    sed -i 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' /etc/pam.d/sshd

RUN pypy -m  pip install bottle
RUN pypy -m  pip install Mako
RUN pypy -m  pip install Beaker
RUN pypy -m  pip install MarkupSafe
RUN pypy -m  pip install PyYAML
RUN pypy -m  pip install Twisted
RUN pypy -m  pip install treq
RUN pypy -m  pip install tablib
RUN pypy -m  pip install cyclone
RUN pypy -m  pip install six
RUN pypy -m  pip install autobahn
RUN pypy -m  pip install pycrypto
RUN pypy -m  pip install pyOpenSSL>=0.14
RUN pypy -m  pip install service_identity
RUN pypy -m  pip install MySQL-python
RUN pypy -m  pip install SQLAlchemy
RUN pypy -m  pip install pyzmq
RUN pypy -m  pip install txzmq
RUN pypy -m  pip install beanstalkc
RUN pypy -m  pip install pybeanstalk
RUN pypy -m  pip install python-memcached
RUN pypy -m  pip install txyam
RUN pypy -m  pip install psutil
RUN pypy -m  pip install IPy

RUN echo "set nocompatible" >> /root/.vimrc && echo "set backspace=2" >> /root/.vimrc
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

EXPOSE 22
