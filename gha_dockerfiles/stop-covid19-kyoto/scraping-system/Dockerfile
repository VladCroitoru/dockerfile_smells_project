FROM python:3.8.5-alpine3.11

ENV APPDIR=/app/

RUN mkdir ${APPDIR}
WORKDIR ${APPDIR}

ADD requirements.txt ${APPDIR}
RUN pip install -r requirements.txt

ADD . /app/