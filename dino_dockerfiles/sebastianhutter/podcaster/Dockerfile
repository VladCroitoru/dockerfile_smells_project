FROM python:3-alpine
MAINTAINER Sebastian Hutter <mail@sebastian-hutter.ch>

RUN apk --no-cache add tini
ADD requirements.txt /
RUN pip install -r /requirements.txt
ADD app /app/

ENTRYPOINT ["/sbin/tini", "--"]
CMD ["python", "/app/podcaster/podcaster.py"]
