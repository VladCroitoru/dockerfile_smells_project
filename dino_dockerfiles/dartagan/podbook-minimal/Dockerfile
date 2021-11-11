FROM python:3-alpine

ENV UUID_NAMESPACE=29bd3b17-cd2e-46eb-886a-4dbf0319c068

RUN mkdir /podbook/
WORKDIR /podbook/

# TODO:
# Waiting for the update to Alpine 3.5 so that these packages may be directly installed, 
# rather than built with gcc. Remove build-dependencies steps.
# When that day happens, perhaps we can use the nginx base image
# and bake that into here too.
#RUN apk add --no-cache \
#    py3-flask \
#    py3-lxml

ADD requirements.txt /podbook/

RUN apk add --no-cache \
    libxslt \
 && apk add --no-cache --virtual build-dependencies \
    gcc \
    libxml2-dev \
    libxslt-dev \
    musl-dev \
 && pip3 install -r requirements.txt \
 && apk del build-dependencies

ENV PYTHONUNBUFFERED True

ADD . /podbook/

CMD python podbook

