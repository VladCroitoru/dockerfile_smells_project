FROM alpine:3.4

RUN apk add --no-cache py-pip gcc python-dev musl-dev libxml2-dev libxslt-dev \
  && pip install bs4 lxml

VOLUME ["/usr/src/exterstellar"]

ENTRYPOINT ["/usr/src/exterstellar/exterstellar.py"]
