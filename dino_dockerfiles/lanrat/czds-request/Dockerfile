FROM python:2-slim
MAINTAINER Ian Foster <ian@vorsk.com>

RUN pip install selenium

ADD request.py request-run.sh /usr/src/czds-request/

USER 1000

WORKDIR /tmp/

CMD ["/usr/src/czds-request/request-run.sh"]
