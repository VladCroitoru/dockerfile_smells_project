FROM ubuntu:latest
RUN apt-get update; apt-get install -qy python-pip
RUN pip install docker-compose
RUN wget -o /usr/local/bin/docker-compose \
		https://github.com/docker/machine/releases/download/v0.3.0/docker-machine_linux-amd64; \
	chmod 755 /usr/local/bin/docker-compose
RUN mkdir /machines
ADD . /opt/
WORKDIR /machines
ENTRYPOINT /opt/machine-compose
