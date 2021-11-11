FROM python:2
MAINTAINER katima90

WORKDIR /usr/src/app
EXPOSE 5000

RUN git clone https://github.com/anru/rsted.git
RUN pip install -r ./rsted/pip-requirements.txt
CMD cd ./rsted ; ./application.py

