from continuumio/anaconda:2.5.0

RUN apt-get --yes  install gcc

RUN pip install pylab plot

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

ONBUILD COPY requirements.txt /usr/src/app/

ONBUILD RUN pip install --no-cache-dir -r requirements.txt

ONBUILD COPY . /usr/src/app