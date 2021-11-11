FROM buildpack-deps:jessie

RUN apt-get purge -y python.*
ENV LANG C.UTF-8
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys C01E1CAD5EA2C4F0B8E3571504C367C218ADD4FF

RUN apt-get update && apt-get -y install wget python-pip
RUN pip install  --upgrade pip
RUN wget http://www.python.org/ftp/python/2.3/Python-2.3.tgz
RUN tar xfz Python-2.3.tgz
RUN cd Python-2.3 && ./configure && make && make install &&  exit
RUN  which python

RUN pip install --no-cache-dir virtualenv
RUN pip install pymysql
RUN pip install requests
RUN pip install beautifulsoup4

RUN mkdir /home/python2
WORKDIR /home/python2
