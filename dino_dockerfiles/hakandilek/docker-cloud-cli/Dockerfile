FROM docker:stable

RUN apk add --no-cache python2 python2-dev py2-pip && \
    python -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip install --upgrade pip setuptools && \
    rm -r /root/.cache

RUN pip install docker-cloud

RUN docker-cloud -v
RUN docker -v
