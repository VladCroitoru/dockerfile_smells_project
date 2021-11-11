
FROM ubuntu

MAINTAINER Leo Li

# Update aptitude with new repo
RUN apt-get update

# Install software 
RUN apt-get install -y git

RUN apt-get install -y curl

# install our dependencies and nodejs
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -

RUN apt-get install -y nodejs

# Make demo dir
RUN mkdir /usr/demo/

RUN cd /usr/demo/ && git clone https://github.com/leejulee/TogetherBoard.git

WORKDIR /usr/demo/TogetherBoard

RUN npm install

RUN npm install -g typescript live-server

CMD [ "npm", "t" ]

EXPOSE 3010