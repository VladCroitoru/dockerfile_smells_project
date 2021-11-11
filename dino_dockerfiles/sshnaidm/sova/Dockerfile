FROM alpine:3.5
LABEL maintainer "sshnaidm <einarum@gmail.com>"
LABEL name "sova"

RUN apk add --no-cache \
    bash \
    ca-certificates \
    gcc \
    git \
    libffi-dev \
    libxml2-dev \
    libxslt-dev \
    openssl-dev \
    make \
    musl-dev \
    python3 \
    python3-dev \
    uwsgi uwsgi-python3 \
    xz-dev && \
python3 -m ensurepip && \
rm -r /usr/lib/python*/ensurepip && \
pip3 install --upgrade pip setuptools && \
rm -r /root/.cache && \
ln -s /usr/bin/python3 /usr/bin/python && \
ln -s /usr/lib/uwsgi/python3_plugin.so /usr/lib/uwsgi/python_plugin.so

COPY requirements.txt /requirements.txt
COPY test-requirements.txt /test-requirements.txt

RUN pip3 install --upgrade -r /requirements.txt -r /test-requirements.txt && \
    mkdir -p /cidata

COPY . /app
COPY entrypoint.sh /entrypoint.sh
COPY uwsgi.ini /uwsgi.ini

WORKDIR /app
VOLUME ["/cidata"]
VOLUME ["/logdir"]
EXPOSE 8090

ENTRYPOINT ["/entrypoint.sh"]
CMD ["-d"]
