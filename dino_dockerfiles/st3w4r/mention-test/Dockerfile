FROM ubuntu

MAINTAINER Yanael Barbier

RUN apt-get update
RUN apt-get install -y curl

RUN curl -sL https://deb.nodesource.com/setup_0.12 | sudo bash -

RUN apt-get install -y nodejs
RUN apt-get install -y git

WORKDIR /usr/src/mention

RUN git clone https://github.com/st3w4r/mention-test /usr/src/mention
EXPOSE 9001

CMD ["node", "bin/www"]
