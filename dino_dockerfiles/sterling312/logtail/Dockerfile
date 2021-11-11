# sterling312/base
#
FROM ubuntu:14.04

MAINTAINER Gang Huang doc.n.try@gmail.com

# compiled package install
RUN apt-get update
RUN apt-get install -y git-core wget curl vim build-essential python-dev g++

# install s3cmd for python2.7
RUN apt-get install -y python-pip python-lxml

# copy repo
COPY . /logtail
RUN pip install -r /logtail/requirements.txt
RUN chmod +x /logtail/startup.sh
VOLUME /tmp

CMD /logtail/startup.sh

EXPOSE 8000
