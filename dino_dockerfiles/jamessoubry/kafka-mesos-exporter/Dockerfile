FROM python:3.6

RUN pip3 install prometheus_client requests

# This is something I like to do as it adds the Dockerfile to the image for easy reverse engineering
ADD . /

RUN chmod 755 /kafka-mesos-exporter.py

ENTRYPOINT [ "/kafka-mesos-exporter.py" ]