FROM debian:buster
MAINTAINER nobody@nowhere.ws

RUN set -x \
	&& apt-get update && apt-get install -y --no-install-recommends \
		gir1.2-poppler-0.18 \
		python3-cairo \
		python3-gi \
		python3-gi-cairo \
		python3-pip \
		python3-setuptools \
		python3-wheel

RUN mkdir /srv/eventmap
WORKDIR /srv/eventmap
COPY requirements.txt /srv/eventmap/requirements.txt

RUN pip3 install -r requirements.txt

COPY ./ /srv/eventmap

VOLUME [ "/srv/eventmap/data" ]

CMD [ "python3", "run_server.py", "-P" ]

EXPOSE 8023
