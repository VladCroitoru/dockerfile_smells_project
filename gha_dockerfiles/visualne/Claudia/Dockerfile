FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

ENV PATH="/scripts:${PATH}"

copy ./requirements.txt /requirements.txt

#  For alpine images
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers mariadb-dev
RUN apk add --no-cache git
RUN apk add --no-cache mariadb-connector-c-dev


#  Installing requirements file.
RUN pip install -r requirements.txt
#  Removes virtual set of requirements.
RUN apk del .tmp

RUN mkdir /webapp
COPY ./webapp /webapp
WORKDIR /webapp

#  Creating media and static directories
RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

#  Installing opensky python client
RUN mkdir -p /opensky_python
RUN git clone https://github.com/openskynetwork/opensky-api.git /opensky_python
RUN pip install -e /opensky_python/python

RUN adduser -D user
RUN chown -R user:user /vol
RUN chmod -R 755 /vol/web
USER user