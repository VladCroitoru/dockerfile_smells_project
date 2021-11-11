FROM gliderlabs/alpine:latest
MAINTAINER Matthew Gall <docker@matthewgall.com>

WORKDIR /app
COPY . /app

RUN apk add --update \
	build-base \
	git \
	python3 \
	python3-dev \
	py-pip \
	py-virtualenv \
	&& rm -rf /var/cache/apk/* \
	&& virtualenv -p python3 /env \
	&& /env/bin/pip install -r /app/requirements.txt

EXPOSE 5000
CMD ["/env/bin/python", "app.py"]