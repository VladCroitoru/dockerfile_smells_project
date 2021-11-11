FROM ubuntu:14.04
MAINTAINER Luca Versari <veluca93@gmail.com>

RUN apt-get update
RUN apt-get -y install g++
RUN apt-get -y install postgresql-client
RUN apt-get -y install gettext
RUN apt-get -y install python2.7
RUN apt-get -y install iso-codes
RUN apt-get -y install shared-mime-info
RUN apt-get -y install stl-manual
RUN apt-get -y install cgroup-lite
RUN apt-get -y install supervisor
RUN apt-get -y install python-pip

# This apt-get is necessary until the following adopt python wheels:
#   * psycopg2
#   * pycups
#   * PyYAML
# (And until python wheels will support Linux binaries)
RUN apt-get -y install python-dev
RUN apt-get -y install libpq-dev
RUN apt-get -y install libcups2-dev
RUN apt-get -y install libyaml-dev

RUN apt-get -y install fpc

ADD . /oiiweb

RUN cd /oiiweb && \
    pip install -r REQUIREMENTS.txt && \
    python setup.py build && \
    python setup.py install

RUN apt-get -y install fpc
RUN apt-get -y install pypy
RUN curl -O https://bootstrap.pypa.io/get-pip.py && pypy get-pip.py && pypy -m pip install sortedcontainers

# See above about python wheels
RUN apt-get -y remove python-dev
RUN apt-get -y remove libpq-dev
RUN apt-get -y remove libcups2-dev
RUN apt-get -y remove libyaml-dev

COPY docker/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 8888 8889 8890
WORKDIR /problems
CMD cgroups-mount
CMD supervisord
