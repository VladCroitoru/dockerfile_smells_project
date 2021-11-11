FROM ubuntu:14.04.2
MAINTAINER Ondrej Klejch

WORKDIR /opt/app/alex-asr
RUN apt-get update && \
    apt-get install -y build-essential libatlas-base-dev python python-dev python-pip git wget gfortran g++ unzip zlib1g-dev automake autoconf libtool subversion

ADD requirements.txt prepare_env.sh /opt/app/alex-asr/
RUN pip install -r requirements.txt && bash prepare_env.sh

ADD . /opt/app/alex-asr/
RUN make -j  4 && python setup.py install
