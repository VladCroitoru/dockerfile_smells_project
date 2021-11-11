FROM python:3.8-alpine3.14

WORKDIR /code

RUN apk --no-cache add gcc g++ make zlib jpeg-dev zlib-dev

# ADD requirements.in /code/
# RUN pip install pip-tools
# RUN pip-compile requirements.in

ADD requirements.txt /code/
RUN pip install -r requirements.txt
