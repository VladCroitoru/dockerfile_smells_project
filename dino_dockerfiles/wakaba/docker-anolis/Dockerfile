FROM debian:sid

RUN apt-get update
RUN apt-get -y install mercurial python-lxml python-cssselect python-setuptools
RUN easy_install html5lib

RUN hg clone http://bitbucket.org/ms2ger/anolis
RUN cd anolis && python setup.py install
