FROM ubuntu:latest

RUN apt-get update && \
  apt-get install -y git bison cmake re2c build-essential && \
  apt-get clean

RUN mkdir /opt/clingo && \
  cd /opt/clingo && \
  git init && \
  git remote add origin https://github.com/potassco/clingo.git && \
  git fetch origin master && \
  git pull origin master && \
  git submodule update --init --recursive

WORKDIR /opt/clingo

RUN cmake -H/opt/clingo -B/opt/clingo -DCMAKE_BUILD_TYPE=release -DCLINGO_BUILD_EXAMPLES=ON && \
  cmake --build /opt/clingo

ENV PATH $PATH:/opt/clingo/bin
