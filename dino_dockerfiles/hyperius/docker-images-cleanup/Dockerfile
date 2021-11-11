FROM python:2.7-alpine
MAINTAINER Denis Savenko <denis.savenko@gmail.com>

RUN pip install docker

ADD ./cleanup.py /usr/local/bin/cleanup.py

CMD ["/usr/local/bin/python", "/usr/local/bin/cleanup.py"]
