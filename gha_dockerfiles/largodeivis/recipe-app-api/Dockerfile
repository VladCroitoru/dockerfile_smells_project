FROM python:3.7-alpine
MAINTAINER Skuubiisnaxx

#run python in unbuffered mode. Recommended when running python on a Docker container
#Doesn't allow python to buffer the outputs, prints them directly.
#Avoids some complications when running Docker image with Python.
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-dependencies \
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-dependencies

#make directory
RUN mkdir /app

#default directory
WORKDIR /app

COPY ./app/ /app

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN adduser -D user
RUN chown -R user:user /vol/
RUN chmod -R 755 /vol/web

#if you dont set the user to user then Docker will run the image using the root account
#This is not recommended because: if app is compromised, they could have root access to the image
USER user
