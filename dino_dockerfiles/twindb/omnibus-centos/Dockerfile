FROM centos:centos7
MAINTAINER dev@twindb.com

RUN yum -y install epel-release
RUN yum groupinstall -y 'Development Tools'

RUN yum install -y \
    git \
    which \
    openssl-devel \
    expat-devel \
    perl-ExtUtils-MakeMaker \
    perl-devel \
    zlib-devel \
    fakeroot \
    gcc \
    gcc-c++ \
    cmake \
    libaio \
    libaio-devel \
    automake \
    autoconf \
    libtool \
    bison \
    ncurses-devel \
    libgcrypt-devel \
    libev-devel \
    libcurl-devel \
    vim-common


COPY gpg/409B6B1796C275462A1703113804BB82D39DC0E3.txt /tmp/409B6B1796C275462A1703113804BB82D39DC0E3.txt
COPY gpg/7D2BAF1CF37B13E2069D6956105BD0E739499BDB.txt /tmp/7D2BAF1CF37B13E2069D6956105BD0E739499BDB.txt
RUN gpg2 --import /tmp/7D2BAF1CF37B13E2069D6956105BD0E739499BDB.txt
RUN gpg2 --import /tmp/409B6B1796C275462A1703113804BB82D39DC0E3.txt

RUN curl -sSL https://get.rvm.io | bash -s stable

RUN bash -lc "rvm requirements; \
        rvm install 2.6.1 ; \
        gem install bundler ;\
        "

RUN rm -rf /usr/local/rvm/src/ruby-*

CMD /bin/bash -l