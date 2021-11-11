FROM ubuntu:18.04
MAINTAINER Manuel Kaufmann <humitos@gmail.com>

RUN apt-get update
RUN apt-get install -y wget unzip git make nodejs npm

# Install latest stable yarn
RUN wget -O - https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update
RUN apt-get install -y yarn

RUN git clone --depth 1 https://github.com/pilas-engine/pilas-engine
RUN cd pilas-engine ; \
    make iniciar

WORKDIR /pilas-engine

CMD make ejecutar
