FROM ubuntu:14.04

RUN apt-get update \
  && apt-get install -y software-properties-common curl git \
  && add-apt-repository -y ppa:openjdk-r/ppa \
  && add-apt-repository -y ppa:brightbox/ruby-ng \
  && apt-get update \
  && apt-get install -y openjdk-8-jdk ruby2.4 \
  && gem install dpl \
  && gem install --pre asciidoctor-pdf

COPY . /home/
WORKDIR /home/