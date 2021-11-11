FROM ubuntu:trusty

RUN apt-get update && \
    apt-get install -y --no-install-recommends python-pip && \
    apt-get clean && \
    pip install python-tutum==0.16.21

COPY . /app
WORKDIR /app

CMD ["/usr/bin/python", "client.py"]
