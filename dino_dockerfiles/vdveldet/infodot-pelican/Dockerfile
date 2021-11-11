FROM phusion/baseimage

MAINTAINER vdvelde.t@gmail.com

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update 
RUN apt-get install -y -q python-pip
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN pip install --upgrade pip
RUN pip install --upgrade pelican

# BUG https://github.com/wadou/pelican/commit/24817a5543edf88af73474ce17405eac62758b39#diff-52fe2de2a8486e716ec2398752ead4dd
#RUN sed -i -e "s/locale.getlocale()\[0\].split('_')\[0\]/'English'/g" /usr/local/lib/python2.7/dist-packages/pelican/tools/pelican_quickstart.py

RUN mkdir documents

WORKDIR /documents
VOLUME /documents

CMD ["/bin/bash"]



