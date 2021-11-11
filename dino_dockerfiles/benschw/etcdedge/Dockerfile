FROM ubuntu

RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list
RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get install -y python python-setuptools curl
RUN easy_install redis 


ADD ./start.py /opt/start.py

CMD /usr/bin/python /opt/start.py
