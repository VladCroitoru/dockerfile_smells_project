FROM armv7/armhf-ubuntu
MAINTAINER Shawn Nock <nock@nocko.se>

ENV APPNAME c3next

RUN apt-get update && apt-get install -y --no-install-recommends \
	python-virtualenv pypy libffi6 openssl libpq-dev gcc pypy-dev \
	git \
	&& rm -rf /var/lib/apt/lists/*

WORKDIR /home/$APPNAME
RUN python -m virtualenv -p /usr/bin/pypy /appenv
COPY requirements.txt .
RUN . /appenv/bin/activate; pip install -r requirements.txt
COPY . ./
RUN . /appenv/bin/activate; pip install -e .
CMD ./docker_entrypoint.sh
