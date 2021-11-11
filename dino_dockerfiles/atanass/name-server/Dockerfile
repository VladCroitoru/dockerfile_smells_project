FROM ubuntu:latest
MAINTAINER Atanas Dichev <dichev.atanas@gmail.com>

ENV FOO bar

RUN apt-get update
RUN apt-get install python-pip python wget -y
RUN pip install redis
RUN wget https://pypi.python.org/packages/source/W/Werkzeug/Werkzeug-0.10.4.tar.gz#md5=66a488e0ac50a9ec326fe020b3083450
RUN tar -xvf Werkzeug-0.10.4.tar.gz && cd Werkzeug-0.10.4 && python setup.py install

ADD name.py .
CMD ["python", "name.py"]
