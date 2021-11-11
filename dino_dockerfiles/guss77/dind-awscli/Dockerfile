FROM docker:latest

RUN \
	apk -Uuv add make gcc groff less \
		musl-dev libffi-dev openssl-dev \
		python3-dev py3-pip cargo && \
	pip install awscli awscli-plugin-endpoint docker-compose && \
	apk --purge -v del cargo musl-dev libffi-dev openssl-dev && \
	rm /var/cache/apk/*
