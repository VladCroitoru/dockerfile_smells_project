FROM ubuntu:14.04

CMD echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections
RUN apt-get -qq update -y
RUN apt-get -qq install -y python
RUN apt-get -qq install -y python-pip
RUN pip install selenium
