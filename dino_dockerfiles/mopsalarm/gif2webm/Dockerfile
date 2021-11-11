FROM python:3.6-alpine
MAINTAINER Mopsalarm

RUN apk --update add ffmpeg coreutils curl

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache -r /tmp/requirements.txt

ENV PYTHONPATH=/app
COPY gif2webm.py /app/


EXPOSE 5000
CMD /usr/local/bin/python -m bottle -s cherrypy -b 0.0.0.0:5000 gif2webm
