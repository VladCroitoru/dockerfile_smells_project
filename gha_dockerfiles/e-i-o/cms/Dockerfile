FROM debian:9.8

RUN apt-get -qqy update
RUN apt-get -y install python3.5=3.5.3-1+deb9u2 g++-6=6.3.0-18+deb9u1 gcc-6=6.3.0-18+deb9u1 openjdk-8-jdk
RUN apt-get -qqy install postgresql-client gettext python2.7 iso-codes shared-mime-info stl-manual cgroup-bin supervisor libcap-dev
RUN apt-get -qqy install python-dev libpq-dev libcups2-dev libyaml-dev libffi-dev
RUN apt-get -qqy install git wget zip
RUN wget http://eio.ee/get-pip.py
RUN python2 get-pip.py

WORKDIR /cms
COPY . .
RUN git submodule update --init 
RUN pip2 install -r requirements.txt 
RUN pip2 install -r dev-requirements.txt 
RUN python2 prerequisites.py -y --no-conf --as-root install 
RUN python2 setup.py install

COPY cms.conf.test /usr/local/etc/cms.conf
