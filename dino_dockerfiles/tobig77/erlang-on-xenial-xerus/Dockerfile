FROM ubuntu:xenial

MAINTAINER Tobias Gerschner <tobias.gerschner@gmail.com>

RUN apt-get update && apt-get upgrade -y  && apt-get install wget -y

RUN cd /tmp; wget https://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb && dpkg -i erlang-solutions_1.0_all.deb

RUN apt-get update && apt-get install esl-erlang -y

CMD ["erl"]
