FROM python:3.3-wheezy
MAINTAINER Alexander Vaniashev

ENV CQ_CODE=/code
#ENV DEBIAN_FRONTEND=noninteractive

RUN mkdir $CQ_CODE
WORKDIR $CQ_CODE
COPY requirements.txt requirements.txt
COPY oursql-0.9.4 oursql

COPY sources.list /etc/apt/sources.list
RUN apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 3B4FE6ACC0B21F32
RUN curl http://repogen.simplylinux.ch/txt/gpg_4ac57e70e4a0141d994f3e956ea39bc0e582996f.txt | tee /etc/apt/gpg_keys.txt
RUN apt-get update
RUN apt-get install debian-keyring 
RUN apt-get install debian-archive-keyring
RUN apt-get -y build-dep python3-scipy 


RUN pip install uwsgi
RUN pip install git+https://github.com/jorgecarleitao/django-sphinxql.git
RUN pip install Cython
RUN pip install Numpy
WORKDIR $CQ_CODE/oursql
RUN python setup.py install
WORKDIR $CQ_CODE
RUN pip install -r $CQ_CODE/requirements.txt

RUN dpkg --add-architecture i386
RUN add-apt-repository ppa:ubuntu-wine/ppa
RUN apt-get update
RUN apt-get -y --fix-missing install wine1.7
ENV WINEPREFIX=/root/wine32
ENV WINEARCH=win32
RUN winecfg
ENV WINEPREFIX=/root/wine64
ENV WINEARCH=win64
RUN winecfg

VOLUME ["/data/qvark/www"]
EXPOSE 8000

WORKDIR /data/qvark/www/
CMD uwsgi --http 0.0.0.0:8000 --wsgi-file __main/wsgi.py  --pidfile __main/running.pid --master --buffer-size=65536
