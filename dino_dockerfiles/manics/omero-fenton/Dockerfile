FROM python:2
MAINTAINER spli@dundee.ac.uk

RUN pip install sleekxmpp
RUN useradd -m logbot
USER logbot
COPY . /home/logbot/omero-fenton

WORKDIR /home/logbot/omero-fenton
ENTRYPOINT ["python", "OmeroFenton.py"]
