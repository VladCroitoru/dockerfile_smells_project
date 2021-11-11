FROM python:alpine

MAINTAINER RockYuan <RockYuan@gmail.com>

RUN apk --update add libxml2-dev libxslt-dev libffi-dev gcc musl-dev libgcc openssl-dev curl bash && \
	pip install scrapy scrapy-splash

CMD ["python3"]