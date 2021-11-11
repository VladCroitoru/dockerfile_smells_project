FROM centos:centos6
MAINTAINER Boris Serebrov

# Based on https://www.digitalocean.com/community/tutorials/how-to-set-up-python-2-7-6-and-3-3-3-on-centos-6-4

RUN rpm -ivh http://dl.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm

RUN yum -y update
RUN yum groupinstall -y development
RUN yum install -y zlib-dev openssl openssl-devel sqlite-devel bzip2-devel \
        tar git java-1.7.0-openjdk java-1.7.0-openjdk-devel \
        gcc gcc-c++ \
        mysql-devel postgresql-devel \
        atlas-sse3-devel lapack-devel && \
        cat /var/log/yum.log

# Install python 2.7.6
WORKDIR /tmp
ADD https://www.python.org/ftp/python/2.7.6/Python-2.7.6.tgz /tmp/
RUN tar -xvzf Python-2.7.6.tgz
WORKDIR /tmp/Python-2.7.6
RUN ./configure --prefix=/usr/local && \
    make && \
    make altinstall

# create a symlink python -> python2.7
RUN ln -s /usr/local/bin/python2.7 /usr/local/bin/python

# Install setuptools
WORKDIR /tmp
ADD https://pypi.python.org/packages/source/s/setuptools/setuptools-1.4.2.tar.gz /tmp/
RUN tar -xvzf setuptools-1.4.2.tar.gz
WORKDIR /tmp/setuptools-1.4.2
RUN python2.7 setup.py install && \
    # Install pip and virtualenv
    curl https://bootstrap.pypa.io/get-pip.py | python2.7 - && \
    pip install virtualenv

# install shapely dependencies, should be installed after python
RUN yum install -y geos geos-devel geos-python

# Install pandas/ numpy / scipy / scikit-learn and their deps
RUN pip install six==1.9.0 \
 numpy==1.9.2 \
 scipy==0.15.1 \
 scikit-learn==0.16.1

RUN pip install pandas==0.16.1

RUN pip install Flask==0.10.1 \
 boto==2.38.0 \
 pytz==2015.4 \
 py_descriptive_statistics==0.2 \
 simplejson==3.6.5 \
 xmltodict==0.9.2 \
 markdown2==2.3.0 \
 pygments==2.0.2 \
 pyzmq==13.0.2 \
 protobuf==3.0.0b2 \
 protobuf-to-dict==0.1.0 \
 shapely==1.5.13 \
 psycopg2==2.6.1 \
 SQLAlchemy==1.0.6 \
 Flask-SQLAlchemy-Session==1.1 \
 alembic==0.7.6 \
 sqlalchemy-utils==0.30.12 \
 MySQL-python==1.2.5 \
 pprofile==1.7.3 \
 requests==2.9.1
