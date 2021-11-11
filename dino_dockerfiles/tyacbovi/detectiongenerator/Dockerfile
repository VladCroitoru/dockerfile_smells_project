FROM ubuntu:16.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update \
 && apt-get -y --no-install-recommends install apt-utils

RUN apt-get -y --no-install-recommends install \
	python-pip \
	build-essential \
	python2.7 \
	python2.7-dev \
	curl \
	libleveldb1v5 \
	libleveldb-dev \
	unzip

RUN pip install --upgrade pip \
 && pip install setuptools \
 && pip install plyvel \
 && pip install simplejson \
 && pip install urllib3

#Installing kafka with python client
ENV LIBRDKAFKA_VERSION 0.9.4
RUN curl -Lk -o /root/librdkafka-${LIBRDKAFKA_VERSION}.tar.gz https://github.com/edenhill/librdkafka/archive/v${LIBRDKAFKA_VERSION}.tar.gz && \
    tar -xzf /root/librdkafka-${LIBRDKAFKA_VERSION}.tar.gz -C /root && \
    cd /root/librdkafka-${LIBRDKAFKA_VERSION} && \
    ./configure && make && make install && make clean && ./configure --clean

ENV CPLUS_INCLUDE_PATH /usr/local/include
ENV LIBRARY_PATH /usr/local/lib
ENV LD_LIBRARY_PATH /usr/local/lib

RUN pip install confluent-kafka

#Install DetectionGenerator
WORKDIR /usr/local/src
RUN curl -Lk -o detection_generator.zip https://github.com/tyacbovi/DetectionGenerator/archive/master.zip && \
    unzip detection_generator.zip
RUN cd DetectionGenerator-master/DetectionGenerator/

ENV PYTHONPATH "/usr/local/src/DetectionGenerator-master/"
ENTRYPOINT ["python", "/usr/local/src/DetectionGenerator-master/DetectionGenerator/__main__.py"]
