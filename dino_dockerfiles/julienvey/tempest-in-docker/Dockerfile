FROM ubuntu:14.04
MAINTAINER Julien Vey <vey.julien@gmail.com>

RUN apt-get update

# Install git, python and essential tools
RUN apt-get install -y git python-setuptools curl ftp
RUN easy_install pip

# Install dependencies
RUN apt-get install -y libxml2-dev libxslt-dev lib32z1-dev
RUN apt-get install -y python2.7-dev python-dev libssl-dev
RUN apt-get install -y python-libxml2 libxslt1-dev libsasl2-dev
RUN apt-get install -y libsqlite3-dev libldap2-dev libffi-dev

# Setup Environment by Cloning tempest
RUN git clone https://github.com/openstack/tempest.git

# installing tempest dependencies
RUN pip install -r /tempest/requirements.txt
RUN pip install -r /tempest/test-requirements.txt

# Copy sample configuration
RUN mkdir /etc/tempest
RUN cp tempest/etc/tempest.conf.sample /etc/tempest/tempest.conf
RUN cp tempest/etc/accounts.yaml.sample /etc/tempest/accounts.yaml.sample

# Running tempest setup
RUN cd tempest && python setup.py install
RUN cd tempest && testr init

WORKDIR /tempest
ENTRYPOINT ["testr", "run", "--subunit"]
