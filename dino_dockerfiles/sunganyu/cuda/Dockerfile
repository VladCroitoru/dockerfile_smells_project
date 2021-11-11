FROM nvidia/cuda

RUN apt-get update -qqy
RUN apt-get -qqy install software-properties-common 
RUN add-apt-repository ppa:jonathonf/python-2.7
RUN apt-get update -qqy
RUN apt-get -qqy install vim nano git wget

RUN apt-get -qqy install   \
       python \
       build-essential \
       fonts-liberation \
       gconf-service \
       libappindicator1 \
       libasound2 \
       libcurl3 \
       libffi-dev \
       libgconf-2-4 \
       libindicator7 \
       libnspr4 \
       libnss3 \
       libpango1.0-0 \
       libssl-dev \
       libxss1 \
       python-dev \
       python-pip \
       python-pyasn1 \
       python-pyasn1-modules \
       unzip \
       wget \
       xdg-utils \
       xvfb \
       python-mysqldb \
       build-essential \
       libmysqlclient-dev \
       && \
    pip  install --upgrade pip
