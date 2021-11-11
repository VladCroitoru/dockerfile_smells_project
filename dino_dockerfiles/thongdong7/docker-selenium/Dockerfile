FROM ubuntu:14.04
MAINTAINER Thong Dong, thongdong7@gmail.com

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y
RUN apt-get install -y build-essential
RUN apt-get install -y ca-certificates
RUN apt-get install -y gcc
RUN apt-get install -y git
RUN apt-get install -y libpq-dev
RUN apt-get install -y make
RUN apt-get install -y python-pip
RUN apt-get install -y python2.7
RUN apt-get install -y python2.7-dev
RUN apt-get install -y ssh
RUN apt-get install -y libxml2-dev
RUN apt-get install -y libxslt1-dev
RUN apt-get install -y libfreetype6 libfreetype6-dev libfontconfig1 libfontconfig1-dev
RUN apt-get autoremove
RUN apt-get clean

RUN pip install -U "setuptools==3.4.1"
RUN pip install -U "pip==1.5.4"
RUN pip install -U "Mercurial==2.9.1"
RUN pip install -U "virtualenv==1.11.4"
RUN pip install -U "supervisor"
RUN pip install -U "urllib3"
RUN pip install -U "pyyaml"
RUN pip install -U "selenium"
RUN pip install -U "psutil"
RUN pip install -U "hashlib"
RUN pip install -U "lxml"
RUN pip install -U "beautifulsoup4"

# Install phantomjs
ENV PHANTOM_JS "phantomjs-1.9.8-linux-x86_64"
RUN wget https://bitbucket.org/ariya/phantomjs/downloads/$PHANTOM_JS.tar.bz2
RUN tar xvjf $PHANTOM_JS.tar.bz2
RUN mv $PHANTOM_JS /usr/local/share
RUN ln -sf /usr/local/share/$PHANTOM_JS/bin/phantomjs /usr/local/bin
