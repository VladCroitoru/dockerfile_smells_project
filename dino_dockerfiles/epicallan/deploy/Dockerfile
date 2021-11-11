FROM ubuntu:latest

LABEL maintainer="epicallan.al@gmail.com"

RUN mkdir /src

WORKDIR /src

RUN mkdir uploads

RUN apt-get update

RUN apt-get -y install wget unzip libgmp-dev 

RUN wget https://github.com/epicallan/deploy/releases/download/0.2.6/deploy-build.zip

RUN unzip -q deploy-build.zip

EXPOSE 8888

CMD ["/src/deploy-build/deploy-exe"]
 