FROM ubuntu:xenial

RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN pip3 install Flask

COPY . /src
WORKDIR /src

CMD run_test.sh
