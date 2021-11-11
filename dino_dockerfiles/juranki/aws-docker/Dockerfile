FROM docker:17.09

RUN apk add --no-cache \
		ca-certificates \
		curl \
		openssl \
		build-base \
		python-dev \
		libffi-dev \
		openssl-dev \
		py-pip

RUN pip install awscli fabric

RUN mkdir ~/.aws \
  && touch ~/.aws/credentials \
  && touch ~/.aws/config
