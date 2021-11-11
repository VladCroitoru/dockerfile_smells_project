from ubuntu:14.04

#install basic environment
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y aptitude
RUN apt-get install -y ipython
RUN apt-get install -y python-pip
RUN apt-get install -y man
RUN apt-get install -y vim
RUN apt-get install -y git

#install mongo
RUN pip install pymongo

#install sacred
RUN cd /root && git clone https://github.com/IDSIA/sacred.git && cd sacred && python setup.py install

VOLUME /root/rr
WORKDIR /root

CMD /bin/bash

