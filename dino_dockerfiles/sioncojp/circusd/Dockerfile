FROM centos:6.8
MAINTAINER Shohei Koyama sion_cojp@yahoo.co.jp

# Install python
RUN yum install gcc-c++ zlib-devel openssl-devel initscripts -y

WORKDIR /usr/local/src
RUN curl -O https://www.python.org/ftp/python/2.7.13/Python-2.7.13.tgz \
  && tar zxf Python-2.7.13.tgz

WORKDIR /usr/local/src/Python-2.7.13
RUN ./configure && make && make altinstall \
  && mv /usr/local/src/Python-2.7.13/python /usr/bin/python

RUN  sed -i -e "s/^#\!\/usr\/bin\/python/#\!\/usr\/bin\/python2.6/g" /usr/bin/yum

# Install pip
RUN curl -kL https://bootstrap.pypa.io/get-pip.py | python

# Install circus
RUN pip install circus==0.13 \
  && mkdir /var/log/circusd && chmod 775 /var/log/circusd \
  && mkdir /etc/circusd/ && chmod 755 /etc/circusd/

# Setting circus.ini
ADD circus.ini /etc/circusd/
RUN chmod 755 /etc/circusd/circus.ini

# Setting /etc/init.d/circusd
ADD circusd_initscript.sh /etc/init.d/circusd
RUN chmod 755 /etc/init.d/circusd

# Clean all
WORKDIR /tmp/
RUN rm -rf /usr/local/src/Python-2.7.13 \
  && rm -rf /usr/local/src/Python-2.7.13.tgz
