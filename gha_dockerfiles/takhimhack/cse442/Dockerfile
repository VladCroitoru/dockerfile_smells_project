FROM ubuntu:18.04

RUN apt-get update

ENV HOME /root

WORKDIR /root


RUN apt-get update --fix-missing
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get install -y python3-venv
RUN python3 -m venv cse442env
RUN cse442env/bin/pip3 install --upgrade pip
RUN apt-get install -y nodejs
RUN apt-get install -y npm

COPY requirements.txt requirements.txt

RUN cse442env/bin/pip3 install -r requirements.txt

COPY . .


EXPOSE $PORT

#Run main.py
CMD cse442env/bin/python3 main.py $PORT