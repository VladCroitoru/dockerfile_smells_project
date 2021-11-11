FROM golang:latest

MAINTAINER Dmitry Kravtsov <idkravitz@gmail.com>

RUN apt-get update && apt-get -y install dos2unix unzip p7zip-full git build-essential cmake \
  && cd /usr/local && mkdir transims4 transims4/bin && cd transims4 \
	&& git clone https://github.com/kravitz/transims4.git src && mkdir build \
	&& cd build && cmake ../src && make -j2 && cp bin/* ../bin && cd .. \
	&& rm -rf src build \
  && apt-get remove -y build-essential cmake && apt-get autoremove -y \
  && apt-get autoclean -y \
  && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
  && useradd -r -m contra

USER contra
WORKDIR /home/contra
ENV GOPATH /home/contra
ENV PATH /usr/local/transims4/bin:$PATH
ENV GO15VENDOREXPERIMENT=1

RUN mkdir -p bin src/github.com/kravitz/contra_exec pkg \
    && go get github.com/Masterminds/glide

ADD . src/github.com/kravitz/contra_exec

RUN cd src/github.com/kravitz/contra_exec && [ -d vendor ] || ~/bin/glide up
RUN go test github.com/kravitz/contra_exec
RUN go install github.com/kravitz/contra_exec

EXPOSE 8080

ENTRYPOINT ["./bin/contra_exec"]
