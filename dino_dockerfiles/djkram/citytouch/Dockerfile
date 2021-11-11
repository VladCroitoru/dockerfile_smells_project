FROM ubuntu:trusty
MAINTAINER Marc Planagumà <mplanaguma@bdigital.org>

# Init and update ubuntu
RUN apt-get -y update
RUN apt-get -y upgrade
RUN locale-gen --no-purge en_US.UTF-8
ENV LC_ALL en_US.UTF-8
RUN update-locale LANG=en_US.UTF-8

# Install Essentials
RUN apt-get install -y build-essential wget sysv-rc
RUN apt-get -y install supervisor

# Install Python 2.7
RUN apt-get install -y python libpq-dev python-dev python-setuptools
RUN apt-get install -y python-pip python-virtualenv
RUN apt-get install -y python-numpy python-scipy ipython cython
RUN apt-get install -y binutils libproj-dev gdal-bin

# Install Pico
RUN pip install psycopg2 django greenlet gensim scikit-learn pico
RUN cd /tmp && wget --quiet --no-check-certificate https://github.com/surfly/gevent/archive/1.0rc2.tar.gz &&\
	tar -xf 1.0rc2.tar.gz && cd gevent-1.0rc2 &&\
	python setup.py build && python setup.py install

# Install Apache2
RUN apt-get install -y apache2