FROM python:2.7
MAINTAINER Ryan Grieve <me@ryangrieve.com>

ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

ADD . /app

WORKDIR /app

VOLUME ["/data"]

CMD ["python", "main.py"]

EXPOSE 5000
