# Version 1.1.0
FROM ubuntu:15.04
MAINTAINER Mike Bartoli "michael.bartoli@pomona.edu"
RUN apt-get update
RUN apt-get -y install \
	python \
	build-essential \
	python-dev \
	python-pip \
	wget \
	unzip \
	git \
	openjdk-8-jdk \
	openjdk-8-jre
RUN pip install numpy nltk ner flask flask-restful 

WORKDIR /home
RUN wget -O ner.zip http://nlp.stanford.edu/software/stanford-ner-2015-04-20.zip
RUN unzip ner.zip

WORKDIR /home
RUN git clone https://github.com/mbartoli/restful-ner
WORKDIR /home/restful-ner/ner
RUN cp start.sh /home/stanford-ner-2015-04-20/start.sh

WORKDIR /home/stanford-ner-2015-04-20
CMD ["/bin/bash","-c","chmod +x start.sh && sh start.sh"]
