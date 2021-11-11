FROM ubuntu:18.04

MAINTAINER Manh Nguyen Duc (manh.nguyenduc@campus.tu-berlin.de), Patrik Schneider (patrik@kr.tuwien.ac.at)
LABEL Description="SR Hackathon 2021 integration Dockerised Simulation of Urban MObility(SUMO)"

ENV SUMO_HOME /usr/share/sumo
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
# Install system dependencies.

RUN APT_INSTALL="apt-get install -y --no-install-recommends" && \
	PIP3_INSTALL="python3 -m pip --no-cache-dir install --upgrade" && \
	apt update && \
	DEBIAN_FRONTEND=noninteractive $APT_INSTALL \
	python3 \
	python3-pip \
	software-properties-common \
	&& \

	$PIP3_INSTALL \
	flask \
	pyyaml \
	websocket_server \
	websocket-client \
	requests \
	rdflib \
	rdflib-jsonld==0.6.1 \
	&& \
	ldconfig && \
	apt-get clean && \
	apt-get autoremove

RUN add-apt-repository -y ppa:sumo/stable
RUN apt update
RUN apt install -y sumo sumo-tools 

RUN apt remove software-properties-common -y
RUN apt clean -y && apt autoremove -y

WORKDIR /root
COPY . .

CMD ["python3", "src/main.py"]
