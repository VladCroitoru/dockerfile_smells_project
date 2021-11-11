FROM centos:7.6.1810

MAINTAINER RPS <devops@rpsgroup.com>

USER root

# Install nodejs/npm and friends:
RUN (curl -sL https://rpm.nodesource.com/setup_10.x | bash) && \
    yum -y install nodejs && \
    npm install -g grunt-cli yarn

# Install container dependencies:
RUN yum -y install epel-release && \
    yum -y update && \
    yum -y install make git m4 zlib-devel redis

RUN yum -y groupinstall "Development Tools"

# Python 3.6 update:
RUN yum update -y \
    && yum install -y python36 python36-libs python36-devel python36-pip \
    which gcc udunits2-devel expat-devel openldap-devel httpd \
    && yum clean all

# UDUNITS
RUN curl -O ftp://ftp.unidata.ucar.edu/pub/udunits/udunits-2.2.25.tar.gz \
    && tar xzf udunits-2.2.25.tar.gz \
    && cd udunits-2.2.25 \
    && /bin/sh configure --prefix=/usr/local \
    && make -j \
    && make install \
    && cd .. \
    && rm -rf udunits-2.2.25 \
    && rm -rf udunits-2.2.25.tar.gz

# HDF5
RUN curl -O https://support.hdfgroup.org/ftp/HDF5/releases/hdf5-1.8/hdf5-1.8.19/src/hdf5-1.8.19.tar.gz \
    && tar xzf hdf5-1.8.19.tar.gz \
    && cd hdf5-1.8.19 \
    && /bin/sh configure --prefix=/usr/local \
    && make -j \
    && make install \
    && cd .. \
    && rm -rf hdf5-1.8.19 \
    && rm -rf hdf5-1.8.19.tar.gz

# NETCDF4
RUN curl -O ftp://ftp.unidata.ucar.edu/pub/netcdf/netcdf-4.4.1.1.tar.gz \
    && tar xzf netcdf-4.4.1.1.tar.gz \
    && cd netcdf-4.4.1.1 \
    && /bin/sh configure --prefix=/usr/local \
    && make -j \
    && make install \
    && cd .. \
    && rm -rf netcdf-4.4.1.1 \
    && rm -rf netcdf-4.4.1.1.tar.gz

RUN systemctl enable httpd.service

# pipenv installation
RUN pip3.6 install pipenv
RUN ln -s /usr/bin/pip3.6 /bin/pip
RUN rm /usr/bin/python
# python must be pointing to python3.6
RUN ln -s /usr/bin/python3.6 /usr/bin/python

RUN pip install Cython --install-option="--no-cython-compile"
RUN pip install numpy

# Startup Shell script:
COPY contrib/docker/my_init.d/run.sh /etc/run.sh

# Add our project
RUN mkdir /usr/lib/ccweb /var/run/datasets /var/log/ccweb

COPY cchecker_web /usr/lib/ccweb/cchecker_web
COPY Gruntfile.js Assets.json package.json requirements.txt\
     app.py setup.py worker.py /usr/lib/ccweb/
COPY contrib/config/config.yml /usr/lib/ccweb/

# User for installing requirements
RUN useradd -ms /bin/bash ccweb
RUN chown -R ccweb:ccweb /usr/lib/ccweb /var/run/datasets /var/log/ccweb
WORKDIR /usr/lib/ccweb

# Install python dependencies
RUN pip --version && pip install -r requirements.txt

# Install local dependencies
USER ccweb
RUN yarn install && \
    grunt

USER root

# Add our daemons:
RUN mkdir -p /etc/service/ccweb-app /etc/service/ccweb-worker-01
COPY contrib/docker/runit/web.sh /etc/service/ccweb-app/run
COPY contrib/docker/runit/worker.sh /etc/service/ccweb-worker-01/run
RUN chmod +x /etc/service/ccweb-app/run /etc/service/ccweb-worker-01/run

# Don't run as root user
USER ccweb

CMD ["/bin/bash", "/etc/run.sh"]
EXPOSE 3000
