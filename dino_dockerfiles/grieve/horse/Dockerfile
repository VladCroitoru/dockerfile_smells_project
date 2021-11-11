FROM python:2.7
MAINTAINER Ryan Grieve <me@ryangrieve.com>

ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
RUN pip install pillow

ADD ./app /app

WORKDIR /app

VOLUME ["/data"]

CMD ["bash", "start.sh"]

EXPOSE 5000
