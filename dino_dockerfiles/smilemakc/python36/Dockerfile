FROM alpine:3.6
MAINTAINER Maks Balashov <main@maksbalashov.ru>

RUN apk add --no-cache python3 gcc python3-dev postgresql-dev g++ gcc libxslt-dev libffi-dev && \
    python3 -m ensurepip && \

    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    rm -r /root/.cache

RUN addgroup -S -g 777 py36_bot && adduser -D -S -G py36_bot -u 777 py36_bot

EXPOSE 8000-8008

RUN mkdir -p /code && chown -R py36_bot /code
RUN pip install ipython pytils aiohttp aiopg
WORKDIR /code
CMD ["/bin/ash"]