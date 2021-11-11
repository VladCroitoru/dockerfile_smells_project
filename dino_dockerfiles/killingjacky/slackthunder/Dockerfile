FROM python:2.7
MAINTAINER Jack Shao "jacky.shaoxg@gmail.com"

#install python modules
RUN apt-get update && \
    apt-get install -qqy --force-yes vim

#add the files into image
RUN mkdir -p /app
COPY . /app

RUN pip install -r /app/requirements.txt

CMD python /app/main.py
