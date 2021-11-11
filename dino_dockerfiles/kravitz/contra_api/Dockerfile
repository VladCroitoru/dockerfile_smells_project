FROM golang:latest

MAINTAINER Dmitry Kravtsov <idkravitz@gmail.com>


RUN apt-get update && apt-get install -y build-essential libssl-dev \
	&& useradd -r -m contra
USER contra
WORKDIR /home/contra
ENV GOPATH /home/contra
ENV GO15VENDOREXPERIMENT 1

RUN cp ~/.profile ~/.oldprofile && curl https://raw.githubusercontent.com/creationix/nvm/v0.30.2/install.sh | bash \
	&& . ~/.profile && nvm install 5.6.0 && nvm use 5.6.0 \
	&& npm install jade jstransformer-markdown-it --global \
	&& mkdir -p bin pkg src/github.com/kravitz/contra_api \
  && go get github.com/Masterminds/glide

USER root

RUN apt-get remove -y build-essential libssl-dev && apt-get autoremove -y && apt-get autoclean -y && \
	apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD . src/github.com/kravitz/contra_api/
ADD www/ www/
RUN chown -R contra:contra www src

USER contra

RUN . ~/.profile && nvm use 5.6.0 && jade www && mv ~/.oldprofile ~/.profile && rm -rf ~/.nvm
# Manual caching: if developer runs glide up on his working dir, then
# build would use versions, pulled externally, instead of trying to glide up internally
RUN cd src/github.com/kravitz/contra_api && [ -d vendor ] || ~/bin/glide up
RUN go install github.com/kravitz/contra_api
EXPOSE 8080

ENTRYPOINT ["./bin/contra_api"]
