FROM ubuntu:trusty

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y qt5-default build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir /code
COPY . /code/
WORKDIR /code/fogleman-ricochet-solver
RUN ./build_ricochet
WORKDIR /code
RUN qmake
RUN make

ENTRYPOINT ["/code/p2t-ricochet-solver"]
