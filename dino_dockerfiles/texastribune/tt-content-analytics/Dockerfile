FROM ubuntu:14.04
MAINTAINER tech@texastribune.org

RUN apt-get update
RUN apt-get install -yq python-pip
RUN pip install --quiet google-api-python-client==1.5.0 slacker==0.9.15 requests==2.18.4

COPY ./tt_analytics /app/
ENTRYPOINT ["python", "/app/run.py"]
