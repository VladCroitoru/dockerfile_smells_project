FROM ubuntu:14.04

RUN apt-get update
RUN apt-get install -y wget make gcc binutils python-pip python-dev libssl-dev libffi-dev bash libapparmor1 libsystemd-journal-dev

WORKDIR /root

RUN pip install python-consul Jinja2

ADD . /app

WORKDIR /app

CMD ["python", "main.py", "bind.cfg.tmpl"]

