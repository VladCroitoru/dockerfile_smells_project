FROM debian
MAINTAINER Sébastien Brennion LeanBI

RUN apt-get update
RUN apt-get install -y python2.7 python-dateutil
RUN apt-get install -y python-pip nano
RUN apt-get autoremove -y
RUN apt-get clean

RUN pip install boto
ENV TERM=xterm
ADD swissmeteo.py /opt/swissmeteo/

CMD ["python","/opt/swissmeteo/swissmeteo.py"]