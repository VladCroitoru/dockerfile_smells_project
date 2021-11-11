FROM python:2.7
MAINTAINER Dan Osborne <daniel@projectcalico.org>

RUN pip install docopt
RUN easy_install http://downloads.mesosphere.io/master/debian/8/mesos-0.26.0-py2.7-linux-x86_64.egg 

ADD framework /framework
ENTRYPOINT ["python", "/framework/calico_framework.py"]
