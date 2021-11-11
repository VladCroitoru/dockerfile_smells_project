FROM ubuntu:16.04

RUN apt-get update && apt-get -y install build-essential libboost-all-dev libssl-dev

WORKDIR /

ADD . /

RUN make

CMD ["/run.sh"]
