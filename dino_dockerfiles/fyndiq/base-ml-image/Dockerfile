FROM fyndiq/python-alpine-kafka:python3.7.0-librdkafka0.11.5

RUN set -x \
    && apk update \
    && apk --no-cache add \
        freetype \
        openblas \
        build-base \
        freetype-dev \
        gfortran \
        openblas-dev

COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt
