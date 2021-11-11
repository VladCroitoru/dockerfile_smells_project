FROM ubuntu:18.04

RUN mkdir /app

WORKDIR /app

COPY . . 

ENV TZ=Europe/Kiev
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN ./install_dependencies.bash
RUN pip3 install -r requirements.txt
RUN ./install_darknet.bash

RUN pip3 install gunicorn
CMD exec gunicorn --bind :5000 --workers 1 --threads 8 --timeout 0 app:app

