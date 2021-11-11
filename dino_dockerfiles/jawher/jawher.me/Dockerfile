FROM debian:jessie

MAINTAINER Jawher Moussa

RUN apt-get update && \
	apt-get -y dist-upgrade && \
	apt-get install -y git python-pip && \
	apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY requirements.txt /tmp/

RUN pip install -r /tmp/requirements.txt

WORKDIR /blog

ENTRYPOINT ["/usr/bin/make"]

CMD ["html"]

EXPOSE 8000