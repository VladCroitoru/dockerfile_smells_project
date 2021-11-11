FROM ubuntu:16.04
MAINTAINER Wouter van Atteveldt (wouter@vanatteveldt.com)

RUN apt-get -qq update && apt-get install -y python3-flask python3-pip python3-lxml 

RUN pip3 install "nlpipe>=0.50" typing

CMD python3 -m nlpipe.worker $NLPIPE_OPTIONS $NLPIPE_SERVER $NLPIPE_MODULE

