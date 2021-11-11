FROM alpine

RUN apk add --no-cache \
	bash \
	g++ \
	gmp-dev \
	openssl-dev \
	libffi-dev \
	python \
	python-dev \
	py-pip \
	rng-tools \
	vim 

RUN pip install --upgrade pip \
 && pip install blockstack

CMD /bin/sh