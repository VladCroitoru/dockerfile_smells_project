FROM node:7

MAINTAINER Richard <hello@noxan.net>

# Install yarn
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb http://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list

RUN apt-get update
RUN apt-get install -y yarn

# Install awscli
RUN apt-get install -y python-dev python-pip

RUN pip install awscli
