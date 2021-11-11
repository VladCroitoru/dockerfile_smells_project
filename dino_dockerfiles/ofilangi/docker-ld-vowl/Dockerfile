FROM debian:jessie
MAINTAINER Olivier Filangi "olivier.filangi@inra.fr"

# Prerequisites
#----------------------------------------------------------------------------------------
RUN apt-get update && apt-get install -y \
  git \
  build-essential \
  vim \
  npm \
  curl

RUN curl -sL https://deb.nodesource.com/setup_7.x | bash -
RUN apt-get install -y nodejs

RUN git clone https://github.com/VisualDataWeb/LD-VOWL.git

WORKDIR LD-VOWL
RUN npm install

EXPOSE 8080
ENTRYPOINT ["npm", "run-script", "start"]
