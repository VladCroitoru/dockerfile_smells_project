FROM ubuntu:latest
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ="Europe/Amsterdam"
RUN apt-get -y update && \
    apt-get -y dist-upgrade && \
    apt-get -y install gcc g++ cmake wget autoconf curl libcurl4-openssl-dev git libboost-date-time-dev libboost-regex-dev nlohmann-json3-dev libantlr4-runtime-dev libantlr4-runtime4.8 && \
	wget http://131.123.42.38/lmcrs/v1.0.0/srcml_1.0.0-1_ubuntu18.04.deb && \
    apt-get -y install ./srcml_1.0.0-1_ubuntu18.04.deb && \
	mkdir controller
COPY . /controller
RUN cd controller && \
	mkdir build && \
	cd build && \
	cmake ../SearchSECOController && \
	cmake --build .
ENTRYPOINT ["./controller/build/searchseco", "start"]