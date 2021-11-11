FROM alpine:latest

# Metadata
ARG VERSION
ARG VCS_REF
ARG BUILD_DATE
LABEL org.label-schema.vendor="Neufund" \
      org.label-schema.url="https://neufund.org" \
      org.label-schema.name="Signature Authentication Server" \
      org.label-schema.description="JWT Authentication server using Ethereum Signatures" \
      org.label-schema.version="0.0.1" \
      org.label-schema.vcs-url="https://github.com/Neufund/signature-authentication-server" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.docker.schema-version="1.0"

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
ENV PYTHONPATH $PYTHONPATH:/urs/src/app

ADD requirements.txt .
RUN \
    apk add --no-cache --virtual build-deps build-base automake autoconf libtool python3-dev libffi-dev openssl-dev &&\
    apk add --no-cache uwsgi-python3 openssl &&\
    python3 -m ensurepip &&\
    rm -r /usr/lib/python*/ensurepip &&\
    pip3 install --upgrade pip setuptools &&\
    pip3 install cffi>=1.3.0 &&\
    pip3 install setuptools_scm &&\
    pip3 install pytest-runner==2.6.2 &&\
    pip3 install -r requirements.txt &&\
    apk del --purge build-deps &&\
    rm -r /root/.cache

ADD uwsgi.ini uwsgi.ini
ADD *.py /usr/src/app/
RUN \
    python3 ./test.py &&\
    rm ./test.py

ENV FLASK_DEBUG 0
ENV FLASK_HOST 0.0.0.0
ENV FLASK_APP server

EXPOSE 5000

CMD ["uwsgi", "--ini", "uwsgi.ini"]
