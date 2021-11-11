FROM ubuntu

MAINTAINER xoyabc <lxh1031138448@gmail.com>

RUN apt-get update; \
    apt-get -y upgrade

RUN apt-get -y install g++ git python2.7 curl vim iproute2 iproute2-doc
RUN ln -s /usr/bin/python2.7 /usr/bin/python
RUN curl https://bootstrap.pypa.io/get-pip.py -o /tmp/get-pip.py 
RUN python /tmp/get-pip.py
RUN pip2 install requests bs4

RUN mkdir /home/git; \
    cd /home/git; \
    git clone https://github.com/xoyabc/search_movies.git -b master;
