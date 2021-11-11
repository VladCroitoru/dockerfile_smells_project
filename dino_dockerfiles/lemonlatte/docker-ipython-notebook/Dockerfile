FROM ubuntu:14.04
MAINTAINER Jim Yeh <lemonlatte@gmail.com>

RUN apt-get -y update
RUN apt-get -y install git python-pip python-dev supervisor 

RUN pip install virtualenv
RUN mkdir ipython-notebook

WORKDIR /ipython-notebook
RUN virtualenv .

RUN apt-get -y install libzmq-dev
RUN ./bin/pip install ipython[all]
 
RUN ./bin/pip install numpy

RUN apt-get -y install gfortran libopenblas-dev liblapack-dev
RUN ./bin/pip install scipy 

RUN apt-get -y install libfreetype6-dev
RUN ./bin/pip install matplotlib

RUN ./bin/pip install pandas

RUN mkdir workspace

ADD supervisor.ipython.conf /etc/supervisor/conf.d/ipython.conf

WORKDIR /

VOLUME /ipython-notebook/workspace
EXPOSE 8888
CMD ["supervisord", "-n"]
