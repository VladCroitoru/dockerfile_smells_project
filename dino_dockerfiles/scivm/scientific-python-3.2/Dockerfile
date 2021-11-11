#
# Copyright (c) 2014 Science Automation, Inc. http://www.scivm.com.  All rights reserved.
# 
# email: contact@scivm.com
# support:  http://support.scivm.com
#
# The MIT License (MIT)
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.  The motd file shall remain
# included to the Dockerfile and unmodified.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
FROM ubuntu:12.04

#RUN echo "deb ftp://mirror.hetzner.de/ubuntu/packages precise main restricted universe multiverse" > /etc/apt/sources.list
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list
RUN apt-get update
RUN apt-get upgrade -y

# install ssh server
RUN apt-get -y install openssh-server; mkdir -p /var/run/sshd; locale-gen en_US en_US.UTF-8

# install supervisor
RUN apt-get -y install supervisor
ADD supervisord.conf /etc/supervisor/supervisord.conf
RUN mkdir -p /var/log/supervisor

# compilers and basic tools
RUN apt-get install -y gfortran build-essential make gcc build-essential git-core curl wget vim-tiny nano

# install python
ADD repo.sh /tmp/repo.sh
ADD fkrull-deadsnakes-precise.list /tmp/fkrull-deadsnakes-precise.list
RUN chmod 755 /tmp/repo.sh; /tmp/repo.sh
RUN apt-get update
RUN apt-get install -y python3.2 python3.2-dev

# database client
# sqllite, postgresql, mysql client
RUN apt-get install -y libsqlite3-dev sqlite3 postgresql-client-9.1 postgresql-client-common libpq5 libpq-dev libmysqlclient-dev

# needed for httplib2
RUN apt-get install -y libxml2-dev libxslt-dev

# distribute
RUN wget http://python-distribute.org/distribute_setup.py; python distribute_setup.py; rm -f /distribute*

# pip
RUN wget https://raw.github.com/pypa/pip/master/contrib/get-pip.py; python get-pip.py; rm -f /get-pip.py

# python-PIL
RUN apt-get install -y python-imaging libpng-dev libfreetype6 libfreetype6-dev

# pyzmq
RUN apt-get install -y libzmq-dev

# hdf5
ADD hdf5_install.sh /tmp/hdf5_install.sh
RUN chmod 755 /tmp/hdf5_install.sh; /tmp/hdf5_install.sh

# blas
ADD blas.sh /tmp/blas.sh
RUN chmod 755 /tmp/blas.sh; /tmp/blas.sh
ENV BLAS /usr/local/lib/libfblas.a

# lapack
ADD lapack.sh /tmp/lapack.sh
RUN chmod 755 /tmp/lapack.sh; /tmp/lapack.sh
ENV LAPACK /usr/local/lib/liblapack.a

# virtualenv
# This gets a current version.  Do not use the version packaged with ubuntu
RUN pip install virtualenv==1.10.1

# scientific python packages
ADD packages.sh /tmp/packages.sh
ADD requirements.sh /tmp/requirements.sh
RUN chmod 755 /tmp/packages.sh; /tmp/packages.sh

# set root password
RUN echo 'root:scivm' | chpasswd

# motd
RUN rm -rf /etc/update-motd.d /etc/motd
ADD motd /etc/motd

EXPOSE 8888 22

# run container with supervisor
CMD ["/usr/bin/supervisord"]
