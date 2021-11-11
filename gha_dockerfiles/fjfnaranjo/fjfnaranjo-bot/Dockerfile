FROM python:3.8.3-alpine

COPY requirements.txt /requirements.txt

RUN apk add --no-cache \
		gcc \
		python3-dev \
		musl \
		musl-dev \
		libffi \
		libffi-dev \
		openssl \
		openssl-dev \
		libev \
		libev-dev \
	&& pip3 install --no-cache-dir -r /requirements.txt \
	&& apk del \
		python3-dev \
		musl-dev \
		libffi-dev \
		openssl-dev \
		libev-dev \
	&& rm /requirements.txt

COPY . /bot
