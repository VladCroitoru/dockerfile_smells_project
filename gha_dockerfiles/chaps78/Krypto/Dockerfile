FROM ubuntu:18.04



RUN   apt-get update \
  && apt-get install -y python3-pip python3-dev\
  && pip3 install krakenex



ADD . /app/


RUN python3 app/toto.py

    

WORKDIR /app 


CMD python3 quatre.py
