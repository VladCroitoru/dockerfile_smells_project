FROM python:2.7.14-slim-stretch

ADD requirements.txt /
COPY dumpy/ /dumpy
ENV PYTHONPATH=:/dumpy

RUN apt-get update &&\
    apt-get --no-install-recommends -y install mysql-client bzip2 &&\
    pip install -r /requirements.txt &&\
    rm -rf /var/lib/apt/lists/*

WORKDIR /

CMD ["/usr/local/bin/python", "dumpy/dumper.py", "-a", "-v"]
